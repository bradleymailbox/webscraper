import mysql.connector

#connect to database
def connect():
    db = mysql.connector.connect(
        host="196.10.10.254",
        user="sysuser",
        password="sysuser123",
        database="systems"
    )
    print "Connected to database..."
    return db
#get value from database
def printdata(db, sql):
    mycursor = db.cursor()
    mycursor.execute(sql)
    print "retrieving records"
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
#function to build a sql string
def buildsql():
    return "SELECT concat('#', sysid, ' - ', systemname, '| LINK:~/', syslink) AS ITEM FROM systems.syslist" 