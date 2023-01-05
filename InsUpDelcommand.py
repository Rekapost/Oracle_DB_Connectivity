# INSERT , UPDATE , DELETE
import cx_Oracle
import os   # module
os.environ['PATH']='C:\\Users\\Reka\\instantclient_21_7'   # method  specify environment variable
con=cx_Oracle.connect("hr","hr","localhost/pdborcl")     # establish connection  to database
cur=con.cursor()  # object for cursor to execute queries (temp area from where we have to execute queries)
query1="update student set sname='xyz' where sid=102"
query2="delete student where sid=102"
cur.execute('select * from student')
cur.execute("insert into student values (102,'smith')")
cur.execute(query1)
cur.execute(query2)
cur.close()
con.commit()
con.close()
print("completed")
