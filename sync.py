import os, json, requests, glob

ENDPOINT=os.environ['ENDPOINT'] # directory root endpoint
AUTH=os.environ['AUTHORIZATION'] # authorization header
TTL=os.environ['TTL'] # seconds
URI_PREFIX=os.environ['URI_PREFIX'] # for TDs without an ID

files = glob.glob('./**/*.jsonld', recursive=True)

# add a TD or update an existing one
def put(td):
    url = ENDPOINT+'/td/'+td['id']
    print('PUT', url)
    res = requests.put(url, data=json.dumps(td).encode('utf-8'), headers={'Authorization':AUTH})
    print('Response:', res.status_code, res.reason)

    if res.text != "":
        print('Response body:\n', json.dumps(json.loads(res.text), indent=4))
    
    return res.status_code

# validate a TD
def validate(td):
    url = ENDPOINT+'/validation'
    print('GET', url)
    res = requests.get(url, data=json.dumps(td).encode('utf-8'), headers={'Authorization':AUTH})
    print('Validation results:\n', json.dumps(json.loads(res.text), indent=4))

for filename in files:
    print('File:', filename)
    with open(filename) as f:
        td = json.loads(f.read())

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
                print('\nValidate the TD explicitly:')
                validate(td)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    print('----------\n')
