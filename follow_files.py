# Part of Py4e Specialization: Using Python to Access Web Data
# Sebastian Quirarte | sebastianquirajus@gmail.com

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieves variable anchor tag
tags = soup('a')
counter = 0
for tag in tags:
    counter = counter + 1
    # Defines value of anchor tag
    if counter == 18:
        new_url = (tag.get('href', None))
        break
    else:
        continue

for i in range(6):
    url = new_url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    counter = 0
    for tag in tags:
        counter = counter + 1
        # Defines value of anchor tag
        if counter == 18:
            new_url = (tag.get('href', None))
            break
        else:
            continue

pieces = new_url.split("_")
name = (pieces[2].split("."))[0]
print(name)
