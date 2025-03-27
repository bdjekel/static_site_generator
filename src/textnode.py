from enum import Enum
from leafnode import LeafNode

#TODO: add type hinting to entire file

class TextType(Enum):
    TEXT = ""
    BOLD = "b"
    ITALIC = "i"
    STRIKETHROUGH = "s"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    
    def __init__(self, text: str, text_type: TextType, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be an instance of TextType Enum")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case text_node.TEXT:
                return LeafNode(value=text_node.text)
            case text_node.BOLD:
                return LeafNode("b", text_node.text)
            case text_node.ITALIC:
                return LeafNode("i", text_node.text)
            case text_node.STRIKETHROUGH:
                return LeafNode("s", text_node.text)
            case text_node.CODE:
                return LeafNode("code", text_node.text)
            case text_node.LINK:
                return LeafNode("a", text_node.text, None, {"href": f"{text_node.url}"})
            case text_node.IMAGE:
                return LeafNode("img","", None, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
            case _:
                raise TypeError("Not a valid text type.")
            



