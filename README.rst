# Python Aircloak Tools

A small package for querying an Aircloak service via the postgres api. 

The main aim is to provide an Aircloak-friendly wrapper around `psycopg2`, and in particular to
provide clear error messages when something doesn't go as planned. 

Query results are return as `pandas` dataframes. 
