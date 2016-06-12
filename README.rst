csvfaker
========

Generate a CSV file with fake data.


Usage
-----

Generate a CSV file with 100 names

    csvfaker --rows 100 name > names.csv

Generate 100 rows of first names, last names and job titles

    csvfaker -r 100 first_name last_name job

Generate 100 rows of first names and last names in Spanish

    csvfaker -r100 --locale=es first_name last_name

Generate 100 cities of Spain

    csvfaker -r100 --locale=es_ES city

Generate 100 Russian names

    csvfaker -r100 -l ru name

Generate 100 rows of latitudes and longitudes. Do not output headers row

    csvfaker -r 100 --no-headers latitude longitude

Generate 100 rows of names and addresses. Replace generated newline characters with a comma and space

    csvfaker -r 100 name address --replace-newline=', '

Show a list of all available fakes

    csvfaker --list-fakes


Installation
------------

    pip install csvfaker



Author
------

    Copyright 2016 Pere Orga

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.