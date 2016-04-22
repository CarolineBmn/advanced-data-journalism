import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

# Open input and output files
#datafile = open('output.csv', 'w')
#writer = csv.writer(output)

# Get the HTML of the page
br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")


county_dropdown = soup.find('table',
    {'name': 'ctl00$MainContent$cboCounty'})

#find option tags under select dropdown
county_values = county_dropdown.find_all('option')

for county in county_values:
    count_name = county.text
    county_id = county['value']

    #submit form
    br.select_form(nr=0) 
    br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
    br.form['ctl00$MainContent$cboCounty'] = [county_id]
    br.submit('ctl00$MainContent$btnCountyChange') #this is the submit button on the page

    # Get HTML
    html = br.response().read()

    # Transform the HTML into a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

     # Find the main table using both the "align" and "class" attributes
    main_table = soup.find('table',
        {'id': 'MainContent_dgrdResults'
    })

   output = []
   ouptput.append(county_name)

    for r in main_table.find_all('tr'):
        data = [cell.text for cell in r.find_all('td')]
        

        if data != []:
            if data[0] in ['Hillary Clinton', 'Ted Cruz', 'Donald J. Trump', 'Bernie Sanders', 'John R. Kasich']: 
                ouptput.append(data[3])

        print output


#print county_values


