"""

提供链表类(Linked_list_demo)
提供add, append, insert, remove, get_list方法
"""


# 创建单个节点类
class Node:
    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next_node = next_node

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def set_next_node(self, next_node):
        self._next_node = next_node

    def get_next_node(self):
        return self._next_node


# 链表类
class Linked_list_demo:
    def __init__(self):
        self._head = Node()
        self._end = None
        self._len = 0

    # 重写长度函数
    def __len__(self):
        count = 0
        current = self._head
        while current.get_next_node() is not None:
            count += 1
            current = current.get_next_node()
        else:
            return count

    # 判断是否为空
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    # 尾部增加一个元素
    def append(self, new_value):
        if self.is_empty():
            self._head.set_next_node(Node(new_value, None))
        else:
            new_node = Node(new_value, None)
            current = self._head
            while current.get_next_node() is not None:
                current = current.get_next_node()
            else:
                current.set_next_node(new_node)

    # 头部增加一个元素
    def add(self, value):
        if self.is_empty():
            self._head.set_next_node(Node(value, None))
        else:
            new_node = Node(value, self._head.get_next_node())
            self._head.set_next_node(new_node)

    # 遍历链表并打印
    def get_list(self):
        current = self._head
        while current.get_next_node() is not None:
            if current.get_value() is not None:
                print(current.get_value())
                current = current.get_next_node()
            else:
                current = current.get_next_node()
        else:
            print(current.get_value())

    # 移除在num位置的元素
    def remove(self, number):
        current = self._head
        count = 0
        while current.get_next_node() is not None:
            if count == number:
                if current.get_next_node().get_next_node() is None:
                    current.set_next_node(None)
                else:
                    current.set_next_node(current.get_next_node().get_next_node())
                return 1
            count += 1
            current = current.get_next_node()
        return -1

    # 在num位置增加一个元素
    def insert(self, number, value):
        if 0 <= number <= len(self):
            current = self._head
            count = 0
            while count < number:
                count += 1
                current = current.get_next_node()
            temp = current.get_next_node()
            current.set_next_node(Node(value, temp))
        else:
            return -1

# newList = Linked_list_demo()
# newList.append(3)
# newList.append(4)
# newList.append(5)
# newList.add(1)
# newList.remove(3)
# newList.insert(1, 2)
# newList.get_list()
# print('---------------------')
# newList.get_list()
# print(len(newList))
