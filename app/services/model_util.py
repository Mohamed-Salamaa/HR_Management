

# converting model to dict
def model_to_dict(model ):
        dict = {column: str(getattr(model, column)) for column in model.__table__.c.keys()}
        return dict

# converting dict to model
def model_from_dict(model , **kwargs):
    if model:
        for key, value in kwargs.items():
            if hasattr(model , key):
                    setattr(model , key , value)
                    # print("key is {0} and value is {1}".format(key , value))
    else:
        print("No Model Found .....!!!!")