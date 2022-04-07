Stack : A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

There are some basic operations that allow us to perform different actions on a stack.

1. Push: Add an element to the top of a stack
2. Pop: Remove an element from the top of a stack
3. IsEmpty: Check if the stack is empty
4. IsFull: Check if the stack is full
5. Peek: Get the value of the top element without removing it

stack = []

class Stack:
    
    def push(self, size):
        if len(stack) == size:
            print("Stack is full!")
        else:
            element = int(input("Input a element : "))
            stack.append(element)
            print(stack)

    def pop(self):
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            stack.pop()
            print(stack)
    
    def isEmpty(self):
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Stack is not empty!")
    
    def isFull(self, size):
        if len(stack) == size:
            print("Stack is full!")
        else:
            print("Stack is not full!")

    def peek(self):
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print(stack[0])

    def len(self):
        if len(stack) == 0:
            print("Stack is full!")
        else:
            length = 0
            for i in stack:
                length += 1
            print(length)

    def max(self):
        if len(stack) == 0:
            print("Stack is full!")
        else:
            max = stack[0]
            for i in stack:
                if i > max:
                    max = i
            print(max)

    def min(self):
        if len(stack) == 0:
            print("Stack is full!")
        else:
            min = stack[0]
            for i in stack:
                if i < min:
                    min = i
            print(min)
        
    def sum(self):
        if len(stack) == 0:
            print("Queue is full!")
        else:
            sum = 0
            for i in stack:
                sum += i
            print(sum)

    def product(self):
        if len(stack) == 0:
            print("Stack is full!")
        else:
            ctr = 1
            for i in stack:
                ctr *= i
            print(ctr)


stack1 = Stack()
size = int(input("Input the size of a stack : "))
print("Input the operation : \n"
      "1 : Push\n"
      "2 : Pop\n"
      "3 : IsEmpty\n"
      "4 : IsFull\n"
      "5 : Peek\n"
      "6 : Length\n"
      "7 : Max\n"
      "8 : Min\n"
      "9 : Sum\n"
      "10 : Product\n"
      "11 : Quit")

while True:
    choice = int(input("Input your choice : "))
    if choice == 1:
        stack1.push(size)
    elif choice == 2:
        stack1.pop()
    elif choice == 3:
        stack1.isEmpty()
    elif choice == 4:
        stack1.isFull(size)
    elif choice == 5:
        stack1.peek()
    elif choice == 6:
        stack1.len()
    elif choice == 7:
        stack1.max()
    elif choice == 8:
        stack1.min()
    elif choice == 9:
        stack1.sum()
    elif choice == 10:
        stack1.product()
    elif choice == 11:
        print("Quit!")
        break
    else:
        print("Invalid Operation!")
