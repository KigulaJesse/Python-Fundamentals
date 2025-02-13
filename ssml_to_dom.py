import re

class SSMLNode:
    def __init__(self, tag, attributes=None, text=None):
        self.tag = tag
        self.attributes = attributes or {}
        self.text = text
        self.children =[]

    def to_dict(self):
        return {
            "tag": self.tag,
            "attributes": self.attributes,
            "text": self.text.strip() if self.text else None,
            "children": [child.to_dict() for child in self.children]
        }

def parse_attributes(attr_string):
    attributes = {}
    for match in re.finditer(r'(\w+)=["\'](.*?)["\']',attr_string):
        attributes[match.group(1)] = match.group(2)
    return attributes

def parse_ssml(ssml):
    tag_pattern = re.compile(r'<(/?)(\w+)([^>]*)')
    tokens = tag_pattern.split(ssml)

    print(tokens)

    root = None
    stack = []

    for i in range(len(tokens)):
        token = tokens[i].strip()
        print(token)
        if not token:
            continue

        



ssml = """
    <speak>
        <voice>
            <prosody rate="slow"> Hello, how are you? </prosody>
        </voice>
    </speak>
"""

tree = parse_ssml(ssml)
# print(tree)
