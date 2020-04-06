class Node:
    def __init__(self, start, stop, string, label = True):
        self.start = start
        self.stop = stop
        self.children = {}
        self.string = string
        self.parent = None
        self.label = label

    def get_val(self):
        if self.label:
            if self.start == self.stop:
                return self.string[self.start]
            return "[" + str(self.start) + ";" + str(self.stop) + "]"
        return ""

    def contains_child(self, first_char):
        return first_char in self.children

    def get_child(self, first_char):
        return self.children[first_char]

    def add_child(self, n):
        self.children[self.string[n.start]] = n

    def remove_child(self, n):
        del self.children[self.string[n.start]]

    def slowfind(self, p, offset = 0):
        if len(p) == 0 or not self.contains_child(p[0]):
            return self, offset
        child = self.get_child(p[0])
        j = 0
        for i in range(child.start, child.stop + 1):
            if self.string[i] != p[j]:
                return child.break_path(i - 1), offset + j
            j = j + 1
        return child.slowfind(p[j:], offset + child.stop - child.start + 1)

    def break_path(self, i):
        n = Node(self.start, i, self.string)
        parent = self.parent
        parent.remove_child(self)
        self.start = i + 1
        self.parent = n
        n.add_child(self)
        parent.add_child(n)
        n.parent = parent
        return n

    def graft(self, start, stop):
        n = Node(start, stop, self.string)
        n.parent = self
        self.add_child(n)

def build(text):
    root = Node(0, 0, text, False)
    root.graft(0, len(text) - 1)
    for i in range(1, len(text)):
        t = text[i:]
        head, offset = root.slowfind(t)
        head.graft(i + offset, len(text) - 1)

    return root


build("abcbccd")