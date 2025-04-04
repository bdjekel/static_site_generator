import re
from textnode import TextNode
from textnode import TextType
from extract_markdown_images import extract_markdown_images

#TODO: add type hinting to entire file
#TODO: commented out test below func needs to be moved to test_split_nodes_image.py

def split_nodes_image(old_nodes: list):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.extend([node])
        else:
            sub_nodes = []
            sub_nodes_text = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", node.text)
            sub_nodes_text = [s for s in sub_nodes_text if len(s) > 0 and s != " "]
            for s in sub_nodes_text:
                if "![" in s:
                    image_data = extract_markdown_images(s)
                    sub_nodes.extend([TextNode(image_data[0][0], TextType.IMAGE, image_data[0][1])])
                else:
                    sub_nodes.extend([TextNode(s, TextType.TEXT)])
            new_nodes.extend(sub_nodes)
    return new_nodes




# list = [
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), 
    
#     TextNode(to boot dev, image, https://www.boot.dev), 
#     TextNode( and, text, None), 
    
#     TextNode(and , text, None), 
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), 
    
#     TextNode(to boot dev, image, https://www.boot.dev), 
#     TextNode( , text, None), 
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), 
    
#     TextNode(to boot dev, image, https://www.boot.dev), 
#     TextNode( <== Click this link for boot. Click this link for video ==> , text, None), 
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), 
    
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), 
#     TextNode( Click this image, text, None), 

#     TextNode(This is text with two images , text, None), 
#     TextNode(to boot dev, image, https://www.boot.dev), 
#     TextNode( and , text, None), 
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), 
    
#     TextNode(This is text with a link [to boot dev](https://www.boot.dev) and an image , text, None), 
#     TextNode(to youtube, image, https://www.youtube.com/@bootdotdev)]