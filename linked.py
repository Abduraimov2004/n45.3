class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def check(self, data):
        if self.head is None:
            return None
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None


list_qolda = []


def tayyor() -> None:
    l_list = LinkedList()
    list_qolda = []
    for i in range(1, 11):
        list_qolda.append(i)
    l_list.head = Node(list_qolda[0])
    for j in list_qolda[1:]:
        l_list.append(j)
    l_list.printList()




def qolda():
    l_list = LinkedList()
    tugun: int = int(input("Nechta tugun yaratmoqchisiz: "))
    if tugun > 0:
        tugun_boshi: int = int(input("Tugundi boshi >>> : "))
        list_qolda.insert(0, tugun_boshi)
        while tugun > 1:
            davomi = int(input("Tugundi davomi > :"))
            list_qolda.append(davomi)
            tugun -= 1
    l_list.head = Node(list_qolda[0])
    for j in list_qolda[1:]:
        l_list.append(j)
    l_list.printList()



def q_amallar():
    l_list = LinkedList()
    if len(list_qolda) > 0:
        tanlang = input("""
        1.> Push
        2.> Insert
        3.> Append
                >>> : """)
        if tanlang == "1":
            tugun1 = int(input("Tugundi boshini ozgartrish  >>> : "))
            list_qolda.insert(0, tugun1)

            for j in list_qolda:
                l_list.append(j)
            l_list.printList()
            tanla = input("""Davom etirmoqchimisiz
            1.> Ha
            2.> Yoq
                    >>> : """)
            if tanla == "1":
                return q_amallar()
            else:
                return


        elif tanlang == "2":
            data = int(input("Tugunni kiriting: "))
            l_list.printList()
            prev_data = int(input("Qaysi tugundan kegin qoshmoqchisiz: "))
            list_qolda.insert(prev_data, data)
            for j in list_qolda:
                l_list.append(j)
            prev_node = l_list.check(prev_data)
            if prev_node is None:
                print("Oldingi tugun mavjud emas")
            else:
                l_list.insert(prev_node, data)
            l_list.printList()
            tanla = input("""Davom etirmoqchimisiz
            1.> Ha
            2.> Yoq
                    >>> : """)
            if tanla == "1":
                return q_amallar()
            else:
                return
        elif tanlang == "3":
            data = int(input("Tugunni kiriting: "))
            list_qolda.append(data)
            for j in list_qolda:
                l_list.append(j)
            l_list.printList()
            tanla = input("""Davom etirmoqchimisiz
            1.> Ha
            2.> Yoq
                    >>> : """)
            if tanla == "1":
                return q_amallar()
            else:
                return
        else:
            print("Noto'g'ri tanlov")
    else:
        print("Hozirda Data bo'sh uni toldiring")
        tanla = input("""
        1.> Qolda qoshish 
        2.> Tayyor data 
        3.> Back
                >>>> : """)

        if tanla == "1":
            return qolda(), q_amallar()
        elif tanla == "2":
            l_list = LinkedList()
            for i in range(1, 11):
                list_qolda.append(i)
            l_list.head = Node(list_qolda[0])
            for j in list_qolda[1:]:
                l_list.append(j)
            l_list.printList()
            return q_amallar()
        else:
            return


q_amallar()

