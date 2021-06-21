import requests
import json

latestComicResp = requests.get("https://xkcd.com/info.0.json")
latestComingRespJson = json.loads(latestComicResp.text)

latestId = int(latestComingRespJson['num'])

with open("descriptions.txt", 'w', encoding='utf-8') as outfile:
    for i in range(latestId + 1):
        response = requests.get(f"https://xkcd.com/{i}/info.0.json")
        if response.status_code == 200:
            respJson = json.loads(response.text)
            outfile.write(respJson['transcript'] + "\n")
            outfile.write(respJson['alt'] + "\n")
        print(f"{i}/{latestId + 1} done")
