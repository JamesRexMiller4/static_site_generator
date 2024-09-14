from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None) -> None:
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        TAG = self.tag
        CHILDREN = self.children
        PROPS = self.props
        return f"ParentNode({TAG}, {CHILDREN}, {PROPS})"
    
    def __eq__(self, value: object) -> bool:
        if self.tag == value.tag \
        and self.children == value.children \
        and self.props == value.props:
            return True
        return False
        
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Instance has no tag value assigned")
        if self.children is None:
            raise ValueError("Instance has no children")
        child_tags = ""
        for child in self.children:
            child_tags += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_tags}</{self.tag}>"
