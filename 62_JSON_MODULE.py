#JSON(JAVA SCRIPT OBJECT NOTATION)

import json
data = '{"var1":"punit", "var2":100}'
print(type(data))
passed = json.loads(data)
print(type(passed))
print(passed)

data2 = {"channel_name":"punitmann", "cars":['bmw', 'audi a8'], "fridge":['ice cream', 'fruits']}
print(type(data2))
jscomp = json.dumps(data2)
print(type(jscomp))
print(jscomp)