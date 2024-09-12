

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        if self.props is None:
            return prop_string
        for key, value in self.props:
            prop_string + f" {key}={value}"
        return prop_string

