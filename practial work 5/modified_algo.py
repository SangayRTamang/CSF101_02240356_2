# Stack class definition for all stack-based operations
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

# Queue class definition for all queue-based operations
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")

# Function to evaluate postfix expressions using a stack
def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():  # Operand
            stack.push(int(token))
        else:  # Operator
            right = stack.pop()
            left = stack.pop()
            result = eval(f"{left}{token}{right}")
            stack.push(result)
    return stack.pop()

# Test Postfix Evaluation
print("Postfix Evaluation:", evaluate_postfix("3 4 + 2 * 7 /"))  # Expected output: 2.0


# Queue implemented with two stacks
class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, item):
        self.stack_in.push(item)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if not self.stack_out.is_empty():
            return self.stack_out.pop()
        raise IndexError("Queue is empty")

# Test QueueWithTwoStacks
queue_two_stacks = QueueWithTwoStacks()
queue_two_stacks.enqueue(1)
queue_two_stacks.enqueue(2)
queue_two_stacks.enqueue(3)
print("Queue With Two Stacks Dequeue:", queue_two_stacks.dequeue())  # Expected output: 1


# Task Scheduler using a Queue
def task_scheduler(tasks):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)
    
    while not queue.is_empty():
        print(f"Processing task: {queue.dequeue()}")

# Test Task Scheduler
tasks = ["Task 1", "Task 2", "Task 3"]
task_scheduler(tasks)  # Expected: Processing each task in order


# Infix to Postfix conversion using a stack
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = Stack()
    postfix = []

    for token in expression.split():
        if token.isdigit():  # Operand
            postfix.append(token)
        elif token == '(':  # Left Parenthesis
            stack.push(token)
        elif token == ')':  # Right Parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard '('
        else:  # Operator
            while not stack.is_empty() and precedence[stack.peek()] >= precedence[token]:
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():  # Remaining operators
        postfix.append(stack.pop())

    return " ".join(postfix)

# Test Infix to Postfix Conversion
print("Infix to Postfix:", infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  # Expected output: "3 4 2 * 1 5 - / +"
