from databases.models.billing import AccountStatus
from databases.db_client import DatabaseConnect


def test_update():
    DatabaseConnect.session.query(AccountStatus).filter(AccountStatus.customer_id =="cp77524").update({
        AccountStatus.balance: 1000
    })

    DatabaseConnect.session.commit()
    DatabaseConnect.session.close()
