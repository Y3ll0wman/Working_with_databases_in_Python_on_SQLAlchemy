from databases.models.billing import AccountStatus
from databases.db_client import DatabaseConnect
from sqlalchemy import select


def test_select():
    query = select(AccountStatus.balance).where(AccountStatus.customer_id == 'cp77524')

    result = DatabaseConnect.session.execute(query)

    row = result.fetchone()

    result.close()
    DatabaseConnect.session.close()

    if row is not None:
        print(f'\n{row}')
    else:
        raise Exception('Строка не найдена')
