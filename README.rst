csvfaker
========

Generate CSV files with fake data.


Usage
-----
.. code-block:: bash

    csvfaker [-h] [-f] [-r ROWS] [-l LOCALE] [-s SEED] [-n]
             [-p REPLACE_NEWLINE] [-d DELIMITER] [--version]
             [FAKE [FAKE ...]]

    positional arguments:
      FAKE                  The name of the fake(s) to use to generate output,
                            separated by space. Will also be used as column
                            headers. If omitted, the fakes 'name job state' will
                            be used.

    optional arguments:
      -f, --list-fakes      Show a list of all available fakes.
      -r ROWS, --rows ROWS  Number of rows to generate. If omitted it defaults to
                            10.
      -l LOCALE, --locale LOCALE
                            Locale to use. Examples: 'en_US', 'es'.
      -s SEED, --seed SEED  Seed to use. Generated result will be the same when
                            called with the same seed.
      -n, --no-headers-row  Do not output columns headers.
      -p REPLACE_NEWLINE, --replace-newline REPLACE_NEWLINE
                            Replace newline character with provided string.
      -d DELIMITER, --delimiter DELIMITER
                            Output column delimiter.


Examples
--------

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

Show a list of all available generator properties

    csvfaker --list-fakes


Installation
------------

    pip install csvfaker

or

    pip3 install csvfaker


Fake providers
--------------
This uses the Faker (https://github.com/joke2k/faker) package. For a list of all available generator properties (like ``name`` and ``address``) see the documentation: http://faker.readthedocs.io/en/master/providers.html 


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
