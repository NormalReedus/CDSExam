import json
import os

print('Step 3: Calculating max covid-19 cases and deaths...')

# Change cwd to this file's dir, so we can use a relative path when saving and loading the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

def get_max_values(covid_19_records):
	# Generate lists of all deaths and cases:
	deaths = [record['deaths'] for record in covid_19_records]
	cases = [record['cases'] for record in covid_19_records]

	# Generate lists of deaths and cases per capita (ignoring cases that were not in a geographic area):
	deaths_per_cap = [(record['deaths'] / record['popData2019']) for record in covid_19_records if record['popData2019'] != None]
	cases_per_cap = [(record['cases'] / record['popData2019']) for record in covid_19_records if record['popData2019'] != None]

	return { "max_deaths": max(deaths), "max_cases": max(cases), "max_cases_per_cap": max(cases_per_cap), "max_deaths_per_cap": max(deaths_per_cap) }

# Data has not yet been transformed, since it is easier to loop through before nesting data with dates:
with open('../data/temp/covid_19_vals_per_cap.json') as input_file:
	covid_19_records = json.loads(input_file.read())['records']

	max_vals = get_max_values(covid_19_records)

	with open('../data/temp/covid_19_max_vals.json', 'w') as output_file:
		json.dump(max_vals, output_file)
