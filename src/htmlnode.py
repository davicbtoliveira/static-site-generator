class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for i in self.props.keys():
            string += f' {i}="{self.props[i]}"'
        return string

    def __repr__(self):
        return f"full: {self}\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"full: {self}\ntag: {self.tag}\nvalue: {self.value}\nprops: {self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("Missing children in ParentNode")
        for i in self.children:
            return f"<{self.tag}{self.props_to_html()}>{i.to_html()}</{self.tag}>"
