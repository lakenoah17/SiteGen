from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        
        text_list = node.text.split(delimiter)
        if len(text_list) % 2 != 1:
            raise Exception("[SplitNodesDelimiter] Not a matching amount of delimiters")
        
        first_char_delim = node.text[0:len(delimiter) + 1] == delimiter
        for i in range(0, len(text_list)):
            if first_char_delim and i % 2 == 0:
                new_nodes.append(TextNode(text_list[i], text_type))
            elif not first_char_delim and i % 2 == 1:
                new_nodes.append(TextNode(text_list[i], text_type))
            else:
                new_nodes.append(TextNode(text_list[i], TextType.PLAIN))

    return new_nodes

