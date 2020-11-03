import json
import os

print('Step 5: Sorting and filtering the data for the visualization...')

# This script sorts the covid_19_transformed.json, filters away the redundant properties
# and merges the json-file with the covid_19_max_values.json
# The output is putinto the output_data folder.

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

# Paths to the json files we need
tertiles_path = "../data/temp/covid_19_tertiles.json"
covid_19_path = "../data/temp/covid_19_transformed.json"

# The sort function takes a compare function
# When sorting, we want to get the earliest date first
# The function creates an integer by concatenating year-month-day and sorts on that


def compare_function(e):
  split_date = e["date"].split("/")
  return int(split_date[2] + split_date[1] + split_date[0])


# loads both covid_19_max_values.json and covid_19_transformed.json
# sorts the records list in the data and merges the two files into a final product
# Filtering might be added later
with open(tertiles_path) as tertiles, open(covid_19_path) as covid_19_data:
  covid_19_dict = json.loads(covid_19_data.read())
  tertiles_dict = json.loads(tertiles.read())

  covid_19_dict["records"].sort(key=compare_function)

  output_dict = {
      "tertiles": tertiles_dict,
      "records": covid_19_dict['records']
  }

  for entry in output_dict['records']:
    for data_point in entry['data']:
      del data_point['dateRep']
      del data_point['day']
      del data_point['month']
      del data_point['year']
      del data_point['popData2019']
      del data_point['continentExp']
      del data_point['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000']

  with open("../data/output/covid_19_output.json", "w") as output_file:
    json.dump(output_dict, output_file, indent=2)
