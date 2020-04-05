class Node:
    def __init__(self, val):
        self.children = {}
        self.parent = None
        self.val = val
        self.link = None
        self.depth = 0

    def add_child(self, node):
        self.children[node.val] = node
        node.parent = self
    
    def get_child(self, val):
        return self.children[val]
    
    def contains_child(self, val):
        return val in self.children


class Trie:
    def __init__(self):
        self.root = Node(' ')

    def __up_link_down(self, leaf):
        pi = []
        while (leaf != None and leaf.link == None):
            pi.append(leaf.val)
            leaf = leaf.parent

        if leaf == None:
            return (None, None)

        head = leaf.link
        while len(pi) > 0:
            l = pi.pop()
            if not head.contains_child(l):
                break
            leaf, head = leaf.get_child(l), head.get_child(l)
            leaf.link = head
        return head, leaf

    def __graft(self, suf, head, to_link):
        for c in list(suf):
            if not head.contains_child(c):
                n = Node(c)
                n.depth = head.depth + 1
                head.add_child(n)
                n.parent = head
                head = n
            else:
                head = head.get_child(c)
            if to_link != None and to_link.contains_child(c):
                to_link = to_link.get_child(c)
                to_link.link = head
        return head

    def build(self, text):
        prev_leaf = self.__graft(text, self.root, None)
        next(iter(self.root.children.values())).link = self.root
        for i in range(1, len(text)):
            head, l = self.__up_link_down(prev_leaf)
            if head == None:
                l = self.root.get_child(text[i - 1])
                l.link = self.root
                head = self.root
            prev_leaf = self.__graft(text[i+head.depth:], head, l)
