from textnode import TextNode
from textnode import TextType

#TODO: incomplete

def main():
    dummy = TextNode("eat my shorts", TextType.BOLD, "www.dummyvalues.org")
    return repr(dummy)

main()