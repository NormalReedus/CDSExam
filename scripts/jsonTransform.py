import json
import urllib.request

def get_unique_dates(covid19_dict):
    used_dates = []

    for entry in covid19_dict:
        date = entry['dateRep']
        if date not in used_dates:
            used_dates.append(date)
        
    return used_dates

covid19_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"

with urllib.request.urlopen(covid19_data_url) as covid_19_json:
    covid19_dict = json.loads(covid_19_json.read())['records']
    data_correct_form = []

    for date in get_unique_dates(covid19_dict):
        date_dict = {'date': date, 'countries': []}

        for entry in covid19_dict:
            if entry['dateRep'] == date:
                date_dict['countries'].append(entry)

        data_correct_form.append(date_dict)
    
    data_correct_form_json = json.dumps(data_correct_form)

    with open('../nuxt/data/covid_19_worldwide_correct_form.json', 'w') as endpoint:
        endpoint.write(data_correct_form_json)


