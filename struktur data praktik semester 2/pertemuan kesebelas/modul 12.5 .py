# Node untuk Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List
class LinkedList:
    def __init__(self):
        self.head = None


    # Menambahkan data
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node


    # Ascending Linked List
    def asc_linked_list(self):
        current = self.head

        while current:
            index = current.next

            while index:
                if current.data > index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp

                index = index.next

            current = current.next


    # Descending Linked List
    def desc_linked_list(self):
        current = self.head

        while current:
            index = current.next

            while index:
                if current.data < index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp

                index = index.next

            current = current.next


    # Menampilkan Linked List
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Membuat objek Linked List
data = LinkedList()

# Menambahkan data
data.append(15)
data.append(9)
data.append(27)
data.append(4)
data.append(18)
data.append(11)

# Menampilkan data awal
print("Data Awal")
data.display()

print()

# Ascending
print("Ascending Linked List")
data.asc_linked_list()
data.display()

print()

# Descending
print("Descending Linked List")
data.desc_linked_list()
data.display()