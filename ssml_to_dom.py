import re

class SSMLTag:
    def __init__(self, name, attributes=None, text=None):
        self.name = name
        self.attributes = attributes or {}
        self.text = text
        self.children = []
    
    def add_child(self, tag):
        self.children.append(tag)
    
    def __repr__(self, level=0):
        indent = "  " * level
        attrs = " ".join(f'{k} = "{v}"' for k,v in self.attributes.items())
        print(attrs)
        # attrs = f" {attrs}" if attrs else ""
        text = f"\n {indent}{self.text}" if self.text else ""
        result = f"{indent}<{self.name} {attrs}>{text} \n"
        for child in self.children:
            result += child.__repr__(level + 1)
        result += f"{indent}<{self.name}/>\n"
        return result



# ssml_string = """
#     <speak>
#         <voice name="Joanna">
#             <say-as interpret-as="date">2024-02-12</say-as>
#         </voice>
#     </speak>
# """

def to_xml(node, level=0):
    indent = "  " * level
    attrs = "".join(f" {k}='{v}'" for k,v in node.attributes.items())
    text = node.text if node.text else ""
    
    if not node.children:
        return f"{indent}<{node.name}{attrs}>{text}</{node.name}> \n"
    
    xml = f"{indent}<{node.name}{attrs}>{text} \n"
    for child in node.children:
        xml += to_xml(child, level + 1)
    xml += f"{indent}<{node.name}/>\n"
    return xml

def parse_xml(xml_string):
    """Parses XML"""
    tag_pattern = None
    attribute_pattern = None
    text_pattern = None

    

root = SSMLTag("speak")
voice = SSMLTag("voice", {'name':'Joanna'})
say_as = SSMLTag("say-as", {'interpret-as':'date', 'type':"new"}, '2024-02-12')
voice.add_child(say_as)
root.add_child(voice)

print(to_xml(root))








