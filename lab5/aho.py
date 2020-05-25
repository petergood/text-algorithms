class TrieNode:
    def __init__(self, char, id):
        self.children = {}
        self.parent = None
        self.is_end = False
        self.char = char
        self.link = self
        self.id = id

    def add_child(self, child):
        self.children[child.char] = child
        child.parent = self

    def get_child(self, char):
        return self.children[char]

class Trie:
    def __init__(self, strings):
        self.root = TrieNode('', 0)
        self.size = 1
        self.__build(strings)

    def __build(self, strings):
        for s in strings:
            self.__insert_string(s)

        q = [self.root]
        while q:
            node = q.pop(0)
            if node.char == '' or node.parent.char == '':
                node.link = self.root
            else:
                c = node.char
                curr = node.parent.link

                while True:
                    if c in curr.children:
                        node.link = curr.children[c]
                        break
                    if curr.char == '':
                        node.link = self.root
                        break

                    curr = curr.link
            
            for char in node.children:
                q.append(node.children[char])


    def __insert_string(self, str):
        curr = self.root

        for char in str:
            if char not in curr.children:
                n = TrieNode(char, self.size)
                self.size = self.size + 1
                curr.add_child(n)
                curr = n
            else:
                curr = curr.get_child(char)


def get_next_state(curr_node, char):
    while True:
        if char in curr_node.children:
            return curr_node.children[char]

        if curr_node.char == '':
            return curr_node #root

        curr_node = curr_node.link

def find_pattern(pattern, mat):
    cols = []
    for c in range(len(pattern[0])):
        s = ""
        for r in range(len(pattern)):
            s += pattern[r][c]
        cols.append(s)

    trie = Trie(cols)
    states = [[0] * len(mat[0]) for i in range(len(mat))]
    acc = []

    for c in range(len(pattern[0])):
        curr_node = trie.root
        for r in range(len(pattern)):
            curr_node = get_next_state(curr_node, pattern[r][c])
        acc.append(curr_node.id)

    for c in range(len(mat[0])):
        curr_node = trie.root
        for r in range(len(mat)):
            curr_node = get_next_state(curr_node, mat[r][c])
            states[r][c] = curr_node.id

    matches = []

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            match = True
            for i in range(len(acc)):
                if states[r][c + i] != acc[i]:
                    match = False
                    break
            if match:
                matches.append((r - len(pattern) + 1, c))

    return matches