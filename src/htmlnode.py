class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, value: object) -> bool:
        if self.tag == value.tag \
        and self.value == value.value \
        and self.children == value.children \
        and self.props == value.props:
            return True
        return False

    def __repr__(self) -> str:
        TAG = self.tag
        VALUE = self.value
        CHILDREN = self.children
        PROPS = self.props
        return f"HTMLNode({TAG}, {VALUE}, {CHILDREN}, {PROPS})"

    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        res = ""
        if self.props is None:
            return res
        for key in self.props:
            attr = f" {key}='{self.props[key]}'"
            res += attr
        return res