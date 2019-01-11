import pyperclip 
import requests
from genop import pyperclip

def PastePaperClipData():
    pyperclip.paste()

def printPageInfo(pagestr):
    res = requests.get(pagestr)
    res.raise_for_status()
    print type(res)
    print res.status_code == requests.codes.ok
    print len(res.text)
    print (res.text[:500]) # returns the html