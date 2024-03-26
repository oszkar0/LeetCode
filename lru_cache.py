class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = dict()
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.val
        else:
            return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            node = self.dict[key] 
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.val = value
        else:
            if len(self.dict) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dict[key] = node
            self.insertIntoHead(node)

        
    def removeFromTail(self):
        if len(self.dict) == 0: return
        node = self.tail.prev
        del self.dict[node.key]
        self.removeFromList(node)

    def removeFromList(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def insertIntoHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)