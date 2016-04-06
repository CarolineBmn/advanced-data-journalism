import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/')

# Fill out the form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']

# Submit the form
br.submit('ctl00$MainContent$btnElectionType')

# Get HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
    {'id': 'MainContent_dgrdResults'}
)

# Now get the data from each table row
for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    print data