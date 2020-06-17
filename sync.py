import os, json, requests, glob, sys

endpoint=os.environ['ENDPOINT']
auth=os.environ['AUTHORIZATION']

# for TD without an ID
uri_tag_prefix='tag:demo.linksmart.eu,2020-06:'

files = glob.glob('./**/*.jsonld', recursive=True)


def put(td):
    res = requests.put(endpoint+'/td/'+td['id'], 
        data=json.dumps(td).encode('utf-8'), 
        headers={'Authorization':auth})

    print('Response:', res.status_code)
    if res.status_code != 200 and res.status_code != 201:
        print('Response body:\n', json.dumps(json.loads(res.text), indent=4), file=sys.stderr)
    return res.status_code

def validate(td):
    res = requests.get(endpoint+'/validation', 
                data=json.dumps(td).encode('utf-8'), 
                headers={'Authorization':auth})
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
            td['id']=uri_tag_prefix+id
            
        print('ID:', td['id'])
        # Submit
        try:
            code = put(td)
            if code == 400:
                print('Validate again:')
                validate(td)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    print('----------\n')
