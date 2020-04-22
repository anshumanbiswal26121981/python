#!/usr/bin/python3

import json
from graphqlclient import GraphQLClient
import os
import glob
import sys
import datetime
import pytz
from datetime import datetime, timezone

rest_url = "http://gql-cpbu.svc.eng.vmware.com/datadirect"
client = GraphQLClient(rest_url)

# Count the arguments
arguments = len(sys.argv) - 1
position = 1
json_dir_name = os.getcwd()


###
# Process the file and send the results to the dashboard using the data direct apis
###
def send_results_to_dashboard(file_name, is_complete_file_name):
    if is_complete_file_name:
        complete_file_name = file_name
    else:
        complete_file_name = json_dir_name + '/' + file_name

    print("{} : processing".format(complete_file_name))
    try:
        with open(complete_file_name) as json_file:
            json_string = json.dumps((json.load(json_file)))
            params = json.loads(json_string)
            load_result_to_dashboard(params)
    except FileNotFoundError:
        print('File does not exist')
    except IOError:
        print('File is not accessible')


###
# Load the results to the dashboard
###
def load_result_to_dashboard(param_list):
    dd_query = """mutation($data : [PushPQTestInput!]!)
                  {pushPQTestData(input: $data)
                  {status,message}}"""
    result = client.execute(dd_query, {"data": param_list})
    utc_dt = datetime.now(timezone.utc)
    print("UTC time     {}".format(utc_dt.isoformat()))
    print("Api execution result {} ".format(result), end='\r\n')


if arguments >= position:
    while (arguments >= position):
        file_name = sys.argv[position]
        send_results_to_dashboard(file_name, False)
        position = position + 1
else:
    json_pattern = os.path.join(json_dir_name, '*.json')
    file_list = glob.glob(json_pattern)
    for file_name in file_list:
        send_results_to_dashboard(file_name, True)
