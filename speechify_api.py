import requests

url = "https://api.sws.speechify.com/"
api_key = "GPvah_Ak2J2kvcdEPX3ZuWQTIjxB7JbvyH2Ruu3_3t4="
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

#Simple Get voices
# response = requests.get(f"{url}/v1/voices", headers=headers)
# for voice in response.json():
#     print("")
#     print(voice)
    
