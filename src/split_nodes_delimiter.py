from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # print(f' NNNNOOOOODDDDEEESSS {old_nodes}')
# TODO Likely in a separate function, handle non-standard delimiters such as links, images, tables, etc.

    new_nodes = []
    for node in old_nodes:
        new_sub_nodes = []
        if node.text_type != "text":
            new_sub_nodes.extend(node)
        else:
            words = node.text.split()
            # print(words)
            delimiter_toggle = False
            delimited_phrase = []
            text_phrase = []
            spacebar_transfer = False

        for word in words:
            # print(word)
        
# Currently only evaluates delimiters at the start or end of words (all eight (8) scenarios described below). It does **NOT** catch delimiters _within_ words.

# Scenario (1): no delimiter, toggle off
            if delimiter not in word and not delimiter_toggle:
                if spacebar_transfer:
                    spacebar_transfer = False
                    text_phrase.extend([f' {word}'])
                else:
                    text_phrase.extend([word])

# Scenario (2): no delimiter, toggle on
            elif delimiter not in word and delimiter_toggle:
                if spacebar_transfer:
                    spacebar_transfer = False
                    delimited_phrase.extend([f' {word}'])
                else:
                    delimited_phrase.extend([word])

# Scenario (3): delimiter at start and end, toggle off
            elif word.startswith(delimiter) and word.endswith(delimiter) and not delimiter_toggle:
            # Add any non-delimited text as a text node, then reset text_phrase
                if len(text_phrase) > 0:
                    text_string = ' '.join(text_phrase) + ' '
                    new_sub_nodes.extend([TextNode(text_string, "text")])
                    text_phrase.clear()
                    # # print('text_phrase cleared')
                delimiter_toggle = False
                spacebar_transfer = True
                new_sub_nodes.extend([TextNode(word.strip(delimiter), text_type)])

# Scenario (4): delimiter at start and end, toggle on
            elif word.startswith(delimiter) and word.endswith(delimiter) and delimiter_toggle:
                delimited_string = ' '.join(delimited_phrase) + ' '
                new_sub_nodes.extend([TextNode(delimited_string, text_type)])
                delimited_phrase.clear()
                new_sub_nodes.extend([TextNode(word.strip(delimiter), "text")])
                delimiter_toggle = True
                spacebar_transfer = True

# Scenario (5): start delimiter, toggle off
            elif word.startswith(delimiter) and not delimiter_toggle:
                # Add any non-delimited text as a text node, then reset text_phrase
                if len(text_phrase) > 0:
                    text_string = ' '.join(text_phrase) + ' '
                    new_sub_nodes.extend([TextNode(text_string, "text")])
                    text_phrase.clear()
                delimiter_toggle = True
                delimited_phrase.extend([word.strip(delimiter)])

# Scenario (6): start delimiter, toggle on
            elif word.startswith(delimiter) and delimiter_toggle:
                text_phrase.extend([word.strip(delimiter)])
                delimited_string = ' '.join(delimited_phrase) + ' '
                new_sub_nodes.extend([TextNode(delimited_string, text_type)])
            # Reset phrase list and toggle
                delimited_phrase.clear()
                delimiter_toggle = False

# Scenario (7): end delimiter, toggle off
            elif word.endswith(delimiter) and not delimiter_toggle:
                text_phrase.extend([word.strip(delimiter)])
                text_string = ' '.join(text_phrase)
                new_sub_nodes.extend([TextNode(text_string, "text")])
                text_phrase.clear()
                delimiter_toggle = True
                spacebar_transfer = True

# Scenario (8): end delimiter, toggle on
            elif word.endswith(delimiter) and delimiter_toggle:
                if spacebar_transfer:
                    spacebar_transfer = False
                    delimited_phrase.extend([f' {word.strip(delimiter)}'])
                else:
                    delimited_phrase.extend([word.strip(delimiter)])
                delimited_string = ' '.join(delimited_phrase)
                new_sub_nodes.extend([TextNode(delimited_string, text_type)])
            # Reset phrase list and toggle
                delimited_phrase.clear()
                delimiter_toggle = False
                spacebar_transfer = True


            # print(f'text_phrase: {text_phrase}')
            # print(f'delimited_phrase: {delimited_phrase}')

# if delimited phrase is not ended by the end of the list, throw an error.
        if delimiter_toggle:
            raise Exception("Invalid Markdown syntax")
        
# if words does not end with a delimiter, add text node for everything since the last delimiter 
        if len(text_phrase) > 0:
            text_string = ' '.join(text_phrase)
            new_sub_nodes.extend([TextNode(text_string, "text")])
        
        # print(f'New Sub Nodes: {new_sub_nodes}')

        new_nodes.extend(new_sub_nodes)

    # print(f'New Nodes: {new_nodes}')
    return new_nodes


            

