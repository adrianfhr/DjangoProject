import yaml    # type: ignore


def yaml_coerce(value):
    # convert value to proper Python

    if isinstance(value, str):
        # yaml.load returns a python object
        # Convert the string to a dictionary examp;e : "{'apples': 3, 'bacon': 2}" to Python dictionary
        # usefull because sometimes we need stringfy setting this way (e.g. in Dockerfile)
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value 
