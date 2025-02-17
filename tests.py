import re

# Your SSML string
ssml_string = """
<speak>
  <voice name="en-US-Wavenet-D">
    Hello, how are you today?
  </voice>
</speak>
"""

# Regular expression to capture tags and content
pattern = r'<([^/][^>]+)>(.*?)<\/\1>'

# Find all the tags and their content
matches = re.findall(pattern, ssml_string)
print("")
print(matches)
print("")
# Print out each tag and its content
for tag, content in matches:
    print(f"Tag: {tag}, Content: {content}")
