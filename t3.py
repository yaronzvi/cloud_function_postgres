
# This file contains all the code used in the codelab. 
import sqlalchemy

# Depending on which database you are using, you'll set some variables differently. 
# In this code we are inserting only one field with one value. 
# Feel free to change the insert statement as needed for your own table's requirements.

# Uncomment and set the following variables depending on your specific instance and database:
connection_name = "bestmana:europe-west3:bestmana-test-database"
table_name = "public.search_results"
table_fields = "restaurant_isn,distance_in_meters,show_order"
table_where = "user_id_or_email = 'test'"
db_name = "bestmana-test-database"
db_user = "postgres"
db_password = "liav100"

# If your database is PostgreSQL, uncomment the following two lines:
driver_name = 'postgres+pg8000'
query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

def insert():
    stmt = sqlalchemy.text("select restaurant_isn,distance_in_meters,show_order from public.search_results t WHERE user_id_or_email = 'test'")
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    try:
        with db.connect() as conn:
           result_json = conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return result_json