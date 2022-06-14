# HR_Management 


## Running the project
The Project Controlled by the following scripts:

1. `bash setup.sh` a shell script to prepare the enviroment and install packages.
2. `source env/bin/activate` a shell script to activate the enviroment.
3. `bash clone-db.sh` a shell script restore th db.
4. `flask db upgrade` to apply changes to Database.
5. `flask run` to run the API.


## command to export dump file
pg_dump -Fc -h localhost -p 5432 -U salama HR_db > path
