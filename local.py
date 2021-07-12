# This gist contains a direct connection to a local PostgreSQL database
# called "suppliers" where the username and password parameters are "postgres"

# This code is adapted from the tutorial hosted below:
# http://www.postgresqltutorial.com/postgresql-python/connect/

import psycopg2

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
conn = psycopg2.connect(host="34.89.196.152", port = 5432, database="postgres", user="postgres", password="liav100")

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""select to_json(array_agg( row_to_json(t)))
from (
   select restaurant_isn,distance_in_meters,show_order 
   from public.search_results 
   WHERE user_id_or_email != '' ) t""")
query_results = cur.fetchall()
print(query_results)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()



def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'
