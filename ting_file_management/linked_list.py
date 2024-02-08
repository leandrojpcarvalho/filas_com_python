class Node:
    def __init__(self, value) -> None:
        self.__preview: Node = None
        self.__next: Node = None
        self.__value = value

    def __repr__(self) -> str:
        return str(
            {
                "value": self.__value,
            }
        )

    def delete(self):
        if self.preview:
            self.preview.next = self.next
        if self.next:
            self.next.preview = self.preview
        del self

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def preview(self):
        return self.__preview

    @preview.setter
    def preview(self, preview):
        self.__preview = preview

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Linked_List:
    def __init__(self) -> None:
        self.header_node: Node = None
        self.tail_node: Node = None
        self.__length = 0

    def __str__(self) -> str:
        return str(self.__to_hash_map())

    def __len__(self):
        return self.__length

    @property
    def len(self):
        return self.__length

    def insert_first(self, value):
        new_node = Node(value)
        print(new_node)
        if self.header_node:
            new_node.next = self.header_node
            self.header_node.preview = new_node
            self.header_node = new_node
        self.__is_empty(new_node)
        self.__length += 1

    def insert_last(self, value) -> Node:
        new_node = Node(value)
        if self.tail_node:
            new_node.preview = self.tail_node
            self.tail_node.next = new_node
            self.tail_node = new_node
        self.__is_empty(new_node)
        self.__length += 1

    def __is_empty(self, new_node: Node):
        if self.__length == 0:
            self.header_node = new_node
            self.tail_node = new_node

    def insert_into(self, value, position: int):
        if (
            not isinstance(position, int)
            or position >= self.__length
            or position < 0
        ):
            raise IndexError("Índice Inválido ou Inexistente")
        new_node = Node(value)
        hashed = self.__to_hash_map()
        node_pushed = hashed[position]
        new_node.next = node_pushed
        new_node.preview = node_pushed.preview
        node_pushed.preview = new_node
        new_node.preview.next = new_node

    def delete_header(self):
        value = self.header_node.value
        self.header_node.delete()
        self.__length -= 1
        return value

    def delete_tail(self):
        value = self.tail_node.value
        self.tail_node.delete()
        self.__length -= 1
        return value

    def exist_in_list(self, value) -> bool:
        hashed = self.__to_hash_map()
        return any(
            [
                value == item.value["nome_do_arquivo"]
                for key, item in hashed.items()
            ]
        )

    def __getitem__(self, index):
        if not isinstance(index, int) or index >= self.__length or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__to_hash_map()[index]

    def __to_hash_map(self) -> dict[int, Node]:
        node = self.header_node
        hashmap = dict()
        while node is not None:
            index = len(hashmap)
            hashmap[index] = node
            node = node.next
        return hashmap
