# async function getPSQLdata() {
#   const pg = require('pg');

#   var pgConfig = {
#     user: 'postgres',
#     password: '[MY PASSWORD]',
#     database: '[MY DB NAME]',
#     host: '[PUBLIC IP ADDRESS OF DB INSTANCE]'
#   };

#   var pgPool;

#   if (!pgPool) {
#     pgPool = new pg.Pool(pgConfig);
#   }

#   const scores = await pgPool
#     .query("SELECT * from table")
#     .then(res => console.log(res.rows[0]))
#     .catch(e => console.error(e.stack));
# }

# exports.dailyFill = async function main() {
#   await getPSQLdata();
# };

# # instance connection name
# bestmana:europe-west3:bestmana-test-database

# # database
# bestmana-test-database

# # A Service account with the Cloud SQL Client role
# best-mana123@bestmana.iam.gserviceaccount.com