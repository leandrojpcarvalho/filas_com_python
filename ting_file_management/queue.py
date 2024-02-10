from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.linked_list import Linked_List
from ting_file_management.indigent import Indigent, SearchLines


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = Linked_List()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value: Indigent):
        self.queue.insert_last(value)
        return value

    def dequeue(self):
        return self.queue.delete_header()

    def search(self, index):
        return self.queue[index].value

    def search_by_value(self, value: str):
        return self.queue.exist_in_list(value)

    def search_by_text(self, value: str, is_search=False):
        maped_hash = self.queue.hash_map
        list_word: list[SearchLines] = list()
        for index, node in maped_hash.items():
            list_word.append(node.value.find_word_at_lines(value, is_search))
        return list_word
