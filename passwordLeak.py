import leakPasswd
import json
result = leakPasswd.findAccount('gza_scnu@163.com')
print(json.dumps(result,indent=4))
