# This file contains all the code used in the codelab. 
# import sqlalchemy
# from flask import escape

# Depending on which database you are using, you'll set some variables differently. 
# In this code we are inserting only one field with one value. 
# Feel free to change the insert statement as needed for your own table's requirements.

# Uncomment and set the following variables depending on your specific instance and database:
# connection_name = "bestmana:europe-west3:bestmana-test-database"
# table_name = "reference.colors"
# table_field = "color"
# table_field_value = "green"
# db_name = "bestmana-test-database"
# db_user = "liav"
# db_password = "liav123456"

# If your database is MySQL, uncomment the following two lines:
#driver_name = 'mysql+pymysql'
#query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If your database is PostgreSQL, uncomment the following two lines:
# driver_name = 'postgres+pg8000'
# query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.





# def insert(request):
#     print ('123')
#     request_json = request.get_json()
#     stmt = sqlalchemy.text('insert into {} ({}) values ("{}")'.format(table_name, table_field, table_field_value))
    
#     db = sqlalchemy.create_engine(
#       sqlalchemy.engine.url.URL(
#         drivername=driver_name,
#         username=db_user,
#         password=db_password,
#         database=db_name,
#         query=query_string,
#       ),
#       pool_size=5,
#       max_overflow=2,
#       pool_timeout=30,
#       pool_recycle=1800
#     )
#     try:
#         with db.connect() as conn:
#             conn.execute(stmt)
#     except Exception as e:
#         return 'Error: {}'.format(str(e))
#     return 'ok'

    # functions_framework --target=func1.py
    # Get-ChildItem -Path Env:\
    # $env:GOOGLE_APPLICATION_CREDENTIALS="/keys/bestmana-918df5d819f3.json"
    # $env:DB_HOST="127.0.0.1:5432"
    # $env:DB_USER="liav"
    # $env:DB_PASS="liav123456"
    # $env:DB_NAME="bestmana-test-database"

    # Start-Process -filepath "C:\Users\E-ncrease\cloud_sql_proxy.exe" -ArgumentList "-instances=bestmana:europe-west3:bestmana-test-database=tcp:5432 -credential_file=/keys/bestmana-918df5d819f3.json"