import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    friends = get_friends(user_id, 10000, fields=["bdate"]).items
    current_date = dt.datetime.today().year
    ages = []
    for friend in friends:
        try:
            ages.append(current_date - dt.datetime.strptime(friend["bdate"], "%d.%m.%Y").year)  # type: ignore
        except:
            pass
    try:
        return statistics.median(ages)
    except statistics.StatisticsError:
        return None
