from databases.models.billing import AccountStatus, Plans
from databases.db_client import DatabaseConnect
from sqlalchemy import select, join, desc


def test_join_zero():
    query = DatabaseConnect.session.query(AccountStatus.customer_id, Plans.name, AccountStatus.balance) \
        .join(Plans, AccountStatus.plan_id == Plans.id) \
        .order_by(desc(AccountStatus.balance)) \
        .limit(10)

    DatabaseConnect.session.close()

    for row in query:
        print({
            "customer_id": row.customer_id,
            "plan_name": row.name,
            "balance": row.balance
        })


def test_join_one():
    j = join(AccountStatus, Plans, AccountStatus.plan_id == Plans.id)

    query = select(AccountStatus.customer_id, Plans.name, AccountStatus.balance) \
        .select_from(j) \
        .order_by(desc(AccountStatus.balance))

    result = DatabaseConnect.session.execute(query)
    rows = result.fetchmany(10)

    result.close()
    DatabaseConnect.session.close()

    for row in rows:
        print(row)


def test_join_two():
    query = select(AccountStatus.customer_id, Plans.name, AccountStatus.balance) \
        .join(Plans, AccountStatus.plan_id == Plans.id) \
        .order_by(desc(AccountStatus.balance)) \
        .limit(10)

    result = DatabaseConnect.session.execute(query)

    rows = result.fetchall()

    result.close()
    DatabaseConnect.session.close()

    for row in rows:
        print({
            "customer_id": row.customer_id,
            "plan_name": row.name,
            "balance": row.balance
        })
