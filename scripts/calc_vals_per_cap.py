import json
import os

print('Step 2: Calculating deaths and cases per capita...')

# Change cwd to this file's dir, so we can use a relative path when saving and loading the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

def insert_variable_per_cap_columns(covid_19_records):
	for record in covid_19_records:
		# Skip cases in international waters etc:
		if record['popData2019'] == None:
			continue
		
		# Insertion of new 'columns':
		record['deaths_per_cap'] = record['deaths'] / record['popData2019']
		record['cases_per_cap'] = record['cases'] / record['popData2019']

with open('../data/input/covid_19_raw.json') as input_file:
	covid_19_dict = json.loads(input_file.read())

	insert_variable_per_cap_columns(covid_19_dict['records'])

	with open('../data/temp/covid_19_vals_per_cap.json', 'w') as output_file:
		json.dump(covid_19_dict, output_file)
