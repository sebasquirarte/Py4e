# Part of Py4e Specialization: Using Python to Access Web Data
# Sebastian Quirarte | sebastianquirajus@gmail.com 

from urllib import request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print ("Retrieving", url)
XML = request.urlopen(url)
data = XML.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount=len(results)
isum=0

for result in results:
    isum += int(result.find('count').text)

print("Count:",icount)
print("Sum:",isum)
