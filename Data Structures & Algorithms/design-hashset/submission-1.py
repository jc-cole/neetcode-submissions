class MyHashSet:

    def __init__(self):
        self.table_size = 8
        self.element_count = 0
        self.table = [None for _ in range(8)]

    def rehash(self):
        old_table = self.table
        self.table_size *= 2
        self.table = [None for _ in range(self.table_size)]
        for key in old_table:
            self.add(key)

    def add(self, key_list: int) -> None:
        if not key_list:
            return
        if type(key_list) == int:
            key_list = [key_list]
        
        for key in key_list:
            if self.element_count / self.table_size > 0.75:
                self.rehash()
            target_list = self.table[key % self.table_size]
            if not target_list:
                self.table[key % self.table_size] = [key]
            elif key not in target_list:
                target_list.append(key)
                
            self.element_count += 1
        
    def remove(self, key: int) -> None:
        target_list = self.table[key % self.table_size]
        if target_list and key in target_list:
            target_list.remove(key) 
        self.element_count -= 1
        
    def contains(self, key: int) -> bool:
        target_list = self.table[key % self.table_size]
        if target_list:
            return key in target_list
        else:
            return False
    