from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children=None, props=None):
        super().__init__(tag, None, children, props)
        

    def to_html(self):
        if self.children == None:
            raise ValueError("Parent node must have children.")
        if self.tag == None:
            raise ValueError("Parent node must have tag.")
        else:
            html_string = f"<{self.tag}>"
            for node in self.children:
                html_string += node.to_html()
            html_string += f"</{self.tag}>"
            return html_string