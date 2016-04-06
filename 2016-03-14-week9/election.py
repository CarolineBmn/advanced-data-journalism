import csv, mechanize
from bs4 import BeautifulSoup

#Get output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/')

br. select_form(nr=0)

br.form['ctl00$MainContent$cboElectionNames'] = ['75000356']

br.submit('ctl00$MainContent$btnElectionType')