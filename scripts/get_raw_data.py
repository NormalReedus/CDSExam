import json
import urllib.request
import os

print('Step 1: Hacking into the EU mainframe...')

covid_19_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

with urllib.request.urlopen(covid_19_data_url) as input_file:
	# We read the json, but decode it as plaintext, not bytes:
	covid_19_json = input_file.read().decode('utf-8')

	# We save the fetched data to file:
	with open('../data/input/covid_19_raw.json', 'w') as output_file:
		output_file.write(covid_19_json)
