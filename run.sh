#!/bin/bash

# Authors: Mikkel Plesner Ottosen, Magnus Bendix Borregaard
# Cultural Data Science Semester Project
# GitHub: https://github.com/NormalReedus/CDSExam

# Run this script to execute all of the data processing steps (in order) needed to produce the data that are visualized in the browser
# ------------------------------------------------------------------------------------------------------------------------------------


# Relative paths from the location of this script:
cd "${BASH_SOURCE%/*}"

# Runs all of the data processing:
jupyter nbconvert --to notebook --inplace --execute scripts/main.ipynb

echo 'Step 6: Transferring data to the visualizer...'
cp data/output/covid_19_final.json nuxt/data/covid_19_data.json

# echo 'Step 7: Getting the toolbox...'
cd nuxt && npm i

# echo 'Step 8: Running the visualizer...'
npm run dev