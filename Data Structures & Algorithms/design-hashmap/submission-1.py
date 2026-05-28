class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 8
        self.elements = 0
        self.table = [None for _ in range(8)]

    def rehash(self):
        self.size *= 2
        self.elements = 0
        old_table = self.table
        self.table = [None for _ in range(self.size)]
        for chain_head in old_table:
            if chain_head:
                current_node = chain_head
                while current_node != None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next

    def put(self, key: int, value: int) -> None:
        if self.elements / self.size > 0.75:
            print("rehash triggered")
            print("size: " + str(self.size))
            print("elements: " + str(self.size))
            self.rehash()
        target_index = key % self.size
        if self.table[target_index] != None:
            current_node = self.table[target_index]
            while current_node.next != None and current_node.key != key:
                current_node = current_node.next
            #either on last node or matching node
            if current_node.key == key:
                current_node.value = value
            else:
                current_node.next = Node(key=key, value=value)
                self.elements += 1
        else:
            self.table[target_index] = Node(key=key, value=value)
            self.elements += 1

    def get(self, key: int) -> int:
        target_index = key % self.size
        if self.table[target_index] != None:
            current_node = self.table[target_index]
            while current_node.next != None and current_node.key != key:
                current_node = current_node.next
            if current_node.key == key:
                return current_node.value
        return -1

    def remove(self, key: int) -> None:
        target_index = key % self.size
        if not self.table[target_index]:
            return
        if self.table[target_index].key == key: #special case to change head pointer
            self.table[target_index] = self.table[target_index].next
        if self.table[target_index] != None:
            current_node = self.table[target_index]
            while current_node.next != None and current_node.next.key != key:
                current_node = current_node.next
            #either on last node or node before the one to remove
            if current_node.next != None: #then it's one one we want to remove
                print(key)
                print(current_node.next.key)
                current_node.next = current_node.next.next
                print(current_node.next.key)
                self.elements -= 1




                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)