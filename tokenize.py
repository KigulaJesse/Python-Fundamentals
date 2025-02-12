# from collections import namedtuple

# Token = namedtuple("Token", ['type', 'value'])

# TOKEN_TYPES = {
#     "OPEN_TAG": "OPEN_TAG",
#     "CLOSING_TAG": "CLOSING_TAG",
#     "SELF_CLOSING_TAG":"SELF_CLOSING_TAG",
#     "ATTRIBUTE_NAME": "ATTRIBUTE_NAME",
#     "ATTRIBUTE_VALUE":"ATTRIBUTE_VALUE",
#     "TEXT":"TEXT",
# }


# import re

# class XMLTokenizer:
#     def __init__(self, xml_text):
#         self.xml_text = xml_text
#         self.position = 0
#         self.length = len(xml_text)

#     def next_token(self):
#         if self.position >= self.length:
#             return None
        
#         char = self.xml_text[self.position]
#         if char == "<":
#             end = self.xml_text.find(">",self.position)
#             if end == -1:
#                 raise ValueError("Malformed XML: Missing closing '>'")
            
#             tag_content = self.xml_text[self.position + 1:end].strip()
#             self.position = end + 1

#             if tag_content.endswith("/"):
#                 print(tag_content[:-1])
#                 return Token(TOKEN_TYPES['SELF_CLOSING_TAG'], tag_content[:-1].strip())
            
#             if tag_content.startswith("/"):
#                 print(tag_content[1:])
#                 return Token(TOKEN_TYPES['CLOSING_TAG'],tag_content[1:].strip())
            
#             # print("")
#             # print(self.xml_text[self.position])
#             # print(tag_content)
#             # print(self.xml_text[end])
#             # print("")

#         self.position = self.position + 1
#         return None


    
#     def tokenize(self):
#         """Tokenize the entire XML document"""
#         tokens = []
#         while self.position < self.length:
#             # print(self.position)
#             # print(self.length)
#             token = self.next_token()
#             if token:
#                 tokens.append(token)
#         return tokens


# xml_sample = """
# <root>
#     <name>John Doe</name>
#     <age>30</age>
#     <address city="New York" />
# </root>
# """


# tokenizer = XMLTokenizer(xml_sample)
# tokens = tokenizer.tokenize()

# print("Printing Tokens")
# print("=================")
# for token in tokens:
#     print(token)




# xml_sample = """
# <root>
#     <name>John Doe</name>
#     <age>30</age>
#     <address city="New York" />
# </root>
# """