import json
import urllib.request
import os

print('Step 1: Hacking into the EU mainframe...')

covid_19_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

with urllib.request.urlopen(covid_19_data_url) as file:
	covid_19_json = json.dumps(json.loads(file.read()))

	# We save the fetched data to file:
	with open('../input_data/covid_19_records.json', 'w') as output_file:
		output_file.write(covid_19_json)

print('DONE: get_input_data.py\n')