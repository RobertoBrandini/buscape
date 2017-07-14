import requests
import json
import csv
import io

lines = open('productIds.csv', 'r').read().split('\n')

for line in lines:
    name = line.split(';')[0]
    id = line.split(';')[1]
    url = "http://www.buscape.com.br/ajax/historicoPreco?idu=" + id + "&days=365"
    response = requests.get(url)
    data = response.json()

    #with open('output_buscape' + id + '.json', 'w') as outfile:
    #    json.dump(data, outfile)
    
    b = data['historicos']
        
    field = b[0].keys()
    f = open('prices/' + name + '.csv', 'w')
    csv_file = csv.DictWriter(f,fieldnames=field,delimiter=';', lineterminator='\n')
    csv_file.writeheader()

    for item in range(0,len(b)):
        val = {}
        for line in b[item].keys():
            val[line] = b[item][line]
        csv_file.writerow(val)
    f.close()

#http://www.buscape.com.br/ajax/historicoPreco?idu=619257&days=90