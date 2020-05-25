"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree."""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    serialization = ""
    for item in root.__dict__.values():
        if item is None:
            serialization += "N "
        elif isinstance(item, str):
            serialization += item + " "
        elif isinstance(item, Node):
            serialization += serialize(item)
    return serialization

def deserialize(s):
    s = s.split(" ") if isinstance(s, str) else s
    n = Node(s.pop(0))
    for side in ("left", "right"):
        if s[0] == "N":
            n.__dict__[side] = None
            s.pop(0)
        else:
            n.__dict__[side] = deserialize(s)
    return n


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
