
class HTMLNode:

    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("[HTMLNode] to_html isn't implemented")

    def props_to_html(self):
        if self.props == None:
            return ""

        attributes = ""
        for key in self.props.keys():
            attributes += f" {key}=\"{self.props[key]}\""

        return attributes

    def __repr__(self):
        return f"tag={self.tag} value={self.value} children={self.children} props={self.props}"
    