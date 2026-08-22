from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str | None, props: list[HTMLNode] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("[LeafNode] No Value")

        if self.tag == None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag={self.tag} value={self.value} props={self.props}"