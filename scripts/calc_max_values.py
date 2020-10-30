import json
import os

print('Step 3: Calculating max covid-19 cases and deaths...')

# Change cwd to this file's dir, so we can use a relative path when saving and loading the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

def get_max_vals(covid_19_records):
	# Generate lists of all deaths and cases:
	deaths = [record['deaths'] for record in covid_19_records]
	cases = [record['cases'] for record in covid_19_records]

	# Generate lists of deaths and cases per capita, or 0, if the key does not exist
	# We are only using the list to generate max vals, so 0 is a fine null value:
	deaths_per_cap = [record.get('deaths_per_cap', 0) for record in covid_19_records]
	cases_per_cap = [record.get('cases_per_cap', 0) for record in covid_19_records]

	return { "deaths": max(deaths), "cases": max(cases), "cases_per_cap": max(cases_per_cap), "deaths_per_cap": max(deaths_per_cap) }

# Data has not yet been transformed, since it is easier to loop through before nesting data with dates:
with open('../data/temp/covid_19_vals_per_cap.json') as input_file:
	covid_19_records = json.loads(input_file.read())['records']

	max_vals = get_max_vals(covid_19_records)

	with open('../data/temp/covid_19_max_vals.json', 'w') as output_file:
		json.dump(max_vals, output_file)
