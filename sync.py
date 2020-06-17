import os, json, requests, glob

endpoint='http://localhost:8081/td'
auth='Basic '

url_prefix='https://github.com/w3c/wot-testing/tree/master/events/2020.06.Online/TDs'
#tag='tag:demo.linksmart.eu,2020-06:'

files = glob.glob('./**/*.jsonld', recursive=True)

for filename in files:
    print('\nFile:', filename)
    with open(filename) as f:
        read_data = f.read()
        td = json.loads(read_data)
        if 'id' not in td:
            print("TD has no ID")
            id=filename
            if id.startswith("."):
                id=id[1:]
            # if id.endswith(".jsonld"):
            #     id=id[2:]
            td['id']=url_prefix+id
            
        print('ID:', td['id'])
        # Submit
        continue
        try:
            res = requests.put(endpoint+'/'+td['id'], 
                data=json.dumps(td).encode('utf-8'), 
                headers={'Authorization':auth})
            print('Response:', res.status_code, res.text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
            
