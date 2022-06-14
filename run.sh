export PYTHONPATH=$PWD
export FLASK_APP=app
export FLASK_DEBUG=1
source env/bin/activate

docker-compose  -f docker-compose.yml up -d db admin

parallel -u ::: 'python -m flask run'
