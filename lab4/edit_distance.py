from enum import Enum

class Operation(Enum):
    add = 0
    remove = 1
    sub = 2
    leave = 3

def edit_distance(s1, s2):
    print(s1, s2)
    l1, l2 = len(s1) + 1, len(s2) + 1
    
    operations = [[]] * l1
    edit = [[]] * l1
    for i in range(l1):
        edit[i] = [0] * l2
        operations[i] = [(0, 0, -1, -1)] * l2

    for j in range(l2):
        edit[0][j] = j
        operations[0][j] = (Operation.add, j - 1, -1, -1)
    for i in range(l1):
        edit[i][0] = i
        operations[i][0] = (Operation.remove, i -1, -1, -1)

    for i in range(1, l1):
        for j in range(1, l2):
            m = edit[i - 1][j] + 1
            op = (Operation.remove, i - 1, i - 1, j)

            if edit[i][j - 1] + 1 < m:
                m = edit[i][j - 1] + 1
                op = (Operation.add, (i, j - 1), i, j - 1)

            match = 0 if s1[i - 1] == s2[j - 1] else 1
            if edit[i - 1][j - 1] + match < m:
                m = edit[i - 1][j - 1] + match
                if match == 0:
                    op = (Operation.leave, i - 1, i - 1, j - 1)
                else:
                    op = (Operation.sub, (i - 1, j - 1), i - 1, j - 1)
        
            edit[i][j] = m
            operations[i][j] = op

    op_seq = []
    i, j = l1 - 1, l2 - 1
    while i >= 0 and j >= 0:
        if (operations[i][j][0] != Operation.leave 
            and not ((operations[i][j][0] == Operation.remove or operations[i][j][0] == Operation.add) and operations[i][j][1] == -1)):
            op_seq.append((operations[i][j][0], operations[i][j][1]))
        i, j = operations[i][j][2], operations[i][j][3]

    return edit[l1 - 1][l2 - 1], op_seq
