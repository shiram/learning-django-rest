class Queue:
    
    def __init__(self):
        self.queue = list()

    def joinQueue(self, dataval):
        #Use insert list method to add data.
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    def queueSize(self):
        return len(self.queue)

    def offQueue(self):
        if self.queueSize() > 0:
            return self.queue.pop()
        return ("No Elements in Queue!")

class Dequeue(Queue):

    def joinQueueRight(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(self.queueSize() + 1, dataval)
            return True
        return False

    def offQueueLeft(self):
        if self.queueSize() > 0:
            return self.queue.pop(0)
        return ("No Elements in Queue!")

qTest = Queue()
qTest.joinQueue("Mon")
qTest.joinQueue("Tue")
qTest.joinQueue("Wed")


print(qTest.queueSize())
print(qTest.offQueue())
print(qTest.offQueue())
print(qTest.queueSize())

dqTest = Dequeue()
dqTest.joinQueue("Sun")
dqTest.joinQueueRight("Sat")
dqTest.joinQueue("Mon")
dqTest.joinQueueRight("Thur")
dqTest.joinQueue("Wed")

print(dqTest.queue)

print("The D Queue")
print(dqTest.queueSize())
print(dqTest.offQueue())
print(dqTest.queueSize())