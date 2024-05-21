from databases.models.billing import AccountStatus
from databases.db_client import DatabaseConnect
from sqlalchemy import select, desc


def test_select_many_raws():
    query = select(AccountStatus.customer_id, AccountStatus.balance) \
        .filter(AccountStatus.plan_id == 1550) \
        .order_by(desc(AccountStatus.balance))

    result = DatabaseConnect.session.execute(query)

    row = result.fetchmany(2)

    result.close()
    DatabaseConnect.session.close()

    if row[0] is not None:
        print(f'\n{row}')
    else:
        raise Exception('Строка не найдена')


def test_select_all_raws():
    query = select(AccountStatus.customer_id, AccountStatus.balance) \
        .filter(AccountStatus.plan_id == 1550) \
        .order_by(desc(AccountStatus.balance))

    result = DatabaseConnect.session.execute(query)

    row = result.fetchall()

    result.close()
    DatabaseConnect.session.close()

    if row[0] is not None:
        print(f'\n{row}')
    else:
        raise Exception('Строка не найдена')
