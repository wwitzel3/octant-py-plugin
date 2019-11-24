from component import (
    View,
    Text,
    Title,
    List,
    Link
)

def defaultView():
    view = View(Title("Python Plugin - Default"))

    links = List(Title("View List"))
    links.add(Link(" View One ", "/octant-py-plugin/view-one"))
    links.add(Link(" View Two ", "/octant-py-plugin/view-two"))
    
    view.add(links)

    return view.encode()


def viewOne():
    view = View(Title("Python Plugin - View One"))
    view.add(Text("View One"))
    return view.encode()

def viewTwo():
    view = View(Title("Python Plugin - View Two"))
    view.add(Text("View Two"))
    return view.encode()