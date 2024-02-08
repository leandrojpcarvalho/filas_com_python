from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.linked_list import Linked_List


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = Linked_List()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.insert_last(value)
        return value

    def dequeue(self):
        return self.queue.delete_header()

    def search(self, index):
        return self.queue[index].value

    def search_by_value(self, value: str):
        return self.queue.exist_in_list(value)
