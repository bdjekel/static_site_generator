from textnode import TextNode
from extract_markdown_images import extract_markdown_images


node_1 = TextNode('This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
node_2 = TextNode('This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', 'text')
node_3 = TextNode('This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)', 'text')
node_4 = TextNode('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', 'text')

old_nodes = [
    node_1,
    # node_2,
    # node_3,
    # node_4
]

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        word_list = []        
        print(node.text)
        image_list = extract_markdown_images(node.text)
        print(image_list)
        node_v0 = node.text
        for image in image_list:
            print(f'V0 => {node_v0}')
            print(image[0])
            node_v1 = node_v0.replace(image[0], '')
            print(f'V1 => {node_v1}')
            node_v2 = node_v1.replace(image[1], '')
            print(f'V2 => {node_v2}')
            node_v0 = node_v2    
        node_list = node_v0.split()
        indices = [i for i, x in enumerate(node_list) if x == '![]()']
        print(indices)
        
        for i in range(0, len(indices) - 1):
            if indices[i] == 0:
                new_nodes.extend([TextNode(image_list[i][0], 'image', image_list[i][1])])
            elif indices[i] == len(image_list) - 1:
                new_nodes.extend([TextNode(word_phrase, 'text')])
                new_nodes.extend([TextNode(image_list[indices[i]][0], 'image', image_list[indices[i]][1])])
            else:
                word_phrase = node_list[indices[i - 1]:indices[i]]
                new_nodes.extend([TextNode(word_phrase, 'text')])
                word_phrase.clear()
                new_nodes.extend([TextNode(image_list[indices[i]][0], 'image', image_list[indices[i]][1])])

            


            # new_nodes.extend(TextNode(image[0], 'image', image[1]))



split_nodes_image(old_nodes)



# new_nodes = split_nodes_image([node])
# [
#     TextNode('This is text with a link ', 'text'),
#     TextNode('to boot dev', 'link', 'https://www.boot.dev'),
#     TextNode(' and ', 'text'),
#     TextNode(
#         'to youtube', 'link', 'https://www.youtube.com/@bootdotdev'
#     ),
# ]