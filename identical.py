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

q1 = queue()
q2 = queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)

temp1 = q1.front
temp2 = q2.front
same = True

while temp1 and temp2:
    if temp1.data != temp2.data:
        same = False
        break

    temp1 = temp1.next
    temp2 = temp2.next

if temp1 or temp2:
    same = False

if same:
    print("Queues are identical")
else:
    print("Queues are not identical")