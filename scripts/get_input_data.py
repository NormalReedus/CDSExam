import json
import urllib.request
import os
from pathlib import Path

covid_19_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

with urllib.request.urlopen(covid_19_data_url) as covid_19_json:
	# The file contains a list "records" which holds the information:
	covid_19_dict = json.loads(covid_19_json.read())['records']

	# We save the fetched data to file:
	with open('../input_data/covid_19_records.json', 'w') as output_file:
		json.dump(covid_19_dict, output_file)
