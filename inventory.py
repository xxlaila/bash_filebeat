#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json

def get_ecs_info(hostList):
    inventory = {
        'opsworks': {
            'hosts': [],
            'vars': {}
        },
        '_meta': {
            "hostvars": {}
        }
    }
    for host in hostList:
        inventory['opsworks']['hosts'].append(host)
        inventory['_meta']['hostvars'][host] = {"ip": host}
    return json.dumps(inventory, indent=4)


if __name__ == "__main__":
    hostListString = os.environ.get('host_list')
    hostList = hostListString.split(',')
    print(get_ecs_info(hostList))

