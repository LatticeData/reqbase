# Lattice Job Search Python Client

The comprehensive job search API, powered by Indeed, Simply Hired, Lawjobs, Monster, Linkedin, StackOverflow, Xing, Glassdoor, Dice, Careerjet and, Craigslist.

## Contents

  - [Overview](#Overview)
  - [Setup](#Setup)
    - [Installation](#Installation)
    - [API Authentication](#API-Authentication)
    - [Dependencies](#Dependencies)
  - [License](#license)
  - [Usage](#Usage)
    - [Function: lawjobs](#function-lawjobs)
    - [Function: indeed](#function-indeed)
    - [Function: simplehired](#function-simplehired)
    - [Function: craigslist](#function-craigslist)
    - [Function: craigslist_regions](#function-craigslist_regions)
    - [Function: careerjet](#function-careerjet)
    - [Function: dice](#function-dice)
    - [Function: xing](#function-xing)
    - [Function: stackoverflow](#function-stackoverflow)
    - [Function: ziprecruiter](#function-ziprecruiter)
    - [Function: monster](#function-monster)
    - [Function: linkedin](#function-linkedin)
## Overview

## Setup

### Installation
The easiest way to install this package is using pip:
```bash
pip install lattice-stocks-data
```
### API Authentication
To successfully use this library you will need an API key for the [Lattice Stock Market Data API](https://rapidapi.com/lattice-data-lattice-data-default/api/job-search4/) that powers it. Navigate to [RapidAPI](https://rapidapi.com/lattice-data-lattice-data-default/api/job-search4/) to sign up for a free API key and then save it to an environment variable called `STOCK_DATA_X_RAPID_API_KEY` in your environment. The library will automatically load that environment variable and use it to authenticate API calls made under the hood.

### Dependencies
This library relies on the following Python libraries:
 - numpy
 - python-dotenv
 - lxml
 - xmltodict
 - pytest
 - requests
 - cachetools
 - pymongo
 - pandas

These are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

## License

`lattice-stocks-data` is licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Usage
### Function: `lawjobs`
Conducts a comprehensive search of jobs posted on Lawjobs.com based on a free text search query.
```bash
lawjobs(query)
```
#### Arguments:
Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`

#### Return value:
Returns the list of jobs available.
#### Example:
```bash

```
### Function: `indeed`
Conducts a comprehensive search of jobs posted in Indeed based on a text query.
```bash
indeed(query)
```
#### Arguments:
Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`

#### Return value:
Returns the list of jobs available.
#### Example:
```bash

```
### Function: `simplehired`
Search for job postings on SimplyHired based on a text query.
```bash
simplehired(query)
```
#### Arguments:
Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`

#### Return value:
Returns the list of jobs available.
#### Example:
```bash

```
### Function: `craigslist`
Search for jobs postings on Craigslist based on a text query.
```bash
craigslist(query,region_id)
```
#### Arguments:
Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`
`region_id` | `str` | Job Location | `False`

#### Return value:
Returns the list of jobs available.
#### Example:
```bash

```
### Function: `craigslist_regions()`
```bash
craigslist_regions()
```
#### Arguments:
None

#### Return value:
Returns the list of regions available in craigslist.
#### Example:
```bash

```
### Function: `lawjobs`
```bash
lawjobs(query)
```
#### Arguments:
Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`

#### Return value:
Returns the list of jobs available.
#### Example:
```bash

```
### Function: `lawjobs`
```bash
lawjobs(query)
```
#### Arguments:
Name | Type | Description | Optional | Default Value
--- | --- | --- | --- |---
`query` | `str` | Job Category | `False`

#### Return value:
Returns the list of jobs available.
#### Example:
```bash

```


