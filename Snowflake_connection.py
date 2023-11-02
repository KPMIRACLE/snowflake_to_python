#This code is connect snowflake to native Python for basic operations
import snowflake.connector as SF
connection = SF.connect(user ='Kiranmiracle7',
                        password = 'Thankyou@2023',
                        account = 'cqyemzs-nd52009')
connection.Cursor().execute("CREATE OR REPLACE DATABASE TRANSFORMATIONS_DEV_DB")
connection.Cursor().execute("CREATE OR REPLACE SCHEMA TRANSFORMATIONS_DEV_SC")
connection.Cursor().execute("CREATE OR REPLACE TABLE EMPLOYEE(E_ID INTERGER, E_NAME VARCHAR, E_COMPANY VARCHAR, E_ROLE VARCHAR)")
connection.close()
