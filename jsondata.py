import json
import datetime
from datetime import date
data =json.load(open('all.json'))
#print(data)
#print(type(data))
# data['date'] = datetime.datetime.now()
#
# def myconverter(o):
#     if fromisoformat(o, datetime.datetime):
#         return o.__repr__()
#
# print(json.dumps(data, default = myconverter)

with open('all.json', 'r') as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(type(json_value))
    print(json_value)
