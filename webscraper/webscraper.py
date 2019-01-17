#################################################
# DATE : 2019 
# DEV  : B.Stevens
# ABOUT: Gets a list of urls that can be executed
##################################################
import webbrowser
import sys
import databaseop as dbop
import genop as gen

try:
    # database operations
    mydb = dbop.connect()
    sql = dbop.buildsql()
    dbop.printdata(mydb, sql)
    page = ''
    # loop while not 999
    while page <> '999':
        if page == 999: break
        print "Enter a page to read [999 to exit program]:"
        page = raw_input()
        pagestr = 'http://196.10.10.254/' + page
        print pagestr
        gen.printPageInfo(pagestr)
        # open the requested page
        webbrowser.open(pagestr)
except Exception as exc:
    print 'program ended %s' % (exc)
    

