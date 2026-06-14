import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def MaxValue(self):
        if self.root is None:
            return None
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.value

    def _get_all_values(self, node, values):
        if node:
            self._get_all_values(node.left, values)
            values.append(node.value)
            self._get_all_values(node.right, values)
        return values

    def AverageValue(self):
        all_data = self._get_all_values(self.root, [])
        if not all_data:
            return 0
        return sum(all_data) / len(all_data)

    def StdDevValue(self):
        all_data = self._get_all_values(self.root, [])
        n = len(all_data)
        if n < 2:
            return 0
        
        mean = sum(all_data) / n
        variance = sum((x - mean) ** 2 for x in all_data) / n
        return math.sqrt(variance)

    def reconstruct(self, value):
        values = self._get_all_values(self.root, [])
        
        if value not in values:
            return False
            
        values.remove(value)
        
        def build_balanced(sorted_list):
            if not sorted_list:
                return None
                
            mid = len(sorted_list) // 2
            node = Node(sorted_list[mid])
            node.left = build_balanced(sorted_list[:mid])
            node.right = build_balanced(sorted_list[mid+1:])
            
            return node
            
        self.root = build_balanced(values)
        return True

# Driver Code / Eksperimen
my_tree = BinarySearchTree()

data_list = [47, 21, 76, 18, 27, 52, 82]
for data in data_list:
    my_tree.insert(data)

print("\nSebelum reconstruct (hapus 76):")
print("Root:", my_tree.root.value)

my_tree.reconstruct(76)

print("\nSesudah reconstruct (hapus 76 dan balance):")
print("Root:        ", my_tree.root.value)
print("Root->left:  ", my_tree.root.left.value)
print("Root->right: ", my_tree.root.right.value)
print(f"1. Nilai Terkecil : {my_tree.min_value_node(my_tree.root).value}")
print(f"2. Nilai Terbesar : {my_tree.MaxValue()}")
print(f"3. Rata-rata      : {my_tree.AverageValue():.2f}")
print(f"4. Standar Deviasi: {my_tree.StdDevValue():.2f}")