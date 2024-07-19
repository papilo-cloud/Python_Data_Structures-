import queues

class PrintManager:
    def __init__(self):
        self.queue = queues.Queue()
    def queue_print_job(self, document):
        self.queue.enqueue(document)
    def run(self):
        while self.queue.peek():
            print(self.queue.dequeue())
       
print_manager = PrintManager() 

print_manager.queue_print_job('First Document')
print_manager.queue_print_job('Second Document')
print_manager.queue_print_job('Third Document')

print(print_manager.run())