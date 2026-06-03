class DLNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.val)

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def reset_priority(self, node_ref):
        if self.head == node_ref:
            return
        
        node_ref.prev.next = node_ref.next

        if node_ref.next:
            node_ref.next.prev = node_ref.prev
        else:
            self.tail = node_ref.prev
        
        self.push_front(node_ref)

    def push_front(self, new_node):
        if self.head:
            self.head.prev = new_node
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
        else:
            self.head = new_node
            self.tail = new_node
        
        self.size += 1
    
    def evict_last(self):
        if self.size <= 1:
            evicted = self.head
            self.head = None
            self.tail = None
        else:
            evicted = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return evicted




class LRUCache:

    def __init__(self, capacity: int):
        self.max = capacity
        self.items = 0
        self.map = {}
        self.dll = DLList()

    def get(self, key: int) -> int:
        print(f"before get: {str(self.map)}")
        if key in self.map:
            node_ref = self.map[key]
            self.dll.reset_priority(node_ref)
            return node_ref.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print(f"before put: {str(self.map)}")
        if key in self.map:
            node_ref = self.map[key]
            self.dll.reset_priority(node_ref)
            node_ref.val = value
        else:
            new_node = DLNode(key=key, val=value)
            self.dll.push_front(new_node)
            self.map[key] = new_node
            self.items += 1
            if self.items > self.max:
                evicted = self.dll.evict_last()
                del self.map[evicted.key]
                self.items -= 1
        
