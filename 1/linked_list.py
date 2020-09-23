"""
链表（1-2，P13）

线性排列的数据结构，增删数据较方便，但访问耗时。
访问数据最大（查最后的数据）时间复杂度为O(n)，添加和删除数据时间复杂度为O(1)（从到达数据位置计算）。
"""

class LinkedListItem():
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item
    
    def get_value(self):
        return self.value

    def get_next_item(self):
        return self.next_item
    
    def set_value(self, val):
        self.value = val

    def set_next_item(self, next_item):
        self.next_item = next_item

    def set_next_item_value(self, next_item_value):
        self.next_item =LinkedListItem(next_item_value)
    
    def get_item_n(self, n):
        next_item = self
        for _ in range(n):
            next_item = next_item.next_item
        return next_item
    
    def get_item_n_value(self, n):
        return self.get_item_n(n).value

    def get_all_values(self):
        val_list = []
        next_item = self
        while next_item is not None:
            val_list.append(next_item.get_value())
            next_item = next_item.get_next_item()
        return val_list
    
    def get_len(self):
        return len(self.get_all_values())
    
    def add_next_item(self, next_item_value):
        if self.next_item is None:
            self.set_next_item_value(next_item_value)
        else:
            self.next_item.add_next_item(next_item_value)
    
    def add_item(self, next_item_value):
        if self.next_item is None:
            self.set_next_item_value(next_item_value)
        else:
            self.next_item.add_next_item(next_item_value)

    def insert_item(self, value, position=None):
        if position is None:
            position = self.get_item_n(self.get_len())
        if position == 0:
            next_value = self.value
            next_2_item = self.get_next_item()
            self.value = value
            self.next_item = LinkedListItem(next_value, next_2_item)
            return 0
        else:
            insert_before = self.get_item_n(position-1)
            insert_after = insert_before.get_next_item()
            insert_before.next_item = LinkedListItem(value, insert_after)
            return 0

    def delete_item(self, position=None):
        if position is None:
            position = self.get_item_n(self.get_len()-1)
            del_before = self.get_item_n(position-1)
        elif position == 0:
            self.value = self.get_next_item()
            return 0
        else:
            del_before = self.get_item_n(position-1)
        del_after = self.get_item_n(position).get_next_item()
        del_before.set_next_item(del_after)
        return 0

# 创建链表
linked_list = LinkedListItem('Blue')
linked_list.add_next_item('Yellow')
linked_list.add_next_item('Red')

print(linked_list.get_all_values())

# 读取数据
print(linked_list.get_item_n_value(0))
print(linked_list.get_item_n_value(1))
print(linked_list.get_item_n_value(2))

# 在中间添加数据，如在Blue后添加
linked_list.insert_item('Green', 1)
print(linked_list.get_all_values())

# 删除数据
linked_list.delete_item(2)
print(linked_list.get_all_values())