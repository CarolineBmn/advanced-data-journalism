#Caroline Bauman API assignment API key: ac9b284431ca477cb1c77ca766acc074

import urllib, urllib2, json

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=ac9b284431ca477cb1c77ca766acc074&state=mo&fields=sponsors,title').read()

data = json.loads(response)

#output = open('api.csv', 'w')
#writer = csv.writer(output)

for bill in data:
    encoded_bill_id = urllib.unquote(bill['sponsors'][0]['name']).encode('utf-8')
    encoded_bill_id2 = urllib.unquote(bill['title']).encode('utf-8')
    print encoded_bill_id, encoded_bill_id2
    # writer.writerow(data)
