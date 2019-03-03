import json
from urllib.request import urlopen
name = "vandann"

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


url = ("https://apps.runescape.com/runemetrics/profile/profile?user=vandann&activities=20")
res = get_jsonparsed_data(url)



print(res.get("totalskill"))
