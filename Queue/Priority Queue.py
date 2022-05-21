Priority Queue : A priority queue is a special type of queue in which each element is associated with a priority value. And, elements are served on the basis of their priority. That is, higher priority elements are served first. However, if elements with the same priority occur, they are served according to their order in the queue.

queue = []

class PriorityQueue:
    def enqueue(self, size):
        if len(queue) == size:
            print("Queue is full!")
        else:
            priority, element = map(int, input("Input the elements along with its priority:").split(','))
            queue.append(element)
            print(queue)

    def dequeue(self):
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            queue.pop()
            print(queue)
    
    def is_empty(self):
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            print("Queue is not empty!")

    def is_full(self, size):
        if len(queue) == size:
            print("Queue is full!")
        else:
            print("Queue is not full!")

    def peek(self):
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            print(queue[0])

    def display():
        print(queue)

queue1 = PriorityQueue()
size = int(input("Input the size of a queue : "))
print("Input the Operation:\n"
      "1 : Push\n"
      "2 : Pop\n"
      "3 : IsEmpty\n"
      "4 : IsFull\n"
      "5 : Peek\n"
      "6 : Display\n"
      "7 : Quit")

while True:
    choice = int(input("Input your choice : "))
    if choice == 1:
        queue1.enqueue(size)
    elif choice == 2:
        queue1.dequeue()
    elif choice == 3:
        queue1.isEmpty()
    elif choice == 4:
        queue1.isFull(size)
    elif choice == 5:
        queue1.peek()
    elif choice == 6:
        queue1.display()
    elif choice == 7:
        print("Quit!")
        break
    else:
        print("Invalid Operation!")
