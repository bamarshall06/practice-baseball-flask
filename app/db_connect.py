import pymysql

### DB CONNECTION

def connect():
    connection = pymysql.connect(host='this.is.you.aws.server.host.com',
                                 port=3306,
                                 database='sys',
                                 user='admin',
                                 password='putyourpasswrodhere',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
