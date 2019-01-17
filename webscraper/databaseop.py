import mysql.connector

#connect to database
def connect():
    db = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
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