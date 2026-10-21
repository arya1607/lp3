import heapq
from collections import Counter


# Node for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    # Leaf node
    if root.char is not None:
        codes[root.char] = code if code else "0"
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)
    return codes


# Huffman Encoding
def huffman_encoding(data):
    # Count frequency of each character
    frequency = Counter(data)

    # Create a priority queue
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Build Huffman Tree using Greedy Approach
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Root of Huffman Tree
    root = heap[0]

    # Generate Huffman Codes
    codes = generate_codes(root)

    # Encode the input data
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]

    return frequency, codes, encoded_data


# Main Program
data = input("Enter the data to encode: ")

if data == "":
    print("Please enter some data.")
else:
    frequency, codes, encoded_data = huffman_encoding(data)

    print("\nCharacter Frequencies:")
    for char, freq in frequency.items():
        print(repr(char), ":", freq)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(repr(char), ":", code)

    print("\nEncoded Data:")
    print(encoded_data)
