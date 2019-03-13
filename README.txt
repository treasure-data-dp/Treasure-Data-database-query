1. Python CLI script to run Treasure Data database query.

2. Required installation: 
	Python 2.7, td-client.

3. Example without command line arguments:
	usage: TD_database_query.py [-h] [-c COL_LIST] [-m MIN_TIME] [-M MAX_TIME]
								[-e ENGINE] [-f FORMAT] [-l LIMIT]
								db_name table_name
	TD_database_query.py: error: too few arguments

4. Example of help menu (using -h, or --help option) Note the two positional/mandatory arguments (db_name, table_name):

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


 5. Special cases:
	If MIN_TIME exceeds MAX_TIME, an error message is generated and program ignores both MIN_TIME and MAX_TIME:
		"Ooops - Min is greater than Max - ignoring Min/Max!!"
	