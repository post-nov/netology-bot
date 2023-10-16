import asyncio

from constants import DEBUG, USER_DATA_FIELDS


async def asleep(seconds: int) -> None:
    """ Асинхронно заснуть на некоторое время """
    if DEBUG:
        print(f'Асинхронно поспали {seconds} секунд')
        return

    await asyncio.sleep(seconds)


async def process_user_data(user_id: int, user_data: dict) -> None:
    """ Сохранить данные о пользователе"""

    print(f'Данные пользователя с идентификатором {user_id}:')
    for field in USER_DATA_FIELDS:
        if user_data.get(field):
            print(f'{field}={user_data.get(field)}')
