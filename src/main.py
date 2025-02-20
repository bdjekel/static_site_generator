from textnode import TextNode
from textnode import TextType

def main():
    dummy = TextNode("eat my shorts", TextType.BOLD, "www.dummyvalues.org")
    return repr(dummy)

main()