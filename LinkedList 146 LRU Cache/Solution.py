'''
Time Complexity:  O(1)               (for get, put as its just pointer manipulation)
Space Complexity: O(2n)              (for LinkedList + dictionary)
'''
class Node:  # doubly LinkedList with key same as in cache
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # K:key, V:Pointer to node
        self.left, self.right = Node(0, 0), Node(0, 0)  # Left: Least Recent, Right: Most Recent
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, Node):
        nodePrev, nodeNxt = Node.prev, Node.next
        nodePrev.next, nodeNxt.prev = nodeNxt, nodePrev

    def insertAtRight(self, Node):
        toBeNodePrev, toBeNodeNxt = self.right.prev, self.right
        toBeNodePrev.next = toBeNodeNxt.prev = Node
        Node.next, Node.prev = toBeNodeNxt, toBeNodePrev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # remove insert again to make it most updated
        node = self.cache[key]
        self.remove(node)
        self.insertAtRight(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)  # add in Dict
        self.insertAtRight(self.cache[key])  # add in Linkedlist

        if len(self.cache) > self.cap:
            # remove element from dict and Linkedlist
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    # Initialize with capacity = 2
    cache = LRUCache(2)
    print("Test 1:", end=" ")
    cache.put(1, 1)  # cache = {1=1}
    cache.put(2, 2)  # cache = {1=1, 2=2}
    print(cache.get(1), "expected:", 1)  # returns 1
    cache.put(3, 3)  # LRU key 2 evicted, cache = {1=1, 3=3}
    print(cache.get(2), "expected:", -1)  # not found
    cache.put(4, 4)  # LRU key 1 evicted, cache = {4=4, 3=3}
    print(cache.get(1), "expected:", -1)  # not found
    print(cache.get(3), "expected:", 3)  # returns 3
    print(cache.get(4), "expected:", 4)  # returns 4

    # Edge case: overwrite existing key
    print("\nTest 2:", end=" ")
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(1, 20)  # update value for existing key
    print(cache.get(1), "expected:", 20)  # should return updated value 20

    # Edge case: capacity = 1
    print("\nTest 3:", end=" ")
    cache = LRUCache(1)
    cache.put(5, 50)
    print(cache.get(5), "expected:", 50)  # returns 50
    cache.put(6, 60)  # evicts key 5
    print(cache.get(5), "expected:", -1)  # not found
    print(cache.get(6), "expected:", 60)  # returns 60

    # Edge case: multiple puts/get without eviction
    print("\nTest 4:", end=" ")
    cache = LRUCache(3)
    cache.put(1, 100)
    cache.put(2, 200)
    cache.put(3, 300)
    print(cache.get(2), "expected:", 200)
    print(cache.get(3), "expected:", 300)
    print(cache.get(1), "expected:", 100)

    # Stress case: check eviction order
    print("\nTest 5:", end=" ")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  # evict key 1
    print(cache.get(1), "expected:", -1)
    print(cache.get(2), "expected:", 2)
    print(cache.get(3), "expected:", 3)
