import pymysql

def connectDb():
    connectionObj = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root1',
            db='vardj', charset='utf8')
    print('Database connected successfully')
    return connectionObj

def disconnectDb(conn):
    conn.close()
    print('Database disconnected successfully')

def createTable():
    query = 'create table IF NOT EXISTS mobiles(id int primary key auto_increment, name varchar(30) not null, price float)'

    connectionObject = connectDb()
    cursor = connectionObject.cursor()
    cursor.execute(query)
    # connectionObject.commit()
    cursor.close()
    disconnectDb(connectionObject)

createTable()