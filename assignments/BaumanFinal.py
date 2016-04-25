#Caroline Bauman Final Project Advanced Data Spring 2016

import urllib2, csv
import requests
from bs4 import BeautifulSoup

# Open input and output files
#datafile = open('output.csv', 'w')
#writer = csv.writer(output)

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

print r.content

#for forms in br.forms():
    #dir(forms)
    #print forms

#submit form
#br.select_form(nr=0)
#br.form['_id'] = ['Tennessee']
#br.form ['search_by']
#br.submit

#for state in state_ids:
    #state_name = state.text
    #state_id = state['value']



# Get HTML
    #html = br.response().read()

# Transform the HTML into a BeautifulSoup object
    #soup = BeautifulSoup(html, "html.parser")



    