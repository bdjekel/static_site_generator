from textnode import TextNode
from extract_markdown_images import extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        image_list = extract_markdown_images(node.text)
        if len(image_list) == 0:
            print(f'No images in node at index [{old_nodes.index(node)}]')
            continue
        else:
            node_text = node.text

            for image in image_list:
                node_text = node_text.replace(image[0], '')
                node_text = node_text.replace(image[1], '')
            word_list = node_text.split()
            indices = [i for i, x in enumerate(word_list) if x == '![]()'] # TODO Review and gain better understanding of this concept.
            
            if len(indices) == len(word_list):
                for i in range(0, len(indices)):
                    new_nodes.extend([TextNode(image_list[i][0], 'image',image_list[i][1])])
            
            else:
                text_phrase = []

                for i in range(0, len(word_list)):
                    if i in indices and len(text_phrase) == 0:
                        new_nodes.extend([TextNode(image_list[0][0], 'image',image_list[0][1])])
                        image_list.pop(0)
                    elif i in indices and len(text_phrase) > 0:
                        new_nodes.extend([TextNode(' '.join(text_phrase), 'text')])
                        text_phrase.clear()
                        new_nodes.extend([TextNode(image_list[0][0], 'image',image_list[0][1])])
                        image_list.pop(0)
                    else:
                        text_phrase.append(word_list[i])

                if len(text_phrase) > 0:
                    new_nodes.extend([TextNode(' '.join(text_phrase), "text")])





            

    print(new_nodes)
    return new_nodes


split_nodes_image(old_nodes)
