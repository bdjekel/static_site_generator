from htmlnode import HTMLNode
from leafnode import LeafNode

class TextNode():
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case "text":
                return LeafNode(value=text_node.text)
            case "bold":
                return LeafNode("b", text_node.text)
            case "italic":
                return LeafNode("i", text_node.text)
            case "code":
                return HTMLNode("code", text_node.text)
            case "link":
                return HTMLNode("a", text_node.text, None, {"href": f"{text_node.url}"})
            case "image":
                return HTMLNode("img","", None, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
            case _:
                raise TypeError("Not a valid text type.")