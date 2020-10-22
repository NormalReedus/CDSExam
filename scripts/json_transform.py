import json

#This script loads a json from opendata.ecdc.europra.eu
#and transforms it into a json file on the form:
#{date: "some date"
# countries: [
#   list of countries with information
# ]}
#
#The result json file is saved into the data folder inside the nuxt folder. 
#One can also run:
#node prettifyJson.js "../nuxt/data/covid_19_worldwide_correct_form.json"
#
#This will prettify the json file in javascript untill i've figured out how to do it in python.

#Helper function: Creates a list with all the unique dates in the dataset.
def get_unique_dates(covid19_list):
    used_dates = []

    for entry in covid19_list:
        date = entry['dateRep']
        if date not in used_dates:
            used_dates.append(date)
        
    return used_dates

def get_max_deaths_and_cases(covid19_list):
    deaths = [entry['deaths'] for entry in covid19_list]
    cases = [entry['cases'] for entry in covid19_list]

    return (max(deaths), max(cases))

#The url from which the json is downloaded
covid19_data_path = "../input_data/covid_19_records.json"

#The file is opened from the url via the urllib library
with covid_data_path as covid_19_json:
    #The file contains a list "records" which holds the information
    covid19_list = json.loads(covid_19_json.read())

    #An array for the finished data is created
    data_correct_form = []

    #I use my helper function to get an array of dates and run through them.
    for date in get_unique_dates(covid19_list):
        #This is the form i want the data to be in, so i create the template dictionary
        date_dict = {'date': date, 'records': []}

        #I run through the entire dataset again, and gather all the data points with the corresponding data.
        #When found, the entire chunk of data is appended into the countries key in the dictionary.
        for entry in covid19_list:
            if entry['dateRep'] == date:
                date_dict['records'].append(entry)

        #The entire dictionary is then appended to the list.
        data_correct_form.append(date_dict)
    
    #The new data list is transformed into json format.
    data_correct_form_json = json.dumps(data_correct_form)

    # The end folder is located and the file inside is updated with the new information.
    with open('../output_data/covid_19_correct.json', 'w') as output:
        output.write(data_correct_form_json)




