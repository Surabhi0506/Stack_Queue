class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data

st = stack()

s = input("Enter a string: ")

for ch in s:
    st.push(Node(ch))

rev = ""

while not st.isempty():
    rev = rev + st.pop()

print("Reversed String:", rev)