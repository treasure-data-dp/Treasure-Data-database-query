
import sys
import os
import tdclient
import argparse
import csv

#Get API key.
apikey = "3867/9fdb83baacfdee0fe976a0d2a8c6606067c982a3"

#Set up a parser.
parser = argparse.ArgumentParser(
    description='Treasure Data database query',
)

#Define parser arguments.
parser.add_argument('db_name', action="store")
parser.add_argument('table_name', action="store")
parser.add_argument('-c', action="store", dest="col_list")
parser.add_argument('-m', action="store", dest="min_time", type=int)
parser.add_argument('-M', action="store", dest="max_time", type=int)
parser.add_argument('-e', action="store", dest="engine")
parser.add_argument('-f', action="store", dest="format")
parser.add_argument('-l', action="store", dest="limit", type=int)

args = parser.parse_args()

#Create SQL statement.
q = "SELECT" 
if str(args.col_list) !="None":
    q+=(" " + args.col_list)
else: q+=(" *")
if args.table_name !="None":
    q+=(" FROM " + args.table_name)
#Check max_time greater than min_time.
if (str(args.min_time) !="None"):
    if (str(args.max_time) =="None"):
	q+=(" WHERE TIME > " + str(args.min_time))
if (str(args.max_time) !="None"):
    if (str(args.min_time) =="None"):
        q+=(" WHERE TIME < " + str(args.max_time))
if (str(args.min_time) !="None"):
    if (str(args.max_time) !="None"):
	if (args.max_time) > (args.min_time):
	    q+=(" WHERE TIME BETWEEN " + str(args.min_time) + " AND " + str(args.max_time))
	else: print("""
        Ooops - Min is greater than Max - ignoring Min/Max!!
                    """)
if str(args.limit) !="None":
    q+=(" LIMIT " + str(args.limit))

#Create q_td to avoid conflict with tdclinet query syntax.
q_td= q 


#print(parser.parse_args())


#Set file output format.
filename = "treasure_data.tsv"
if str(args.format) !="None":
    if str(args.format) == ('csv' or 'tsv'):
        filename = "treasure_data." + str(args.format)

#Run SQL.

def main():

    
    with tdclient.Client(apikey) as client:
        print("""
        Now processing this SQL query: """ + q_td)
        job = client.query(db_name = "sample_datasets", q = q_td)
        # sleep until job's finish
        job.wait()
        f = open(filename, "w")
        for row in job.result():
            row = str(row)           
            f.write(row)
        
   
if __name__ == "__main__":
    #Test validity of database name and table name. If not valid, print useful error message.
    #Otherwise, run SQL
    with tdclient.Client(apikey) as client:
            for db in client.databases():
                    if db.name == args.db_name:
                            for table in db.tables():
                                    if table.table_name == args.table_name:
                                        main()
                                        break                           
                                    else: print("""
                    Invalid database name and/or invalid table name! Please retry!""")
                    else: print("""
                    Invalid database name and/or invalid table name! Please retry!""")
                    break
    
    

