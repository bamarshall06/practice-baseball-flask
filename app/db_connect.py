import pymysql

### DB CONNECTION

def connect():
    connection = pymysql.connect(host='baseball.cqyhggbcdmue.us-east-1.rds.amazonaws.com',
                                 port=3306,
                                 database='sys',
                                 user='admin',
                                 password='pepsi2222',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection