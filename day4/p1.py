import pymysql

def connectDb():
    connectionObj = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root1',
            db='vardj', charset='utf8')
    print('Database connected successfully')
    return connectionObj

connectionObject = connectDb()
connectionObject.close()
print('Database disconnected successfully')

    
    


