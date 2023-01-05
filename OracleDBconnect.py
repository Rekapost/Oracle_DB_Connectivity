import cx_Oracle
import os   # module
os.environ['PATH']='C:\\Users\\Reka\\instantclient_21_7'   # method  specify environment variable
# oracle instant client is configured in environment variable , and use that path  in script/code
# establish connection to Database
con=cx_Oracle.connect("hr","hr","localhost/pdborcl")# con = connection,server username ,password, server name and id
print("connected")
con.close()