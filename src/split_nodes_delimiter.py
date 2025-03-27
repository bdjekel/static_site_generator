from textnode import TextNode
from textnode import TextType

# TODO: consider refactoring the conditionals below to DRY up the code a bit. There might be some repetition that can be wrapped into helper functions. If not, consider making each condition its own helper function.

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    
    new_nodes = []

    for node in old_nodes:
        new_sub_nodes = []
        if delimiter not in node.text:
            new_sub_nodes.extend([node])
        else:
            if node.text[0] == " ":
                spacebar_transfer = True
            else:
                spacebar_transfer = False
            words = node.text.split()
            delimiter_toggle = False
            delimited_word_list = []
            text_word_list = []
            for word in words:
        
# Currently only evaluates delimiters at the start or end of words (the ten (10) scenarios described below). It does **NOT** catch delimiters _within_ words. (e.g., "Jim puts the _x_ in e_x_tra." Will not return extra with a bolded x.) This includes formatted words ending in punctuation (e.g., "This **bold phrase**, will throw an error.")

# Scenario (9): isolated delimiter, toggle off
                if word == delimiter and not delimiter_toggle:
                    if len(text_word_list) > 0:
                        text_string = ' '.join(text_word_list) + ' '
                        new_sub_nodes.extend([TextNode(text_string, TextType.TEXT)])
                        text_word_list.clear()
                    delimiter_toggle = True
                    spacebar_transfer = True

    # Scenario (10): isolated delimiter, toggle on
                elif word == delimiter and delimiter_toggle:
                    delimited_string = ' '.join(delimited_word_list) + ' '
                    new_sub_nodes.extend([TextNode(delimited_string, text_type)])
                    delimited_word_list.clear()
                    delimiter_toggle = False
                    spacebar_transfer = True

    # Scenario (1): no delimiter, toggle off
                elif delimiter not in word and not delimiter_toggle:
                    if spacebar_transfer:
                        spacebar_transfer = False
                        text_word_list.extend([f' {word}'])
                    else:
                        text_word_list.extend([word])

    # Scenario (2): no delimiter, toggle on
                elif delimiter not in word and delimiter_toggle:
                    if spacebar_transfer:
                        spacebar_transfer = False
                        delimited_word_list.extend([f' {word}'])
                    else:
                        delimited_word_list.extend([word])

    # Scenario (3): delimiter at start and end, toggle off
                elif word.startswith(delimiter) and word.endswith(delimiter) and not delimiter_toggle:
                    if len(text_word_list) > 0:
                        text_string = ' '.join(text_word_list) + ' '
                        new_sub_nodes.extend([TextNode(text_string, TextType.TEXT)])
                        text_word_list.clear()
                    delimiter_toggle = False
                    spacebar_transfer = True
                    new_sub_nodes.extend([TextNode(word.strip(delimiter), text_type)])

    # Scenario (4): delimiter at start and end, toggle on
                elif word.startswith(delimiter) and word.endswith(delimiter) and delimiter_toggle:
                    delimited_string = ' '.join(delimited_word_list) + ' '
                    new_sub_nodes.extend([TextNode(delimited_string, text_type)])
                    delimited_word_list.clear()
                    new_sub_nodes.extend([TextNode(word.strip(delimiter), TextType.TEXT)])
                    delimiter_toggle = True
                    spacebar_transfer = True

    # Scenario (5): start delimiter, toggle off
                elif word.startswith(delimiter) and not delimiter_toggle:
                    if len(text_word_list) > 0:
                        text_string = ' '.join(text_word_list) + ' '
                        new_sub_nodes.extend([TextNode(text_string, TextType.TEXT)])
                        text_word_list.clear()
                    delimiter_toggle = True
                    delimited_word_list.extend([word.strip(delimiter)])

    # Scenario (6): start delimiter, toggle on
                elif word.startswith(delimiter) and delimiter_toggle:
                    text_word_list.extend([word.strip(delimiter)])
                    delimited_string = ' '.join(delimited_word_list) + ' '
                    new_sub_nodes.extend([TextNode(delimited_string, text_type)])
                    delimited_word_list.clear()
                    delimiter_toggle = False

    # Scenario (7): end delimiter, toggle off
                elif word.endswith(delimiter) and not delimiter_toggle:
                    text_word_list.extend([word.strip(delimiter)])
                    text_string = ' '.join(text_word_list)
                    new_sub_nodes.extend([TextNode(text_string, TextType.TEXT)])
                    text_word_list.clear()
                    delimiter_toggle = True
                    spacebar_transfer = True

    # Scenario (8): end delimiter, toggle on
                elif word.endswith(delimiter) and delimiter_toggle:
                    if spacebar_transfer:
                        spacebar_transfer = False
                        delimited_word_list.extend([f' {word.strip(delimiter)}'])
                    else:
                        delimited_word_list.extend([word.strip(delimiter)])
                    delimited_string = ' '.join(delimited_word_list)
                    new_sub_nodes.extend([TextNode(delimited_string, text_type)])
                    delimited_word_list.clear()
                    delimiter_toggle = False
                    spacebar_transfer = True


# if delimited word_list is not ended by the end of the list, throw an error.
            if delimiter_toggle:
                raise Exception('Invalid Markdown syntax')
        
# if words does not end with a delimiter, add text node for everything since the last delimiter 
            if len(text_word_list) > 0:
                text_string = ' '.join(text_word_list)
                new_sub_nodes.extend([TextNode(text_string, TextType.TEXT)])
        

        new_nodes.extend(new_sub_nodes)

    return new_nodes


            

