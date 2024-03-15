class TextNode:
    text = ""
    text_type = ""
    url = ""

    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, comp_node):
        return self.text == comp_node.text and self.text_type == comp_node.text_type and self.url == comp_node.url
    
    def repr(self):
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")

