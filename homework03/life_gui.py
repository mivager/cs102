import pygame  # type: ignore
from life import GameOfLife
from pygame import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.screen_size = (
            self.life.rows * self.cell_size,
            self.life.cols * self.cell_size,
        )
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        for a in range(0, self.life.rows * self.cell_size, self.cell_size):
            pygame.draw.line(
                self.screen,
                pygame.Color("black"),
                (a, 0),
                (a, self.life.cols * self.cell_size),
            )
        for b in range(0, self.life.cols * self.cell_size, self.cell_size):
            pygame.draw.line(
                self.screen,
                pygame.Color("black"),
                (0, b),
                (self.life.rows * self.cell_size, b),
            )

    def draw_grid(self) -> None:
        for b_coordinate in range(len(self.life.curr_generation[0])):
            for a_coordinate in range(len(self.life.curr_generation)):
                if self.life.curr_generation[a_coordinate][b_coordinate] == 1:
                    cell_color = "green"
                else:
                    cell_color = "white"
                pygame.draw.rect(
                    self.screen,
                    pygame.Color(cell_color),
                    (
                        b_coordinate * self.cell_size,
                        a_coordinate * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:  # type: ignore
                    running = False
                # PAUSE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        while True:
                            event = pygame.event.wait()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    column_num = event.pos[0] // self.cell_size
                                    row_num = event.pos[1] // self.cell_size
                                    self.life.curr_generation[row_num][column_num] = 1
                                    self.draw_grid()
                                    self.draw_lines()
                                    pygame.display.flip()
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
            self.life.step()
        pygame.quit()


if __name__ == "__main__":
    life = GameOfLife((10, 10))
    ui = GUI(life)
    ui.run()
