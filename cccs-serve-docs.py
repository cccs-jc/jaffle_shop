#!/opt/conda/bin/python3.8


import json
import os

search_str = 'o=[i("manifest","manifest.json"+t),i("catalog","catalog.json"+t)]'

with open('target/index.html', 'r') as f:
    content_index = f.read()

with open('target/manifest.json', 'r') as f:
    json_manifest = json.loads(f.read())

with open('target/catalog.json', 'r') as f:
    json_catalog = json.loads(f.read())

with open('target/index2.html', 'w') as f:
    new_str = "o=[{label: 'manifest', data: "+json.dumps(json_manifest)+"},{label: 'catalog', data: "+json.dumps(json_catalog)+"}]"
    new_content = content_index.replace(search_str, new_str)
    f.write(new_content)

with open('target/index2.html', 'r') as f:
    content_index = f.read()

os.rename('target/index.html', 'target/index.html.backup')
os.rename('target/index2.html', 'target/index.html')

os.chdir('./target')


import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()