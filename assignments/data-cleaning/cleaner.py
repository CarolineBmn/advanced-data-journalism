# -*- coding: utf-8 -*-
import csv
import string

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleanme-clean.csv', 'w')
specials = "&NBSP;"

reader = csv.DictReader(csvfile)

writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()
    
for row in reader:
    for k, v in row.iteritems():
        row[k]=row[k].upper()
        row["zip"]=row["zip"].zfill(5)
        row[k] = row[k].replace(specials, ' ')
    print row
