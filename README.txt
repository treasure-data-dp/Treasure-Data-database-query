1. Python CLI script to run Treasure Data database query. 
	
2. Required installation: 
	Python 2.7, td-client.

3. Example without command line arguments: 
	python database_query_TD.py
	
	usage: TD_database_query.py [-h] [-c COL_LIST] [-m MIN_TIME] [-M MAX_TIME]
								[-e ENGINE] [-f FORMAT] [-l LIMIT]
								db_name table_name
	TD_database_query.py: error: too few arguments

4. Example of help menu (using -h, or --help option) Note the two positional/mandatory arguments (db_name, table_name):

	python database_query_TD.py -h

	usage: TD_database_query.py [-h] [-c COL_LIST] [-m MIN_TIME] [-M MAX_TIME]
								[-e ENGINE] [-f FORMAT] [-l LIMIT]
								db_name table_name

	Treasure Data databse query

	positional arguments:
	  db_name
	  table_name

	optional arguments:
	  -h, --help   show this help message and exit
	  -c COL_LIST
	  -m MIN_TIME
	  -M MAX_TIME
	  -e ENGINE
	  -f FORMAT
	  -l LIMIT

5. Examples:

	python database_query_TD.py sample_datasets www_access -c time -l 3 -f tsv
	
	python database_query_TD.py sample_datasets www_access -c time -l 2 -f tsv -m 1412382251 -M 1412382292
	
	python database_query_TD.py sample_datasets www_access -c time -l 4 -f tsv -m 1412382292  -M 1412382292
        Error:
			Ooops - Min is greater than Max - ignoring Min/Max!!
			Now processing this SQL query: SELECT time FROM www_access LIMIT 4
	
	python database_query_TD.py  sample_dataset www_access
		Error: 
			Invalid database name and/or invalid table name! Please retry!
		
		
	

6. Special cases:
	If MIN_TIME exceeds MAX_TIME, an error message is generated and program ignores both MIN_TIME and MAX_TIME:
		"Ooops - Min is greater than Max - ignoring Min/Max!!"
	
7. Issues:
	Note: Code supports query of all columns, or one column, but not multiple collumns.  Apologies, I ran out of time!!! If you need to see this, I can add it!!!
