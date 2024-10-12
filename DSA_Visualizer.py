import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def visualize_array(arr):
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title('Array Visualization')
    plt.show()

def visualize_stack(stack):
    plt.barh(range(len(stack)), stack, color='lightgreen')
    plt.gca().invert_yaxis()
    plt.title('Stack Visualization')
    plt.show()

def visualize_queue(queue):
    plt.bar(range(len(queue)), queue, color='coral')
    plt.title('Queue Visualization')
    plt.show()

def visualize_linked_list(head):
    G = nx.DiGraph()
    current = head
    idx = 0

    while current:
        G.add_node(idx, label=str(current['value']))
        if current['next']:
            G.add_edge(idx, idx + 1)
        current = current['next']
        idx += 1

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color='lightblue')
    plt.title('Linked List Visualization')
    plt.show()

def visualize_tree(node, pos=None, x=0, y=0, layer=1):
    if pos is None:
        pos = {}
    pos[node['value']] = (x, y)
    if node['left']:
        pos = visualize_tree(node['left'], pos, x - 1 / layer, y - 1, layer + 1)
    if node['right']:
        pos = visualize_tree(node['right'], pos, x + 1 / layer, y - 1, layer + 1)
    return pos

def draw_tree(tree):
    G = nx.Graph()
    add_edges(tree, G)
    pos = visualize_tree(tree)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgreen')
    plt.title('Binary Tree Visualization')
    plt.show()

def add_edges(node, G):
    if node['left']:
        G.add_edge(node['value'], node['left']['value'])
        add_edges(node['left'], G)
    if node['right']:
        G.add_edge(node['value'], node['right']['value'])
        add_edges(node['right'], G)

def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            visualize_array(arr)

# Sample Data Structures for Testing

def linked_list_example():
    return {'value': 1, 'next': {'value': 2, 'next': {'value': 3, 'next': None}}}

def binary_tree_example():
    return {
        'value': 1,
        'left': {'value': 2, 'left': None, 'right': None},
        'right': {'value': 3, 'left': None, 'right': None}
    }

if __name__ == "__main__":
    print("DSA Visualizer:")
    print("1. Array\n2. Stack\n3. Queue\n4. Linked List\n5. Binary Tree\n6. Bubble Sort\n7. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            arr = [5, 3, 8, 6, 2]
            print(f"Array: {arr}")
            visualize_array(arr)

        elif choice == 2:
            stack = [10, 20, 30, 40]
            print(f"Stack: {stack}")
            visualize_stack(stack)

        elif choice == 3:
            queue = deque([1, 2, 3, 4, 5])
            print(f"Queue: {list(queue)}")
            visualize_queue(queue)

        elif choice == 4:
            head = linked_list_example()
            print("Linked List: 1 -> 2 -> 3")
            visualize_linked_list(head)

        elif choice == 5:
            tree = binary_tree_example()
            print("Binary Tree:\n    1\n   / \\ \n  2   3")
            draw_tree(tree)

        elif choice == 6:
            arr = [5, 3, 8, 6, 2]
            print(f"Original Array: {arr}")
            bubble_sort_visual(arr)
            print(f"Sorted Array: {arr}")

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
