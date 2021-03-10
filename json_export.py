#!/usr/bin/env python3

import json
import requests
from time import sleep

while True:
    response = requests.request(url="http://my_nginx/status/format/json", method="GET")
    vts_json = json.loads(response.text)
    upstream_servers = vts_json['upstreamZones']['trendyol']
    
    with open("/usr/local/nginx/html/metrics", "w") as f:
        f.write("# HELP vts_upstream_response_time\n# TYPE vts_upstream_response_time gauge\n")
        for server in upstream_servers:
            hostname = server['server']
            response_time = server['responseMsec']
            f.write('vts_upstream_response_time{{hostname=\"{}\"}} {}\n'.format(hostname, response_time))
    sleep(30)

