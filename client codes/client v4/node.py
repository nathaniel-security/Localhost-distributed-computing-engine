import json
with open('config.json') as json_file:  
    data = json.load(json_file)
    for p in data['config']:
        node_id = p['node id']
        node_password=p['node password']

