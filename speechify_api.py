import requests
import base64
import io
from pydub import AudioSegment
from pydub.playback import play

url = "https://api.sws.speechify.com/"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Simple Get voices
# response = requests.get(f"{url}/v1/voices", headers=headers)
# for voice in response.json():
#     print("")
#     print(voice)
    
voice = "george"
text = "Hi this is Jesse's first trial"

data = {
    'input': f"<speak>{text}</speak>",
    'voice_id': voice,
    'audio_format': "mp3"
}


response = requests.post(f"{url}/v1/audio/speech", json=data, headers=headers)
print("")
print(response.status_code)
# print(response.text)

if response.status_code == 200:
   if "audio_data" in response.json():
        print(response.json()["audio_data"])
        audio_data = response.json()["audio_data"]
        audio_bytes = base64.b64decode(audio_data)
        audio_file = io.BytesIO(audio_bytes)
        audio = AudioSegment.from_file(audio_file, format="mp3")

        play(audio)

        with open("output.mp3", "wb") as f:
            f.write(audio_bytes)