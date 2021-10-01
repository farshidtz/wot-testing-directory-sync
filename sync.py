import os, json, requests, glob

ENDPOINT=os.getenv('ENDPOINT') # directory root endpoint
AUTH=os.getenv('AUTHORIZATION') # authorization header (optional)
TTL=os.getenv('TTL') # seconds (optional: overrides existing ttl)

if ENDPOINT is None:
    print("ERROR: ENDPOINT not set.")
    exit(1)

files = glob.glob('./**/*.jsonld', recursive=True)

# create a TD or update an existing one
def put(td):
    url = ENDPOINT+'/things/'+td['id']
    print('PUT', url)
    res = requests.put(url, data=json.dumps(td).encode('utf-8'), headers={'Authorization':AUTH})
    print('Response:', res.status_code, res.reason)

    if res.text != "":
        print('Response body:\n', json.dumps(json.loads(res.text), indent=4))
    
    return res.status_code

# create a TD
def post(td):
    url = ENDPOINT+'/things'
    print('POST', url)
    res = requests.post(url, data=json.dumps(td).encode('utf-8'), headers={'Authorization':AUTH})
    print('Response:', res.status_code, res.reason)
    if res.status_code == 201:
        print('Generated ID:', res.headers['Location'])

    if res.text != "":
        print('Response body:\n', json.dumps(json.loads(res.text), indent=4))
    
    return res.status_code

def submit(td):
    if 'id' in td:
        print('ID:', td['id'])
        code = put(td)
    else:
        print("--> TD has no ID. Will POST.")
        code = post(td)


for filename in files:
    print('\n----------')
    print('File:', filename)
    with open(filename) as f:
        try:
            td = json.loads(f.read())
        except ValueError as e:
            print('Error loading JSON file:\n', e)
            continue

        # set/override ttl
        if TTL is not None:
            if 'registration' in td:
                td['registration']['ttl']=int(TTL)
            else:
                td['registration'] = {'ttl': int(TTL)}

        try:
            submit(td)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
