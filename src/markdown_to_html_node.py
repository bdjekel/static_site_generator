from block_to_block_type import block_to_block_type, BlockType
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_children import text_to_children


def markdown_to_html_node(markdown):
    wrapper_div = ParentNode("div", children=[])
    markdown_blocks = markdown_to_blocks(markdown)
    
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                block = block.strip("`")    # Since "`" is both a block level and inline level delimiter, must be stripped to avoid throwing error
                code_node = ParentNode(block_type.value, block)
                wrapper_div.children.append(code_node)
            case BlockType.UNORDERED_LIST:
                ul_node = ParentNode(BlockType.UNORDERED_LIST, children=[])
                wrapper_div.children.append(ul_node)
                # TODO: add list items as children
            case BlockType.ORDERED_LIST:
                ol_node = ParentNode(BlockType.ORDERED_LIST, children=[])
                wrapper_div.children.append(ol_node)
                # TODO: add list items as children

        children = text_to_children(block)
        block_html_node.children = children
    # print(f"\n-----------\n{wrapper_div}\n-----------\n")
    return wrapper_div

def list_items_to_leaf_nodes(block, tag):
    leaf_nodes = []
    list_items = block.splitlines()
    for item in list_items:
        leaf_nodes.append(LeafNode(tag, item))
    print("\n\n------------------\n\n")    
    print(f"{leaf_nodes}")    
    print("\n\n------------------\n\n")
    return leaf_nodes

# Split the markdown into blocks (you already have a function for this)
# Loop over each block:
    # Determine the type of block (you already have a function for this)
    # Based on the type of block, create a new HTMLNode with the proper data
    # Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
    # The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
# Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
md1 = """
# Code block below

```go
type User struct {
    name: Jimbo
    password: craigLeg
}
```

## quote below

> "29 Kids go into the water, **22 Kids** come out of the water. 
> The Ice _Cream Man,_ He gets the rest. 
> April the 9th, Half past four P.M."

### unordered list below

- Quoted Actor: Dana Carvey
- Quoted Movie: Master of Disguise
- IMDb Rating: `3.4 / 10`
- Metascore: 12 / 100
- My Rating: 7 / 10

#### ordered list below

1. watch better movies
2. like those better [movies](https://fake.link.io)
3. stop quoting ~~thinking about~~ impressively bad movies
4. get friends ![fake pic](https://fake.picture.io/fakepic.jpg)
"""


md2 = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

md_node_tree = markdown_to_html_node(md1)

#TODO: the below throws an error due to "NotImplementedError." This means your program is not correctly labelling Parent and Child Nodes. Think through your solution thoroughly before fixing the bug.
md_html = md_node_tree.to_html()
print(md_html)





















