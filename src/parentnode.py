from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag="", children=None, props=None):
        if children == None:
            children = []
        super().__init__(tag=tag, children=children, props=props)
        

    def to_html(self):
        if self.children == None or len(self.children) == 0:
            raise ValueError("Parent node must have children.")
        if self.tag == "":
            raise ValueError("Parent node must have tag.")
        else:
            html_string = f"<{self.tag}>"
            for node in self.children:
                if node.tag and len(node.tag) > 0:
                    html_string += f"<{node.tag}>{node.value}</{node.tag}>"
                else:
                    html_string += f"{node.value}"
            html_string += f"</{self.tag}>"
            return html_string