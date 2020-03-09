import json
import pandas as pd
import datetime

json_file = open("event_log.json", mode="r")
json_file = json_file.read()
json_file = "[" + json_file[:-1] + "]"
data = json.loads(json_file)
#  "timest_format":"yyyy-MM-dd'T'HH:mm:ss.SSSZ"
for i in data:
    if i["Event_type"] == "Start":
        i["Event_type"] = "start"
    else:
        i["Event_type"] = "complete"

    # i["TimeStamp"] = pd.to_datetime(i["TimeStamp"])
    # i["TimeStamp"] = i["TimeStamp"].strftime('%Y-%m-%dT%H:%M:%S.000Z')

json_file = open("file_json.json", mode="w")
json.dump(data, json_file)
print(data)
