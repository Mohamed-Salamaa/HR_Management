
DB_SERVER=localhost
DB_PORT=5432
DB_USER=salama
DB=HR_db
DB_PASS=salama


FILE_NAME=db.dump


touch ~/.pgpass
echo "${DB_SERVER}:${DB_PORT}:*:${DB_USER}:${DB_PASS}" >> ~/.pgpass
chmod 0600 ~/.pgpass

echo "Dropping ${DB} DB.."
dropdb -h ${DB_SERVER} -p ${DB_PORT} -U ${DB_USER} -w ${DB}

echo "Recreating ${DB} DB.."
createdb -h ${DB_SERVER} -p ${DB_PORT} -U ${DB_USER} -O ${DB_USER} -w  ${DB}

echo "Restoring ${DB} DB.."
pg_restore -h ${DB_SERVER} -p ${DB_PORT} -U ${DB_USER} -d ${DB} ${FILE_NAME}
