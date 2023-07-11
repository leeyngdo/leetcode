class MyQueue(object):

    def __init__(self):
        self.top = None; self.size = 0
        self.queue = []
        self.ready = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ready.append(x)

        # Queue size update
        self.size += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        
        if len(self.queue) == 0:
            while self.ready:
                self.queue.append(self.ready.pop())

        item = self.queue.pop()

        # Queue size update
        self.size -= 1

        return item

    def peek(self):
        """
        :rtype: int
        """
        if self.size == 0:
            self.top = None
        elif self.queue:
            self.top = self.queue[-1]
        else:
            self.top = self.ready[0]
        return self.top

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()