import re

class SSMLNode:
    def __init__(self, tag, attributes=None, text=None):
        self.tag = tag  # e.g., "speak", "break", "voice"
        self.attributes = attributes if attributes else {}  # Store tag attributes
        self.text = text  # Store inner text
        self.children = []  # Child nodes

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        indent = "  " * level
        result = f"{indent}<{self.tag} {self.attributes}>\n"
        if self.text:
            result += f"{indent}  {self.text}\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        result += f"{indent}</{self.tag}>\n"
        return result

import re

class SSMLParser:
    def __init__(self, ssml):
        self.tokens = self.tokenize(ssml)
        self.current_index = 0

    def tokenize(self, ssml):
        """Splits the SSML text into meaningful tokens."""
        token_pattern = r"(<[^>]+>|[^<>]+)"
        tokens = re.findall(token_pattern, ssml)
        print("Tokens:", tokens)  # Debugging the tokens
        return tokens


    def parse(self):
        """Parses tokens into a DOM-like tree structure."""
        if not self.tokens:
            return None
        return self._parse_element()

    def _parse_element(self):
        """Parses an individual SSML element and its children."""
        token = self.tokens[self.current_index]

        if token.startswith("<") and not token.startswith("</"):
            # Extract tag name
            tag_name = re.match(r"<(\w+)", token).group(1)
            attributes = self._parse_attributes(token)

            node = SSMLNode(tag=tag_name, attributes=attributes)
            self.current_index += 1  # Move to next token

            # Recursively process child elements until closing tag
            while self.current_index < len(self.tokens):
                next_token = self.tokens[self.current_index]

                if next_token.startswith(f"</{tag_name}>"):  # Closing tag found
                    self.current_index += 1  # Move past closing tag
                    return node
                else:
                    node.add_child(self._parse_element())  # Parse child

        elif not token.startswith("<"):
            # Plain text node: Here we make sure the text is properly assigned
            node = SSMLNode(tag="text", text=token.strip())
            self.current_index += 1
            return node

        return None


    def _parse_attributes(self, tag_string):
        """Extracts attributes from a tag string."""
        attributes = {}
        matches = re.findall(r'(\w+)="([^"]+)"', tag_string)
        for key, value in matches:
            attributes[key] = value
        return attributes

ssml_text = '''
<speak>
  <voice name="Matthew">Hello, how are you?</voice>
  <break time="500ms"/>
  <prosody pitch="+10%">I am excited!</prosody>
</speak>
'''

parser = SSMLParser(ssml_text)
dom = parser.parse()
print(dom)