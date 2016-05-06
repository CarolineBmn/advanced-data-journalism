#Caroline Bauman Final Project Advanced Data Spring 2016

import urllib2, csv
import requests
from bs4 import BeautifulSoup

# Get the HTML of the page
r = requests.get('https://www.brewersassociation.org/directories/breweries/')

html = r.content

#print html

soup = BeautifulSoup(html, "html5lib")

#print soup.prettify()

#get dropdown
state_dropdown = soup.find('ul',
    {'id': 'state_select'})

#print state_dropdown

#find option tags under select dropdown
state_ids = state_dropdown.find_all('li')

#print state_ids

formdata = {'action': 'get_breweries', '_id': 'Tennessee', 'search_by': 'statename'}

r = requests.post("https://www.brewersassociation.org/wp-admin/admin-ajax.php", data=formdata)

html = r.content

soup = BeautifulSoup(html, "html5lib")

breweries = soup.find_all('ul', class_ = 'vcard simple')


output = []

for r in breweries:
    names = r.find('li', class_ = 'name').text
    address = r.find('li', class_ = 'address').text
    brewtype = r.find('li', class_ = 'brewery_type').text
    #print names, address, brewtype
    url = r.find('li', class_ = 'url')
    if url == None:
        pass
    if url is not None:
        h = url.find('a').get('href')

    brewery_list = [names, address, brewtype, h]
    output.append(brewery_list)

for row in output:
    print row
 
# Open input and output files
datafile = open('output.csv', 'w')
writer = csv.writer(datafile)
writer.writerows(output)

    