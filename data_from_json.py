# Part of Py4e Specialization: Using Python to Access Web Data
# Sebastian Quirarte | sebastianquirajus@gmail.com

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print ("Retrieving", url)

# Retrieves json data from url
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
js = json.loads(data)
print("Retrieved",len(data),"characters")

# Finds and sums all counts
count = 0
sum = 0
for i in js["comments"]:
    count += 1
    sum += (i["count"])

print("Count:", count)
print("Sum:", sum)
