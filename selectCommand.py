import cx_Oracle
import os   # module
os.environ['PATH']='C:\\Users\\Reka\\instantclient_21_7'   # method  specify environment variable
con=cx_Oracle.connect("hr","hr","localhost/pdborcl")     # establish connection  to database
cur=con.cursor()  #   object for cursor to execute queries  (temp area from where we have to execute queries)
query1="select * from employees"
cur.execute(query1)   # data is stored in cur
# to read data from cur and print
for cols in cur:    # column
    print(cols[0]),"   ",cols[1],"    ",cols[2]
cur.close()
con.close()
print("completed")