
import os
from flask import Flask
import sqlalchemy
from sqlalchemy import func

app = Flask(__name__)

connection_name = "bestmana:europe-west3:bestmana-test-database"
db_name = "bestmana-test-database"
db_user = "liav"
db_password = "liav123456"

# If your database is PostgreSQL, uncomment the following two lines:
driver_name = 'postgres+pg8000'
query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})


@app.route('/', methods=['GET'])    
def get():
     
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
            json_results = conn.session.query(func.public.get_best_mana('test')).all()
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return {json_results}

    return Response(
        status=200,
        response="restaurants successfully returned"
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)