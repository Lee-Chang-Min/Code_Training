class Person:

    # 생성자
    def __init__(self, name):
        self.name = name
        print("person created", self, self.name)

    def talk(self):
        print("안녕하세요 저는 ", self.name)
    
    pass


# person1 = Person("유재석")
# person1.talk()

# person2 = Person("박명수")
# person2.talk()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

node = Node(3)
print(node.data, node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
 


# linked_list = LinkedList(5)
# print(linked_list.head.data)

# linked_list.append(10)
# print(linked_list)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur
    
    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head # [7]->[5]
            self.head = new_node
            return

        prev_node = self.get_node(index - 1)
        next_node = node.next
        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next

# linked_list = LinkedList(5)
# linked_list.append(12)

# print(linked_list.get_node(0).data)

# linked_list.add_node(1,4)
# linked_list.print_all()


## 링크드 리스트 문제
def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = 0
    cur_1 = linked_list_1.head
    while cur_1 is not None:
        sum_1 = sum_1 * 10 + cur_1.data
        cur_1 = cur_1.next

    sum_2 = 0
    cur_2 = linked_list_2.head
    while cur_2 is not None:
        sum_2 = sum_2 * 10 + cur_2.data
        cur_2 = cur_2.next

    return sum_1 + sum_2



linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))

####################################################################
####################################################################
####################################################################


finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    for number in array:
        if target == number:
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True