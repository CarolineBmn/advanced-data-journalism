#scraping assignment Caroline Bauman

import csv, mechanize
from bs4 import BeautifulSoup

#Get output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

# Fill out the form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
#ask James about value on right

# Submit the form
#br.submit('ctl00$MainContent$btnElectionType')

# Get HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

#Loop over each county listed in the "counties" dropdown
dropdown = soup.find('select', id = 'cboCounty')

print dropdown

#Scrape results ONLY for the five active candidates: Clinton, Sanders, Cruz, Kasich and Trump
#for row in dropdown
#Display that information (either printed to the terminal or as CSV) in a format