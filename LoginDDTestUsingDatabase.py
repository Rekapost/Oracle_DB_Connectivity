import time
from selenium import webdriver
import cx_Oracle
import os   # module
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
os.environ['PATH']='C://Users//Reka//WINDOWS.X64_213000_db_home//instantclient_21_7' # method  specify environment variable
serv_object = Service("C://Users//Reka//Drivers//chromedriver.exe")
driver = webdriver.Chrome(service=serv_object)
driver.get("http://newtours.demoaut.com")
driver.maximize_window()
con=cx_Oracle.connect("RekaNV","admin","localhost/pdborcl")     # establish connection  to database
cur=con.cursor()  #   object for cursor to execute queries  (temp area from where we have to execute queries)
query="select * from users"
cur.execute(query)
# to read data from cur and print
for cols in cur:    # column
    driver.find_element(By.NAME,"userName").send_keys(cols[0])
    driver.find_element(By.NAME,"password").send_keys(cols[1])
    driver.find_element(By.NAME,"login").click()
    time.sleep(5)
    # validation started
    if driver.title=="Find a Flight:Mercury Tours:":
        print("test passed")
    else:
        print("test failed")
    driver.find_element(By.LINKTEXT,"Home").click() # go to login page and for second set of username and pwd

cur.close()
con.close()
print("completed")