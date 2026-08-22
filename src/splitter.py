from textnode import TextNode, TextType
import re

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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_images(node.text)
        text_list = node.text
        for i in range(0, len(links), 1):
            curr_text_link = f"![{links[i][0]}]({links[i][1]})"
            text_list = text_list.split(curr_text_link)
            if len(text_list) > 0:
                new_nodes.append(TextNode(text_list[0], TextType.PLAIN));
            
            new_nodes.append(TextNode(links[i][0], TextType.IMAGE, links[i][1]));
            if len(text_list) > 0:
                text_list = ''.join(text_list[1:])

        if len(text_list) > 0:
            new_nodes.append(TextNode(text_list[0], TextType.PLAIN));

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        text_list = node.text
        for i in range(0, len(links), 1):
            curr_text_link = f"[{links[i][0]}]({links[i][1]})"
            text_list = text_list.split(curr_text_link)
            if len(text_list) > 0:
                new_nodes.append(TextNode(text_list[0], TextType.PLAIN));
            
            new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]));
            if len(text_list) > 0:
                text_list = ''.join(text_list[1:])

        if len(text_list) > 0:
            new_nodes.append(TextNode(text_list[0], TextType.PLAIN));

    return new_nodes

def extract_markdown_images(text: str) -> list[(str, str)]:
    listOfImageAttrs = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return listOfImageAttrs

def extract_markdown_links(text: str) -> list[(str, str)]:
    listOfLinkAttrs = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return listOfLinkAttrs
