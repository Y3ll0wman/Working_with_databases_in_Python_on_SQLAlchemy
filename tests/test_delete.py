from databases.models.billing import AccountStatus
from databases.db_client import DatabaseConnect


def test_delete():
    DatabaseConnect.session.query(AccountStatus).filter(AccountStatus.customer_id =="cp77524").delete()

    DatabaseConnect.session.commit()
    DatabaseConnect.session.close()
