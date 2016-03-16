import urllib2, csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

# Get the HTML of the page
br = mechanize.Browser()
br.open('https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500')
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
    {'align': 'center',
    'class': ['collapse', 'shadow', 'BCSDTable']
})

# Now get the data from each table row
for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(data)
