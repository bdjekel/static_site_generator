

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
        print("\n\n--------PROPS--------\n\n")
        print(f"{self.props}")
        for key, value in self.props.items():
            print(f"{key}")
            print(f"{value}")
            prop_string += f" {key}={value}"
        print("\n\n--------PROPS--------\n\n")
        return prop_string

# TODO: Add test condition for multiple props.