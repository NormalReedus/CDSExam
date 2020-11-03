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

  # Generate lists of deaths and cases per capita, if the key exists:
  deaths_per_cap = [record['deaths_per_cap']
                    for record in covid_19_records if record.get('deaths_per_cap')]
  cases_per_cap = [record['cases_per_cap']
                   for record in covid_19_records if record.get('cases_per_cap')]

  return {
      "deaths": max(deaths),
      "cases": max(cases),
      "cases_per_cap": max(cases_per_cap),
      "deaths_per_cap": max(deaths_per_cap)
  }


def calc_tertiles(max_vals):
  return {
      "deaths": {
          # "first": max_vals['deaths'] * (1 / 3),
          "first": max_vals['deaths'] * (1 / 5),
          # "second": max_vals['deaths'] * (2 / 5),
          "second": max_vals['deaths'] * (4 / 5),
          "max": max_vals['deaths']
      },
      "cases": {
          # "first": max_vals['cases'] * (1 / 3),
          "first": max_vals['cases'] * (1 / 5),
          # "second": max_vals['cases'] * (2 / 3),
          "second": max_vals['cases'] * (4 / 5),
          "max": max_vals['cases']
      },
      "cases_per_cap": {
          # "first": max_vals['cases_per_cap'] * (1 / 3),
          "first": max_vals['cases_per_cap'] * (1 / 5),
          # "second": max_vals['cases_per_cap'] * (2 / 3),
          "second": max_vals['cases_per_cap'] * (4 / 5),
          "max": max_vals['cases_per_cap']
      },
      "deaths_per_cap": {
          # "first": max_vals['deaths_per_cap'] * (1 / 3),
          "first": max_vals['deaths_per_cap'] * (1 / 5),
          # "second": max_vals['deaths_per_cap'] * (2 / 3),
          "second": max_vals['deaths_per_cap'] * (4 / 5),
          "max": max_vals['deaths_per_cap']
      }
  }


# Data has not yet been transformed, since it is easier to loop through before nesting data with dates:
with open('../data/temp/covid_19_vals_per_cap.json') as input_file:
  covid_19_records = json.loads(input_file.read())['records']

  max_vals = get_max_vals(covid_19_records)

  tertiles = calc_tertiles(max_vals)

  with open('../data/temp/covid_19_tertiles.json', 'w') as output_file:
    json.dump(tertiles, output_file)
