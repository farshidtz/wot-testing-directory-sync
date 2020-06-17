import os, json, requests, glob

ENDPOINT=os.environ['ENDPOINT'] # directory root endpoint
AUTH=os.environ['AUTHORIZATION'] # authorization header
TTL=os.environ['TTL'] # seconds
URI_PREFIX=os.environ['URI_PREFIX'] # for TDs without an ID

files = glob.glob('./**/*.jsonld', recursive=True)


def put(td):
    path = '/td/'+td['id']
    print('PUT', path)
    res = requests.put(ENDPOINT+path, 
        data=json.dumps(td).encode('utf-8'), 
        headers={'Authorization':AUTH})

    print('Response:', res.status_code, res.reason)
    if res.text != "":
        print('Response body:\n', json.dumps(json.loads(res.text), indent=4))
    return res.status_code

def validate(td):
    path = '/validation'
    print('GET', path)
    res = requests.get(ENDPOINT+'/validation', 
                data=json.dumps(td).encode('utf-8'), 
                headers={'Authorization':AUTH})
    print(json.dumps(json.loads(res.text), indent=4))

for filename in files:
    print('File:', filename)
    with open(filename) as f:
        read_data = f.read()
        td = json.loads(read_data)
        if 'id' not in td:
            print("--> TD has no ID. Construct a Tag URI with filename:")
            id=filename
            if id.startswith("./"):
                id=id[2:]
            if id.endswith(".jsonld"):
                id=id[:-7]
            td['id']=URI_PREFIX+id
            
        print('ID:', td['id'])

        # inject ttl
        td['ttl']=int(TTL)

        # Submit
        try:
            code = put(td)
            if code == 400:
                print('\nJust validate:')
                validate(td)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    print('----------\n')
