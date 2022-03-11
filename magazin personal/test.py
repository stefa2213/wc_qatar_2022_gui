import json

filename = 'mag.json'
with open(filename, 'w') as f:
    data = json.write(f)
    data['id'] = 134

print(data)
