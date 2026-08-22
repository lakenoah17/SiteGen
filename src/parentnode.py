from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("[ParentNode] No Tag")

        if self.children == None:
            raise ValueError("[ParentNode] No Children")

        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html
    