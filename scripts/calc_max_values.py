import json
import os

# Change cwd to this file's dir, so we can use a relative path when saving and loading the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

def get_max_values(covid_19_records):
    deaths = [record['deaths'] for record in covid_19_records]
    cases = [record['cases'] for record in covid_19_records]
		
		deaths_per_pop = [(record['daths'] / record['popData2019']) for record in covid_19_records]
		cases_per_pop = [(record['cases'] / record['popData2019']) for record in covid_19_records]

    return (max(deaths), max(cases))

with open('../input_data/covid_19_records.json') as input_file:
	covid_19_records = json.loads(file.read())['records']

	max_vals = get_max_values(covid_19_records)
