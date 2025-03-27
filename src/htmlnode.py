
class HTMLNode():

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self) -> str:
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        prop_string = ""
        if self.props is None:
            return prop_string
        for key, value in self.props.items():
            prop_string += f" {key}={value}"
        return prop_string
