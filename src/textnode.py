class TextNode:
    def __init__(self, text = "", text_type = "", url = None) -> None:
        self.text = text 
        self.text_type = text_type
        self.url = url
    def __eq__(self, text_node) -> bool:
        if self.text == text_node.text \
        and self.text_type == text_node.text_type \
        and self.url == text_node.url:
            return True
        return False

    def __repr__(self) -> str:
        TEXT = self.text
        TEXT_TYPE =  self.text_type
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"