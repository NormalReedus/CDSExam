import json
import os

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

max_value_path = "../temporary_data/covid_19_max_values.json"
covid_19_data = "../temporary_data/covid_19_transformed.json"

with open(max_value_path) as max_values, open(covid_19_data) as covid_19_data:
    

