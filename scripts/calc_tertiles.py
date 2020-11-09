import json
import os

print('Step 3: Calculating max covid-19 cases and deaths...')

# Change cwd to this file's dir, so we can use a relative path when saving and loading the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)


def filter_countries(dict):
  dict[len(dict) - 1]


def remove_top_countries(covid_19_records, sort_by):
  # The amount of countries to remove:
  remove_amt = 3

  # There aren't numbers for all records with these variables:
  if sort_by == 'cases_per_cap' or sort_by == 'deaths_per_cap':
    covid_19_records = filter(
        lambda record: record.get(sort_by), covid_19_records)

  # Sorts by the given variable:
  sorted_list = sorted(covid_19_records, key=lambda record: record[sort_by])

  # Removes the countries with the top numbers
  for i in range(remove_amt):
    highest_num_country = sorted_list[len(
        sorted_list) - 1]['countriesAndTerritories']
    sorted_list = [
        record for record in sorted_list if record['countriesAndTerritories'] != highest_num_country]
  return sorted_list


def get_max_vals(covid_19_records):
  # # Generate lists of all deaths and cases:
  # deaths = [record['deaths'] for record in covid_19_records]
  # cases = [record['cases'] for record in covid_19_records]

  # # Generate lists of deaths and cases per capita, if the key exists:
  # deaths_per_cap = [record['deaths_per_cap']
  #                   for record in covid_19_records if record.get('deaths_per_cap')]
  # cases_per_cap = [record['cases_per_cap']
  #                  for record in covid_19_records if record.get('cases_per_cap')]

  # return {
  #     "deaths": max(deaths),
  #     "cases": max(cases),
  #     "cases_per_cap": max(cases_per_cap),
  #     "deaths_per_cap": max(deaths_per_cap)
  # }

  def get_max_value(variable):
    sorted_filtered = remove_top_countries(covid_19_records, sort_by=variable)
    max = sorted_filtered[len(sorted_filtered) - 1][variable]
    return max

  return {
      "cases": get_max_value('cases'),
      "deaths": get_max_value('deaths'),
      "cases_per_cap": get_max_value('cases_per_cap'),
      "deaths_per_cap": get_max_value('deaths_per_cap')
  }


# def calc_tertiles(max_vals):
#   return {
#       "deaths": {
#           # "first": max_vals['deaths'] * (1 / 3),
#           "first": max_vals['deaths'] * (1 / 5),
#           # "second": max_vals['deaths'] * (2 / 5),
#           "second": max_vals['deaths'] * (4 / 5),
#           "max": max_vals['deaths']
#       },
#       "cases": {
#           # "first": max_vals['cases'] * (1 / 3),
#           "first": max_vals['cases'] * (1 / 5),
#           # "second": max_vals['cases'] * (2 / 3),
#           "second": max_vals['cases'] * (4 / 5),
#           "max": max_vals['cases']
#       },
#       "cases_per_cap": {
#           # "first": max_vals['cases_per_cap'] * (1 / 3),
#           "first": max_vals['cases_per_cap'] * (1 / 5),
#           # "second": max_vals['cases_per_cap'] * (2 / 3),
#           "second": max_vals['cases_per_cap'] * (4 / 5),
#           "max": max_vals['cases_per_cap']
#       },
#       "deaths_per_cap": {
#           # "first": max_vals['deaths_per_cap'] * (1 / 3),
#           "first": max_vals['deaths_per_cap'] * (1 / 5),
#           # "second": max_vals['deaths_per_cap'] * (2 / 3),
#           "second": max_vals['deaths_per_cap'] * (4 / 5),
#           "max": max_vals['deaths_per_cap']
#       }
#   }


# Data has not yet been transformed, since it is easier to loop through before nesting data with dates:
with open('../data/temp/covid_19_vals_per_cap.json') as input_file:
  covid_19_records = json.loads(input_file.read())['records']

  # The max values are not necessarily all for the same country, since they are just used to set the color limits in the visualizer:
  max_vals = get_max_vals(covid_19_records)

  print(max_vals)

  # tertiles = calc_tertiles(max_vals)

  # with open('../data/temp/covid_19_tertiles.json', 'w') as output_file:
  #   json.dump(tertiles, output_file)
  with open('../data/temp/covid_19_max_vals.json', 'w') as output_file:
    json.dump(max_vals, output_file)
