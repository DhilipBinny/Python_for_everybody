
#
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter the url : ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

span_count = 0
sum = 0

spans = soup('span')
for span in spans:
    sum = sum + int(span.contents[0])
    span_count = span_count + 1

print('Count ', span_count)
print('Sum ', sum)