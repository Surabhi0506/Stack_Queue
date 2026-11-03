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

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

q = queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print("Original Queue:")
q.print()

st = stack()
temp = q.front

while temp:
    st.push(Node(temp.data))
    temp = temp.next

q.front = None
q.rear = None

while not st.isempty():
    q.enqueue(st.pop())

print("Reversed Queue:")
q.print()