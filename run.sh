#!/bin/bash

# Authors: Mikkel Plesner Ottosen, Magnus Bendix Borregaard
# Cultural Data Science Semester Project

# Run this to execute all of the data processing steps (in order) needed to produce the data to visualize in the browser:

# Relative paths from the location of this script:
cd "${BASH_SOURCE%/*}"

# Order is important:
python scripts/get_raw_data.py
python scripts/calc_vals_per_cap.py
python scripts/calc_max_values.py
python scripts/transform_data.py
python scripts/sort_and_filter_data.py

echo 'Step 7: Transferring data to the visualizer...'
cp data/output/covid_19_output.json nuxt/data/covid_19_output.json

echo 'Step 8: Getting the toolbox...'
cd nuxt && npm i

echo 'Step 9: Running the visualizer...'
npm run build && npm run start

