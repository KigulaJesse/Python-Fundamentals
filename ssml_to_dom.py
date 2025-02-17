class TreeNode:
    """A simple tree node representation for SSML elements."""
    def __init__(self, tag=None, attributes=None, text=None):
        self.tag = tag  # e.g., 'speak', 'voice', 'break'
        self.attributes = attributes if attributes else {}  # Store tag attributes
        self.text = text.strip() if text else None  # Store text separately
        self.children = []  # List of child nodes

    def add_child(self, child):
        """Adds a child node to the current node."""
        self.children.append(child)

    def __repr__(self, level=0):
        """Custom representation for visualization."""
        indent = "  " * level
        attr_str = f" {self.attributes}" if self.attributes else ""
        text_str = f": {self.text}" if self.text else ""
        repr_str = f"{indent}<{self.tag}{attr_str}>{text_str}\n"
        for child in self.children:
            repr_str += child.__repr__(level + 1)
        return repr_str


def parse_ssml(ssml):
    """Manually parse SSML into a tree representation."""
    ssml = ssml.strip()
    index, length = 0, len(ssml)
    root = TreeNode("root")  # Root node
    stack = [root]

    while index < length:
        if ssml[index] == "<":
            # Closing tag case
            if ssml[index + 1] == "/":
                end_index = ssml.find(">", index)
                stack.pop()  # Close the current node
                index = end_index + 1
            else:
                # Opening tag
                end_index = ssml.find(">", index)
                tag_content = ssml[index + 1:end_index]
                
                # Extract tag name and attributes
                parts = tag_content.split()
                tag_name = parts[0]
                attributes = {}

                # Extract attributes
                for part in parts[1:]:
                    if "=" in part:
                        key, value = part.split("=", 1)
                        attributes[key] = value.strip("\"'")

                # Create a new node
                node = TreeNode(tag_name, attributes)
                stack[-1].add_child(node)  # Attach to the current parent
                stack.append(node)  # Make it the current node

                index = end_index + 1
        else:
            # Text Node Case
            end_index = ssml.find("<", index)
            text_content = ssml[index:end_index].strip()
            if text_content:
                text_node = TreeNode(tag="text", text=text_content)
                stack[-1].add_child(text_node)  # Attach text to the current parent
            index = end_index

    return root


# Example SSML Input
ssml_data = """
<speak>
    <voice name="Emma">
        Hello there!
        <break time="500ms"/>
        <prosody rate="slow">This is a test.</prosody>
    </voice>
</speak>
"""

# Parse and print tree representation
ssml_tree = parse_ssml(ssml_data)
print(ssml_tree)
