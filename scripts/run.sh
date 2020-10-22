#!/bin/bash

# Authors: Mikkel Plesner Ottosen, Magnus Bendix Borregaard
# Cultural Data Science Semester Project

# Run this to execute all of the data processing steps (in order) needed to produce the data to visualize in the browser:

# Relative paths from the location of this script:
cd "${BASH_SOURCE%/*}"

# Order is important:
python get_input_data.py
python calc_max_values.py
python transform_data.py
python sort_and_filter_data.py
node prettifyJson.js '../output_data/covid_19_final.json'

echo 'All done'