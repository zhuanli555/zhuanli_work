import os
import json
fs = (None, None, '{"json_latitude":"31.29","json_longitude":"121.55","json_time":"2015-04-04 15:56:28"}')
tmp = json.loads(fs[2])

for key in tmp:
    print (key,tmp[key])