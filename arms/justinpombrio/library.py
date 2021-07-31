class Widget:
    """
    A marker class, to signify that any subclass obeys the interface required for a widget:
   
        getSize(self) -> (int, int)
        click(self, x, y)
        render(self)

    (Is this idiomatic Python? Probably not, but you get the idea.)
    """
    pass

class Label(Widget):
    """Just render some text on one line"""

    def __init__(self, text):
        self.text = text

    def getSize(self):
        return (len(self.text), 1)

    def click(self, x, y):
        pass

    def render(self):
        print self.text

class Vertical(Widget):
    """Stacks multiple widgets vertically"""

    def __init__(self, widgets):
        self.widgets = widgets

    def getSize(self):
        width = 0
        height = 0
        for widget in self.widgets:
            (w, h) = widget.getSize()
            width = max(width, w)
            height += h
        return (width, height)

    def render(self):
        for widget in self.widgets:
            widget.render()

    def click(self, x, y):
        # TODO: uhh coordinates, let's just click all the things for now.
        for widget in self.widgets:
            widget.click(x, y)
