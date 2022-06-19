export PYTHONPATH=$PWD
# export $(xargs < database.conf)
export FLASK_APP=app
export FLASK_DEBUG=1
source env/bin/activate

docker-compose  -f docker-compose.yml up -d database admin

parallel -u ::: 'python -m flask run --host=0.0.0.0'
