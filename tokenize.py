from collections import namedtuple

Token = namedtuple("Token", ['type', 'value'])

TOKEN_TYPES = {
    "OPEN TAG": "OPEN TAG",
    "CLOSING TAG": "CLOSING TAG",
    "SELF CLOSING TAG":"SELF CLOSING TAG",
    "ATTRIBUTE NAME": "ATTRIBUTE NAME",
    "ATTRIBUTE VALUE":"ATTRIBUTE VALUE",
    "TEXT":"TEXT",
}


import re

class XMLTokenizer:
    def __init__(self, xml_text):
        self.xml_text = xml_text
        self.position = 0
        self.length = len(xml_text)

    def next_token(self):
        if self.position >= self.length:
            return None
        
        char = self.xml_text[self.position]
        if char == "<":
            end = self.xml_text.find(">",self.position)
            if end == -1:
                raise ValueError("Malformed XML: Missing closing '>'")
            
            tag_content = self.xml_text[self.position + 1:end].strip()
            print("")
            print(tag_content)
            print("")

        self.position = self.position + 1
        return None


    
    def tokenize(self):
        """Tokenize the entire XML document"""
        tokens = []
        while self.position < self.length:
            # print(self.position)
            # print(self.length)
            token = self.next_token()
            if token:
                tokens.append(token)
        return tokens


xml_sample = """
<root>
    <name>John Doe</name>
    <age>30</age>
    <address city="New York" />
</root>
"""


tokenizer = XMLTokenizer(xml_sample)
tokens = tokenizer.tokenize()

for token in tokens:
    print(token)