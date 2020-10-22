import pandas as pd

covid19_data_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"

covid19_json_file = pd.read_json("covid_19_worldwide.json", typ ="frame")

for key in covid19_json_file.records.to_dict():
    print(covid19_json_file.records.to_dict()[key]['dateRep'])

# print(covid19_json_file.records.to_dict())

