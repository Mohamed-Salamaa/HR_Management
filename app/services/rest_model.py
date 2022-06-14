from sqlalchemy.inspection import inspect
from flask_restx import fields

python2rest= {
    'int' : fields.Integer,
    'str' : fields.String,
    'bool' : fields.Boolean,
    'datetime' : fields.DateTime,
    'float' : fields.Float,
    'list' : fields.List,
    'time' : fields.String
}


# convert Database model to flask model
def model_to_rest(model):
    d ={}
    for c in inspect(model).mapper.columns:
        column_type = python2rest.get(c.type.python_type.__name__)
        d[str(c.name)] = column_type
    return d