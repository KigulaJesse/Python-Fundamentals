import xml.etree.ElementTree as ET
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Parse the XML file
tree = ET.parse("speech.xml")
root = tree.getroot()


# # Read and speak each speech tag
# for speech in root.findall("speech"):
#     text = speech.text
#     print(f"Speaking: {text}")
#     engine.say(text)

# # Play all text
# engine.runAndWait()
