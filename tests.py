import re

# pattern = re.compile(r"<(/?)(\w+)([^>]*)>")
pattern = re.compile(r"<(/?)(\w+)([^>]*)>")

# Example HTML-like string
text = """
    <div class='container' name="james" id="james">
        Content
        <br/>
    </div>
"""

matches = pattern.findall(text)

for match in matches:
    print(match)