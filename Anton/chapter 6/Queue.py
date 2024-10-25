class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def enqueue(self, item, priority=5):
        self.items.append([item,priority])
        return self.items
    def dequeue(self):
        i1=0
        for i,j in self.items:
            if j==0:
                return self.items.pop(i1)
            i1 += 1
    def front(self):
        if len(self.items)==0:
            print("в масиве нет чисел")
        else:
            return self.items[0]
    def size(self):
        return len(self.items)

    def sort_queue(self):
        i1=0
        for i,j in self.items:
            self.items[i1]=[j,i]
            i1+=1
        self.items=sorted(self.items)
        i1 = 0
        for i, j in self.items:
            self.items[i1] = [j,i]
            i1 += 1
        return self.items

# Example usage:
my_queue = Queue()

my_queue.enqueue(1, priority=2)
my_queue.enqueue(2, priority=5)
my_queue.enqueue(3, priority=0)

print("Queue:", my_queue.items)

# Dequeue an item from the queue
dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)

# Get the front of the queue
front_item = my_queue.front()
print("Front item:", front_item)

# Enqueue a new item with priority
my_queue.enqueue(4, priority=3)
print("Queue after enqueue:", my_queue.items)

# Check if the queue is empty
print("Is queue empty?", my_queue.is_empty())

# Get the size of the queue
print("Queue size:", my_queue.size())
print("sort_queue:", my_queue.sort_queue())

