import json

#load načítá z otevřeného souboru
#loads načítá ze stringu
#dump vezme reprezentaci v pythonu a vrátí jako řetězec

adict = json.loads('{"key":12}')
print(adict['key'])
adict['key2']=None

json.dumps(adict)   #dumps převrací do stringu
print(json.dumps(adict))

with open("output.sdon", "w") as f:
    json.dump(adict, f)

