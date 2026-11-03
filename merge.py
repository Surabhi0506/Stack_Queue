class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

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

q1 = queue()
q2 = queue()
q3 = queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q2.enqueue(40)
q2.enqueue(50)
q2.enqueue(60)

temp = q1.front
while temp:
    q3.enqueue(temp.data)
    temp = temp.next

temp = q2.front
while temp:
    q3.enqueue(temp.data)
    temp = temp.next

print("Merged Queue:")
q3.print()