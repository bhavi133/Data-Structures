Queue : A queue is a linear data structure that follows the principle of First In First Out (FIFO). This means the item that goes in first is the item that comes out first.
In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

Basic Operations of Queue

A queue is an object (an abstract data structure - ADT) that allows the following operations:
  
1. Enqueue: Add an element to the end of the queue
2. Dequeue: Remove an element from the front of the queue
3. IsEmpty: Check if the queue is empty
4. IsFull: Check if the queue is full
5. Peek: Get the value of the front of the queue without removing it
  
import collections

queue = collections.deque()

class Queue:
    def enqueue(self, size):
        if len(queue) == size:
            print("Queue is full!")
        else:
            element = int(input("Input a element : "))
            queue.append(element)
            print(queue)

    def dequeue(self):
        if len(queue) == 0:
            print("Queue is full!")
        else:
            queue.pop()
            print(queue)

    def peek(self):
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            print(queue[0])

    def isEmpty(self):
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            print("Queue is not empty!")
    
    def isFull(self, size):
        if len(queue) == size:
            print("Queue is full!")
        else:
            print("Queue is not full!")

    def len(self):
        if len(queue) == 0:
            print("Queue is full!")
        else:
            length = 0
            for i in queue:
                length += 1
            print(length)

    def max(self):
        if len(queue) == 0:
            print("Queue is full!")
        else:
            max = queue[0]
            for i in queue:
                if i > max:
                    max = i
            print(max)
        
    def min(self):
        if len(queue) == 0:
            print("Queue is full!")
        else:
            min = queue[0]
            for i in queue:
                if i < min:
                    min = i
            print(min)

    def sum(self):
        if len(queue) == 0:
            print("Queue is full!")
        else:
            sum = 0
            for i in queue:
                sum += i
            print(sum)

    def product(self):
        if len(queue) == 0:
            print("Queue is full!")
        else:
            ctr = 1
            for i in queue:
                ctr *= i
            print(ctr)


queue1 = Queue()
size = int(input("Input the size of a queue : "))
print("Input the operation : \n"
      "1 : Push\n"
      "2 : Pop\n"
      "3 : Peek\n"
      "4 : IsEmpty\n"
      "5 : IsFull\n"
      "6 : Length\n"
      "7 : Max\n"
      "8 : Min\n"
      "9 : Sum\n"
      "10 : Product\n"
      "11 : Quit")

while True:
    choice = int(input("Input your choice : "))
    if choice == 1:
        queue1.enqueue(size)
    elif choice == 2:
        queue1.dequeue()
    elif choice == 3:
        queue1.peek()
    elif choice == 4:
        queue1.isEmpty()
    elif choice == 5:
        queue1.isFull(size)
    elif choice == 6:
        queue1.len()
    elif choice == 7:
        queue1.max()
    elif choice == 8:
        queue1.min()
    elif choice == 9:
        queue1.sum()
    elif choice == 10:
        queue1.product()
    elif choice == 11:
        print("Quit!")
        break
    else:
        print("Invalid Operation!")
