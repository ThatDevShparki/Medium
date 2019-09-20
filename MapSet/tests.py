from mapset import MapSet
import json

with open('test_a.json', 'r') as f:
    data_a = json.load(f)

with open('test_b.json', 'r') as f:
    data_b = json.load(f)

with open('test_c.json', 'r') as f:
    data_c = json.load(f)

ms = MapSet(data_c)

# print(ms['hello'])