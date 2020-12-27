# COVID-19 Heatmap

Mikkel Plesner Ottosen & Magnus Bendix Borregaard

# Abstract.

The European Union collects and publishes data on the current numbers of COVID-19 cases and deaths every day for countries and areas around the world. It can, however, be difficult to determine whether a country is ‘doing well’ with just an overview of the absolute values for their daily COVID-19 cases or deaths, and not the values per capita. To illustrate this discrepancy, we have created a heatmap that (among other things) allows the changing between absolute values and the same variable per 10,000 inhabitants. The results of using the heatmap illustrate how the absolute number of COVID-19 cases and deaths for a given country or area can be misleading, since a higher population will most often have a higher number of cases and deaths.

**Keywords:** COVID-19, heatmap, European Union.

# Introduction

We live in the information age and the digital foundation that most societies are built on today allows for a rapid spread of data. This grants the opportunity to extract loads of useful and updated information about almost anything. Now add a global pandemic that spreads from one place to a vast amount of countries in a matter of months. The product is a demonstration of global data gathering and sharing as we have rarely seen before.

The motivation of this project stems from an urge to explore and make good use of this vast amount of data reporting on the covid-19 situation. We wanted to see if there was a new or unused angle to be used in order to see the data in a new light. As such, we came upon the idea of a heatmap. It is not that the heatmap-format has not been used before in similar cases, but it allows for many interesting ways of displaying correlations and points to be made within the data. We ended up exploring a way to show the distinct difference between visualizing data based on absolute numbers and ones created from a relation between two values as in our case: the relation between cases/deaths and population.

There is not necessarily anything new about that approach but with the help of a world map and vibrant colors, we truly believe that we have created a heatmap that allows for an intuitive way of exploring the covid-19-situation for each day and each country relative to one another and relative to the population of that particular country.

# Problem

During the COVID-19 pandemic, a lot of countries have been keeping records of the number of new COVID-19 cases and deaths per date, and in the public eye these numbers have been used as an indication as to how well any given country is doing in combating the virus. Especially the United States of America has been criticized in the media for handling the pandemic poorly by referencing the absolute amount of new cases and deaths per day, but are these absolute numbers appropriate for this purpose?

This project thus seeks to answer the question: Are the absolute numbers for new COVID-19 cases per day an accurate indication of how well / poorly a country is handling the COVID-19 pandemic, or is there a better metric for this?

# Software

The following is a quick overview of the technologies used in this project (version numbers are guaranteed to work, but the newest versions will in most cases work just the same):

- Python 3.8: Gets and processes the data
- Jupyter (nbconvert 5.6.1): Strings together the data processing scripts
- Node.js 14.14.0: Builds and runs the frontend visualizer
- NPM 6.14.8: Installs and manages dependencies for the frontend
- Nuxt (Vue 2): Builds the visualizer dashboard and manages visualizer state
- Git Bash 2.29.2: Strings together the data processing, dependency installation and running the visualizer
- A web browser: Displays the visualizer (please don’t use Internet Explorer)

# Data processing

All of the data processing steps necessary for generating a timeline visualization of the EU coronavirus dataset are present in [this Jupyter notebook](https://github.com/NormalReedus/CDSExam/blob/master/jupyter/data_processing.ipynb). The notebook includes small descriptions of all of the scripts as well as optional steps for saving and loading data from the scripts, so not all steps will have to be completed every time, if the output of the given scripts have already been saved.

An in-depth explanation of _how_ the individual scripts work can be found in the notebook.

## 0. Setup

This cell imports the required packages and changes the current working directory to the directory containing this notebook, so file paths will be easier to work with.

## 1. Get latest raw data from EU

This cell makes a GET request to [the EU open data portal](https://opendata.ecdc.europa.eu/covid19/casedistribution/json/) for the original dataset.

## 2. Calculate deaths and cases per 10k

This cell uses the original data to calculate the amount of cases and deaths per 10,000 inhabitants for any given record, using the fields `"cases"`, `"deaths"`, and `"popData2019"`.

## 3. Calculate global max values

This cell takes the output from step 2, and adds to it the highest\* number of `"cases"`, `"deaths"`, `"casesPer10k"`, and `"deathsPer10k"` of all time across all countries. These numbers are used in the legend and in the map to anchor the highest color value (red), when the visualizer is used to display values that are in relation to the highest values of all time.

\*These numbers are calculated by disregarding (only for the calculation of these numbers) the 3 countries that are the ‘worst offenders’ for any specific variable (cases, deaths etc.), because these countries tend to stretch the color scale immensely, resulting in a visualization that does not show nuances well. Removing these countries allows for more differences to be seen in the colors of countries with few and moderate amounts of cases / deaths / etc. while every country above the top 4 amount for a date will be displayed as the maximum red color.

## 4. Transform data into a better format for the visualizer

The primary responsibility for this cell is to take the data produced by step 2 (a flat array of dates and countries) and convert it into a two-dimensional array, where every country’s records are categorized into another array representing a date.

This allows for the visualizer to easily index every record by date, which is extremely useful when producing a timeline that displays the data for all countries for only one date at a time.

## 5. Calculate local max values

This cell takes the transformed output of step 4, and calculates the max values for the same 4 variables as in step 3 for every date. These max values are used to anchor the highest color value (red) for any single date in both the legend and map, but does not disregard any countries, since the color scale for any single date is mostly much more compact than the scale from zero to the global max values.

## 6. Sort and filter data

This cell combines the output from step 3 and 5 into a single JSON, deletes all of the unused properties (left over from the original dataset) and sorts all of the dates from earliest to latest. In the end, the output is saved as `/data/output/covid_19_final.json`. The format of the output data can be seen viewed in the 'Metadata' section.

# Visualizer

The code for the frontend visualizer is available [here](https://github.com/NormalReedus/CDSExam/tree/master/nuxt). The frontend consists of a simple dashboard and a custom SVG world map. The visualizer is made with Nuxt / Vue (HTML, CSS, JavaScript). Only aesthetics are handled by the frontend.

## World map

The world map SVG is used to display the EU data as a heatmap by manipulating the styling of the individual areas (specifically the color) through the DOM. Binding together the data points and the DOM element representing the area in the map is done through matching `"geoId"`s.

The map has only been edited for two subtle purposes.

1. Errors in matching `"geoId"`s
2. Browser support for displaying ‘title’ (name of the geographic area) when hovering over an area.

### Matching IDs

The actual United Kingdom was labelled as GB in the SVGs `"geoId"`, and Greece was labelled with the Greek initials for Ellas (‘EL’). To match the dataset, these were simply converted manually in the SVG source code (one location each) to ‘UK’ and ‘GR’ respectively.

### Titles

The SVG source code specified the ‘title’ of areas as a property on the DOM element (SVG path) instead of specifying the title as a child (`<title>`) element of the SVG path. Hovering will not in most (all?) browsers display the human readable name of the geographic area as well as the area’s value for the given date when this is the case.

To correct this, we used the Visual Studio Code editor to search and replace every instance of this. The matching regex was the following: `title="(.+)"\n\s+(id=".+")\n\s+/>`. Replacing the matches with the following expression: `$2><title>$1</title></path>`. `$2` represents the ID of the element, since this varies from element to element, and `$1` represents the title value, since this also varies.

## Features

Interactive elements are marked as **bold**.

The visualizer will display the number of new **cases**, **deaths**, **cases per 10,000 inhabitants**, or **deaths per 10,000 inhabitants** for a specified date on the map with a color, that represents where this value lands in relation to either the highest value for the variable for that **specific date**, or the highest value for the variable of **all time**.

The legend will indicate the corresponding value for any color, but the specific numbers can be seen by **hovering** over a geographic area on the map. The areas with no data are marked with a specific color, as well as the countries that have the selected variable value of zero, since we feel the need to distinguish this from ‘very few’ cases / deaths.

The **‘Go to max’ button** will take you to the date of the highest value of all time for your selected variable and display the geographical area and value in a small window.

A specific date can be selected by **scrolling on the timeline slider** at the bottom of the dashboard, but you can also set the map to automatically scroll through time in two different speeds with the **‘Timeline speed’** controls.

There are two different **color modes** and an option to **turn off animations**, if these are taxing on your computer.

# Recreation of results

## Prerequisites

1. Install Git from [their website](https://git-scm.com/downloads). This will include a GNU Bash distribution, which will not need to be installed separately.
2. Install the latest version of Anaconda from [their website](https://www.anaconda.com/). This will include Jupyter and Python, which will not need to be installed separately. If needed, Anaconda can be used to install the correct versions of Python and Jupyter.
3. Install Node.js from [their website](https://nodejs.org/en/). This will include Node Package Manager, which will not need to be installed separately.
   - Be aware that during installation you will need to check a box to install additional build tools for all the dependencies to work.

## Setup

To use this project, you have three options, depending on what you wish to do.

### Demo

There are no prerequisites for this option. To see what the visualizer is capable of, you can access a live demo on [this website](https://covid-heatmap.netlify.app/). The demo includes the interactive visualizer, but not the data processing steps, and as such, the latest data will be from the date on which the site was last updated.

### Running everything at once

This option will require you to complete every step in 'Prerequisites'. Run the [file](https://github.com/NormalReedus/CDSExam/blob/master/run.sh) `/run.sh` (in the root folder of the project) with Bash by double clicking the file _or_ opening Git Bash, navigating to the project folder, and running the command: `./run.sh`.

The process will take a while, since it will complete the following tasks:

1. Fetch the latest covid-data from the EU Data Portal
2. Process the data
3. Save input, intermediary, and output data
4. Copy data to the visualizer
5. Install dependencies for the visualizer
6. Run the visualizer in you default browser

**Be aware** that step 1 will take 10+ minutes on the Aarhus University network because of throttling, and should be done somewhere else. If the data from this step has already been saved, you can skip this step by following the guide in 'Running scripts individually'.

### Running scripts individually

For this option, you will only need to complete step 2 and 3 in 'Prerequisites', since Bash is not used when running scripts manually.

#### Processing data

To run all of the data fetching and data processing steps, you will navigate into the `/jupyter` directory and open `data_processing.ipynb` as a Jupyter notebook, running on a Python 3 kernel.

In the notebook, you will always have to run the cell labelled `0. Setup`, but any other cells can be omitted, if the required input for the cell has already been saved to a file, using the `Optional - Save {step number}` and `Optional - Load {step number}` cells. A cell’s required files can be identified by looking at the loading step cell description which will always be in the cell immediately before the given data processing step.

When step `6. Sort and filter data` has been completed, you will have to copy the final output file `/data/output/covid_19_final.json` into `/nuxt/data/covid_19_data.json`. Note the file name change.

#### Running the visualizer

When the latest data has been copied to the visualizer, you will have to install the visualizer dependencies with your preferred terminal. This can be done by either opening your terminal and navigating into the project folder followed by the command `cd nuxt` to navigate into the visualizer subdirectory, or by opening the terminal directly inside `/nuxt`. With the terminal window open, run the command `npm i` to install the visualizer’s dependencies. This process will take a short while.

Running the visualizer locally in your default browser is now as simple as running the command `npm run dev`. **Be aware** that the visualizer will not work, if you did not install the additional build tools during step 3 of 'Prerequisites'.

## Analysis

To see the discrepancy between the use of absolute numbers for the COVID-19 data and numbers per 10,000 inhabitants, you can use the interface to do the following:

1. Make sure you have selected ‘Single date’ for the Legend limits and ‘Cases’ as the variable to display.
2. Scroll the timeline to the 21st of November 2020.
3. Notice how the United States of America has the highest absolute amount of new COVID-19 cases for the selected date (~200,000), denoted by the completely red color of the area on the map. Notice how Georgia has around 7500 new cases for the same date.
4. Change the displayed variable from ‘Cases’ to ‘Cases per 10k.’ without selecting a new date.
5. Notice how Georgia is now the reddest area on the map with ~19 new COVID-19 cases per 10,000 inhabitants, whereas the United States of America only has around 6 new cases per 10,000 inhabitants.

# Evaluation

Given the fact, that the underlying EU dataset does not seem to always be completely correct and given that an area can be either a separate area on the map or an integrated part of the country, that it belongs to, we would not be comfortable using this tool to analyze the specific situation in an area at a specific point in time. For example: Is it accurate to say that Crete is a part of Greece, when the fact that Crete is an island has a big effect on the prevalence of COVID-19?

We do, however, feel that the COVID-19 heatmap software developed for this project has features that allow for a great overview of the global COVID-19 situation which makes it easy to explore different ways of analysing the EU dataset and doing meta-analysis of the data, for example, on the differences between the absolute numbers for cases and deaths versus the same variables normalized by the amount of inhabitants for a given country or area, since the visualization can still be used to distinguish between the effects of different ways of looking at the data.

# Conclusion

The results of our analysis illustrate how the absolute number of COVID-19 cases and deaths for a given country or area can be misleading, since a higher population will most often have a higher number of cases and deaths, but these can be somewhat normalized by simply dividing the numbers by the number of inhabitants for the country or area. This is not to say that the best metric for how well / poorly a country is doing in terms of handling the COVID-19 pandemic is the amount of cases or deaths per capita, but the results certainly illustrate that the absolute numbers by themselves do not convey this information very well.

# Disclaimer

This project was made as a technical demo, and we do not in any way claim that the data are correct or without omissions et cetera. For example, the amount of deaths in the US on the 16th of April 2020 seems to be the accumulated value for two days - we have not edited any of these numbers from the original data.

Lastly, this visualization was made for a desktop experience, and will work - but poorly - on a mobile device.

# Metadata

## Source data

The source data consists of a flat array of records, the only props of which that are used in this project, and that are not also explicitly documented in 'Output data' are the following:

<table>
  <tr>
   <td><strong>Property</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>dateRep
   </td>
   <td>string
   </td>
   <td>A representation of the date of the given record in the DD/MM/YYYY-format.
   </td>
  </tr>
  <tr>
   <td>popData2019
   </td>
   <td>integer
   </td>
   <td>The population number of the given geographical area in 2019.
   </td>
  </tr>
</table>

## Output data

`"maxVals"` (global)

<table>
  <tr>
   <td><strong>Property</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>cases
   </td>
   <td>integer
   </td>
   <td>The highest number of new covid-19 cases for any geographic area and date*.
   </td>
  </tr>
  <tr>
   <td>deaths
   </td>
   <td>integer
   </td>
   <td>The highest number of new covid-19 deaths for any geographic area and date*.
   </td>
  </tr>
  <tr>
   <td>casesPer10k
   </td>
   <td>float
   </td>
   <td>The highest number of new covid-19 cases per 10,000 inhabitants for any geographic area and date*.
   </td>
  </tr>
  <tr>
   <td>deathsPer10k
   </td>
   <td>float
   </td>
   <td>The highest number of new covid-19 deaths per 10,000 inhabitants for any geographic area and date*.
   </td>
  </tr>
</table>

\*With the top 3 geographic areas disregarded, as described in '3. Calculate global max values'.

`"records"`

The records property is an array of objects in the following format:

<table>
  <tr>
   <td><strong>Property</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>date
   </td>
   <td>string
   </td>
   <td>A representation of the date of the given record in the DD/MM/YYYY-format.
   </td>
  </tr>
  <tr>
   <td>data
   </td>
   <td>data[]
   </td>
   <td>The covid-19 data and area data for every geographic area for the given date.
   </td>
  </tr>
  <tr>
   <td>maxVals (local)
   </td>
   <td>object
   </td>
   <td>The maximum values for the four visualizer variables for the given date
   </td>
  </tr>
</table>

`"data"`

<table>
  <tr>
   <td>

<strong>Property</strong>

   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>cases
   </td>
   <td>integer
   </td>
   <td>The number of new covid-19 cases for the given geographic area and date.
   </td>
  </tr>
  <tr>
   <td>deaths
   </td>
   <td>integer
   </td>
   <td>The number of new covid-19 deaths for the given geographic area and date.
   </td>
  </tr>
  <tr>
   <td>countriesAndTerritories
   </td>
   <td>string
   </td>
   <td>The human-readable name of the geographic area.
   </td>
  </tr>
  <tr>
   <td>geoId
   </td>
   <td>string
   </td>
   <td>A 2-letter ID representing the geographic area. Corresponds to the ID in the geographic areas in the visualizer.
   </td>
  </tr>
  <tr>
   <td>deathsPer10k
   </td>
   <td>float
   </td>
   <td>The number of new covid-19 deaths per 10,000 inhabitants for the given geographic area and date.
   </td>
  </tr>
  <tr>
   <td>casesPer10k
   </td>
   <td>float
   </td>
   <td>The number of new covid-19 cases per 10,000 inhabitants for the given geographic area and date.
   </td>
  </tr>
</table>

`"maxVals"` (local)

<table>
  <tr>
   <td><strong>Property</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>cases
   </td>
   <td>integer
   </td>
   <td>The highest number of new covid-19 cases for any geographic area on the specific date.
   </td>
  </tr>
  <tr>
   <td>deaths
   </td>
   <td>integer
   </td>
   <td>The highest number of new covid-19 deaths for any geographic area on the specific date.
   </td>
  </tr>
  <tr>
   <td>casesPer10k
   </td>
   <td>float
   </td>
   <td>The highest number of new covid-19 cases per 10,000 inhabitants for any geographic area on the specific date.
   </td>
  </tr>
  <tr>
   <td>deathsPer10k
   </td>
   <td>float
   </td>
   <td>The highest number of new covid-19 deaths per 10,000 inhabitants for any geographic area on the specific date.
   </td>
  </tr>
</table>

# Contact

**Github repository:** [https://github.com/NormalReedus/CDSExam](https://github.com/NormalReedus/CDSExam)

**E-mail:** magnus.borregaard@gmail.com

# License

## World map

The world map [SVG file](https://mapsvg.com/static/maps/geo-calibrated/world.svg) from [mapSVG.com](https://mapsvg.com/) is subject to the [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license, which can be found [here](https://github.com/NormalReedus/CDSExam/blob/master/nuxt/components/MAP_LICENSE.md). The source code for a modified version of this map is used inside the visualizer of this project.

## Data

The source data in `/data/input` and our modified data in `/data/output` are both subject to the [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license that can be found [here](https://github.com/NormalReedus/CDSExam/blob/master/data/DATA_LICENSE.md).

[The ECDC copyright notice](https://www.ecdc.europa.eu/en/copyright) applies to the source data and our derived dataset as well, and can be found [here](https://github.com/NormalReedus/CDSExam/blob/master/data/COPYRIGHT.md).

The source data (DOI 10.2906/101099100099/1) by the [ECDC](https://www.ecdc.europa.eu/en) is available at: [https://opendata.ecdc.europa.eu/covid19/casedistribution/json/](https://opendata.ecdc.europa.eu/covid19/casedistribution/json/).

## Software

The MIT software license can be found [here](https://github.com/NormalReedus/CDSExam/blob/master/LICENSE), and covers only the software, that is: everything but the data inside the `/data` directory of this project and the world map SVG inside `/nuxt/components/WorldSvg.vue`.
