from htmlnode import HTMLNode

#TODO: add type hinting to entire file

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        elif self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props})"