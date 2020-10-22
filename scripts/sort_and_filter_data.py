import json
import os

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

max_value_path = "../temporary_data/covid_19_max_values.json"
covid_19_path = "../temporary_data/covid_19_transformed.json"

def compare_function(e):
    
    return int(year + month + day)
 
# with open(max_value_path) as max_values, open(covid_19_data) as covid_19_data:
with open(covid_19_path) as covid_19_data:
    covid_19_dict = json.loads(covid_19_data.read())

    covid_19_dict["records"].sort(key=compare_function)

    with open("../output_data/covid_19_final.json", "w") as output:
        output.write(json.dumps(covid_19_dict))


