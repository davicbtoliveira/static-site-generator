

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ""
        for i in self.props.keys():
            string += f"{i}={self.props[i]} "
        return string

    def __repr__(self):
        return f"full: {self}\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
