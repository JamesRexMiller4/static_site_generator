from leafnode import LeafNode
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_img = "image"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == "text":
        return LeafNode(text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, { "href": text_node.url })
    elif text_node.text_type == "image":
        return LeafNode("img", "", { "src": text_node.url, "alt": text_node.text })
    else:
        raise Exception("No matching text node type")

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    '''
        This function takes a list of TextNode and (potentially) extends the list
        based on the value of the text_node.text_type. Ex: If the text contains bold text
        within then a delimiter is identified, **, and the appropriate TextNode type
        is extended into the list such that it is [TextNode(text), TextNode(bold), TextNode(text)]
    '''
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
        split_nodes = old_node.text.split(delimiter)
        if len(split_nodes) == 1:
            new_nodes.append(old_node)
        elif len(split_nodes) == 2:
            raise Exception(f"Invalid syntax, missing opening/closing delimiter: {delimiter} in {old_node.text}")
        else:
            for idx, split_node_text in enumerate(split_nodes):
                if idx == 1:
                    new_nodes.append(TextNode(split_node_text, text_type))
                else:
                    new_nodes.append(TextNode(split_node_text, text_type_text))
    return new_nodes