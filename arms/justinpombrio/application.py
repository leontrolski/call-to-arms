# Idea from "The Power of Interoperability: Why Objects Are Inevitable" by Jonathan Aldrich
#
# The intent is that the code is split in two:
# - A library that defines the Widget abstraction, and some base widgets (Label and Vertical)
# - An application that defines its own widget, and combines that widget with base widgets.
#
# Importantly, the application is written by someone *other* than the library author! So they each
# have internal details that the other shouldn't know about: the application author doesn't know the
# details of Vertical, and the library author doesn't know that there even is a Button widget.

from library import *

class Button(Widget):
    def __init__(self, label, onClick):
        self.onClick = onClick
        self.label = label

    def getSize(self):
        return (len(self.label) + 2, 1)

    def click(self, x, y):
        # TODO: coordinates
        self.onClick()

    def render(self):
        print "[" + self.label + "]"

def main():
    label = Label("World's Best App")
    def onClick():
        print "Hello world"
    button = Button("click me!", onClick)
    widget = Vertical([label, button])

    widget.render()
    # World's Best App
    # [click me!]

    print "\n-------------\n"

    print widget.getSize()
    # (16, 2)

    print "\n-------------\n"

    widget.click(0, 0)
    # Hello, world

main()
