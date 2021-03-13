import pathlib
import random
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1
        # Текущее поколение
        self.n_generation = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        if randomize:
            grid = [[random.randint(0, 1) for n in range(self.rows)] for n in range(self.cols)]
        else:
            grid = [[0 for n in range(self.rows)] for n in range(self.cols)]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        neighbours_cells_values = []
        for n in range(cell[0] - 1, cell[0] + 1 + 1):
            for m in range(cell[1] - 1, cell[1] + 1 + 1):
                if n == cell[0] and m == cell[1]:
                    pass
                else:
                    if 0 <= n < len(self.curr_generation):
                        if 0 <= m < len(self.curr_generation[0]):
                            neighbours_cells_values.append(self.curr_generation[n][m])

        return neighbours_cells_values

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        updated_grid = [n[:] for n in self.curr_generation]
        for n in range(len(self.curr_generation)):
            for m in range(len(self.curr_generation[0])):
                cell = (n, m)
                cell_status = self.curr_generation[n][m]
                count_of_alive_neighbours = sum(self.get_neighbours(cell))
                if cell_status == 1:
                    if count_of_alive_neighbours == 2 or count_of_alive_neighbours == 3:
                        pass
                    else:
                        updated_grid[n][m] = 0

                elif cell_status == 0:
                    if count_of_alive_neighbours == 3:
                        updated_grid[n][m] = 1
                    else:
                        pass

        return updated_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = [n[:] for n in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        self.n_generation += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations  # type: ignore

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return not self.curr_generation == self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r") as file:
            file_lines = file.readlines()
            file_lines = [line.rstrip() for line in file_lines]

        read_out_grid = [[int(m) for m in n] for n in file_lines]
        game_template_from_file = GameOfLife((len(read_out_grid), len(read_out_grid[0])))
        game_template_from_file.curr_generation = read_out_grid
        return game_template_from_file

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        f = open(filename, "w")
        for n in range(len(self.curr_generation)):
            for m in self.curr_generation[n]:
                f.write(str(m))
            f.write("\n")
