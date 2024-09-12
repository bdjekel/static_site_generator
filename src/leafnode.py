from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag="", value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == "":
            return f"{self.value}"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"