class TextNode:
    def __init__(self, text = "", text_type = "", url = None) -> None:
        self.text = text 
        self.text_type = text_type
        self.url = url
    # TODO refactor to use kwargs
    def __eq__(self, textnode) -> bool:
        if self.text == textnode.text \
        and self.text_type == textnode.text_type \
        and self.url == textnode.url:
            return True
        return False

    def __repr__(self) -> str:
        TEXT = self.text
        TEXT_TYPE =  self.text_type
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"