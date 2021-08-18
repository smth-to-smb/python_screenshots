import json

# Parses the JSON config file and return a dictionary with settings
def config_parsing():
    jsons = open('/home/anton/Desktop/python_screenshots/json_config.json', 'r')

    entity = []

    for i in jsons:
        entity.append(i)

    myString = ''.join(entity)

    total = json.loads(myString)

    return total
