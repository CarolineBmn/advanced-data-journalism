#scraping assignment Caroline Bauman

import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

#Get output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

# Fill out the form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
#br.form['ctl00$MainContent$cboCounty'] = ['001, 003']
# value must be submitted as a string inside of a list, a one value list

# Submit the form
br.submit('ctl00$MainContent$btnElectionType')
#br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

#Loop over each county listed in the "counties" dropdown
dropdown = soup.find('select', id = 'cboCounty').find_all('option')

counties = []
#dictionaries in a list

for i in dropdown:
    county = {'name':i.text, 'num':i['value']}
    counties.append(county)
    #print type(i)
    #print dir(i)
    #print i.text
    #print county

for county in counties: 
    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboCounty'] = [county['num']]
    br.submit('ctl00$MainContent$btnCountyChange')
    html = br.response().read()
    soup = BeautifulSoup(html, "html.parser")


# Find the main table using both the "align" and "class" attributes
    main_table=soup.find('table', id ='MainContent_dgrdResults')
    #print main_table.prettify()

    for row in main_table.find_all('tr'):
        data = [cell.text.replace(u'\xa0', '') for cell in row.find_all('td') ]
        #writer.writerow(data)
        if data:
            in ['Hillary Clinton', 'Ted Cruz', 'Donald J. Trump', 'Bernie Sanders', 'John R. Kasich']: 
                print option_values[i], data[0], data[3]

 i=i+1
    if i == len(option_values):
        break



