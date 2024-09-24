from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        new_sub_nodes = []
        words = node.split()
        print(words)
        delimiter_toggle = False
        delimited_phrase = []
        text_phrase = []

        for word in words:
            print(word)
# Currently evaluates all eight (8) conditions where delimiters are at the start or end of strings.

# 'This' in 'This *is example* text'
            if delimiter not in word and not delimiter_toggle:
                text_phrase.extend([word])

# 'is' in '*This is example* text'
            elif delimiter not in word and delimiter_toggle:
                delimited_phrase.extend([word])

# '*example*' in 'This is *example* text'
            elif word.startswith(delimiter) and word.endswith(delimiter) and not delimiter_toggle:
            # Add any non-delimited text as a text node, then reset text_phrase
                if len(text_phrase) > 0:
                    text_string = ' '.join(text_phrase) + ' '
                    new_sub_nodes.extend([TextNode(text_string, "text")])
                    text_phrase.clear()
                    print('text_phrase cleared')
                delimiter_toggle = False # Likely unnecessary
                new_sub_nodes.extend([TextNode(word[1:-1], text_type)])


# TO-DO Add case ==> '*example*' in '*This is *example* text*'


# 'is*' in 'This is* example* text'
            elif word.endswith(delimiter) and not delimiter_toggle:
                text_phrase.extend([word[:-1]])
                text_string = ' '.join(text_phrase) + ' '
                new_sub_nodes.extend([TextNode(text_string, "text")])
                text_phrase.clear()
                delimiter_toggle = True            

# 'example*' in 'This *is example* text'
            elif word.endswith(delimiter) and delimiter_toggle:
                delimited_phrase.extend([word[:-1]])
                delimited_string = ' '.join(delimited_phrase) + ' '
                new_sub_nodes.extend([TextNode(delimited_string, text_type)])
            # Reset phrase list and toggle
                delimited_phrase.clear()
                delimiter_toggle = False  

# '*is' in 'This *is example* text'
            elif word.startswith(delimiter) and not delimiter_toggle:
                # Add any non-delimited text as a text node, then reset text_phrase
                if len(text_phrase) > 0:
                    text_string = ' '.join(text_phrase) + ' '
                    new_sub_nodes.extend([TextNode(text_string, "text")])
                    text_phrase.clear()
                delimiter_toggle = True
                delimited_phrase.extend([word[1:]])

# '*text' in 'This *is example *text'
            elif word.endswith(delimiter) and delimiter_toggle:
                delimited_phrase.extend([word[:-1]])
                delimited_string = ' '.join(delimited_phrase) + ' '
                new_sub_nodes.extend([TextNode(delimited_string, text_type)])
            # Reset phrase list and toggle
                delimited_phrase.clear()
                delimiter_toggle = False 

            print(f'text_phrase: {text_phrase}')
            print(f'delimited_phrase: {delimited_phrase}')


# if words does not end with a delimiter, add text node for everything since the last delimiter 
        if len(text_phrase) > 0:
            text_string = ' '.join(text_phrase)
            new_sub_nodes.extend([TextNode(text_string, "text")])
        
        print(f'New Sub Nodes: {new_sub_nodes}')

        new_nodes.extend(new_sub_nodes)

    print(f'New Nodes: {new_nodes}')

             

            

split_nodes_delimiter(["tickle me *tiddies*", "your *hankies* are so panky", "*third's* the word"], '*', 'italic')