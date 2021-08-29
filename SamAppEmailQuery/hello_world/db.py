import pymysql
import secret

rds_host = secret.db_endpoint
name = secret.db_username
password = secret.db_password
user_db = secret.db_name_user
master_db = secret.db_name_master
order_db = secret.db_name_order
port = 3306
 

def connectUserDb():
    conn = None
    try:
        conn = pymysql.connect(host=rds_host, user=name,
                               passwd=password, db=user_db,
                               connect_timeout=5,
                               cursorclass=pymysql.cursors.DictCursor)
        print("Database connected")
    except Exception as e:
        return None
        print("Database connection has failed due to {}".format(e))

    return conn


def connectOrderDb():
    conn = None
    try:
        conn = pymysql.connect(host=rds_host, user=name,
                               passwd=password, db=order_db,
                               connect_timeout=5,
                               cursorclass=pymysql.cursors.DictCursor)
        print("Database connected")
    except Exception as e:
        return None
        print("Database connection has failed due to {}".format(e))

    return conn


def connectMasterDb():
    conn = None
    try:
        conn = pymysql.connect(host=rds_host, user=name,
                               passwd=password, db=master_db,
                               connect_timeout=5,
                               cursorclass=pymysql.cursors.DictCursor)
        print("Database connected")
    except Exception as e:
        return None
        print("Database connection has failed due to {}".format(e))

    return conn
