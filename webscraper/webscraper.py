import webbrowser
import sys
import pyperclip 
from webscraper import pyperclip
import requests


#if len(sys.argv) > 1:
#    address = ' '.join(sys.argv[1:])
#else:
#    address = pyperclip.paste()
#webbrowser.open('http://www.google.com/maps/place/' + address)
try:
    page = ''
    while page <> '999':
        if page == 999: break
        print "Enter a page to read"
        page = raw_input()
        pagestr = 'http://www.' + page
        print pagestr

        res = requests.get(pagestr)
        res.raise_for_status()
        print type(res)
        print res.status_code == requests.codes.ok
        print len(res.text)
        print (res.text[:500])

        webbrowser.open(pagestr)
except Exception as exc:
    print 'program ended %s' % (exc)
    

