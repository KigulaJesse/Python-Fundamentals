
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

# def to_xml(node, level=0):
#     indent = "  " * level
#     name = node.name
#     attrs = "".join(f"{k}='{v}'" for k,v in node.attributes.items())
#     attrs = f" {attrs}" if attrs else ""
#     text = node.text





root = SSMLTag("speak")
voice = SSMLTag("voice", {'name':'Joanna'})
say_as = SSMLTag("say-as", {'interpret-as':'date', 'type':"new"}, '2024-02-12')
voice.add_child(say_as)
root.add_child(voice)

print(say_as.__repr__)








