import csv, mechanize
from bs4 import BeautifulSoup

#Get output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/')
html = br.response().read()

print html