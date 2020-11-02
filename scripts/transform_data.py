import json
import os

print('Step 4: Transforming the data to make it easier to work with...')

# Change cwd to this file's dir, so we can use a relative path when saving the json:
this_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(this_dir)

# This script loads a json from opendata.ecdc.europra.eu
# and transforms it into a json file on the form:
# { date: "some date"
# 		countries: [
#   		list of countries with information
# 		]
# }
#
# The result json file is saved into the data folder inside the nuxt folder. 
# One can also run:
# node prettifyJson.js "../nuxt/data/covid_19_worldwide_correct_form.json"
#
# This will prettify the json file in javascript untill i've figured out how to do it in python.

# Helper function: Creates a list with all the unique dates in the dataset.
def get_unique_dates(covid_19_list):
    used_dates = []

    for entry in covid_19_list:
        date = entry['dateRep']
        if date not in used_dates:
            used_dates.append(date)
        
    return used_dates


# The file is opened from the url via the urllib library
with open("../data/temp/covid_19_vals_per_cap.json") as input_file:
    # The file contains a list "records" which holds the information
    covid_19_dict = json.loads(input_file.read())

    # An array for the finished data is created
    data_correct_form = []

    # I use my helper function to get an array of dates and run through them.
    for date in get_unique_dates(covid_19_dict['records']):
        # This is the form i want the data to be in, so i create the template dictionary
        date_dict = {'date': date, 'data': []}

        # I run through the entire dataset again, and gather all the data points with the corresponding data.
        # When found, the entire chunk of data is appended into the countries key in the dictionary.
        for entry in covid_19_dict['records']:
            if entry['dateRep'] == date:
                date_dict['data'].append(entry)

        # The entire dictionary is then appended to the list.
        data_correct_form.append(date_dict)

    covid_19_dict['records'] = data_correct_form

    # The end folder is located and the file inside is updated with the new information.
    with open('../data/temp/covid_19_transformed.json', 'w') as output_file:
        json.dump(covid_19_dict, output_file, indent=2)