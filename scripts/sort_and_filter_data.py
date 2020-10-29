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
max_value_path = "../data/temp/covid_19_max_vals.json"
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
with open(max_value_path) as max_values, open(covid_19_path) as covid_19_data:
    covid_19_dict = json.loads(covid_19_data.read())
    output_dict = json.loads(max_values.read())

    covid_19_dict["records"].sort(key=compare_function)

    output_dict['records'] = covid_19_dict["records"]

    with open("../data/output/covid_19_output.json", "w") as output_file:
        output_file.write(json.dumps(output_dict))
