from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props

    def __repr__(self) -> str:
        TAG = self.tag
        VALUE = self.value
        PROPS = self.props
        return f"LeafNode({TAG}, {VALUE}, {PROPS})"
    
    def __eq__(self, value: object) -> bool:
        if self.tag == value.tag \
        and self.value == value.value \
        and self.props == value.props:
            return True
        return False
    
    def to_html(self) -> str:
        if self.value is None:
            return ValueError
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def props_to_html(self) -> str:
        return super().props_to_html()