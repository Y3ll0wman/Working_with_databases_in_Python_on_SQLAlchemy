import pymysql

from database_connection_config import db_config


def test_pymysql():
    conn = pymysql.connect(host=db_config.host, user=db_config.login, port=int(db_config.port), password=db_config.password, database=db_config.db_name)

    # Curren set of records
    cursor = conn.cursor()

    cursor.execute('SELECT customer_id FROM billing.account_status WHERE plan_id = 1550')

    row = cursor.fetchone()

    rest_of_rows = cursor.fetchall()

    all_rows = cursor.fetchmany()

    # print(f'\n{row}')
    # print('__________________')
    # print(rest_of_rows)
    print('__________________')
    print(all_rows)

    cursor.close()
    conn.close()
