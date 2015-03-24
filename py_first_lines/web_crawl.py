from BeautifulSoup import BeautifulSoup
import urllib

data= urllib.urlopen('http://www.yahoo.com')
refine=BeautifulSoup(data.read())
print refine
