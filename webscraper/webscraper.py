import webbrowser
import sys
import databaseop as dbop
import genop as gen

try:
    mydb = dbop.connect()
    sql = dbop.buildsql()
    dbop.printdata(mydb, sql)
    page = ''
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
    

