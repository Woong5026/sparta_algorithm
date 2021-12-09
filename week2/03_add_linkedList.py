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
        # 헤드에서 인덱스 번째를 가야하는 변수
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # 인덱스 번째에 새로운 원소값을 추가하는 것 몇번째 인지도 알아야 하고 무슨 값을 넣을지도 알아야해
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0: # 0을 넣으면 -1이 되기때문에 출력값을 바꿔줘야 한다
            new_node.next = self.head
            self.head = new_node
            return
        # 다른 메소드를 불러올때는 self.을 해주면 된다, index번째 노드를 가져오겠다

        node = self.get_node(index - 1) # why -1? index번째에 넣기 위해서는 5를 가지와야 하니 -1
        # 다음 노드가 사라질 수 있기 때문에
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return "index 번째 Node 뒤에 value 를 추가하세요!"


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# 5와 12 사이에 6을 넣고싶어
linked_list.add_node(1,6)
# print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.print_all()