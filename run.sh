#!/bin/bash

# Authors: Mikkel Plesner Ottosen, Magnus Bendix Borregaard
# Cultural Data Science Semester Project
# GitHub: https://github.com/NormalReedus/CDSExam

# Run this script to execute all of the data processing steps (in order) needed to produce the data that are visualized in the browser
# ------------------------------------------------------------------------------------------------------------------------------------

echo -e 'Fetching data, processing data, installing dependencies, and running the visualizer.\n\e[32mThis might take a while...\e[39m\n\n'

# Relative paths from the location of this script:
cd "${BASH_SOURCE%/*}"

# Runs all of the data processing:
jupyter nbconvert --to notebook --inplace --execute scripts/data_processing.ipynb

# Copies the output of data processing into the visualizer's directory:
cp data/output/covid_19_final.json nuxt/data/covid_19_data.json

# Installs the visualizer's dependencies
cd nuxt && npm i

# Opens the visualizer in your default browser:
npm run dev