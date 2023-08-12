# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        indexOfNode = {}
        nodeOfIndex = {}

        p1 = head
        newHead = None
        p2 =None
        i = 0
        while p1!=None:
            tmpNode = RandomListNode(p1.label)
            if newHead is None:
                newHead = tmpNode
                p2 = newHead
            else:
                p2.next = tmpNode
                p2 = p2.next

            indexOfNode[p1] = i
            nodeOfIndex[i] = p2
            p1 = p1.next
            i = i+1
        p1 = head
        p2 = newHead
        i = 0
        while p1!=None:
            if p1.random is None:
                p2.random = None
            else:
                p2.random = nodeOfIndex.get(indexOfNode.get(p1.random))
            p1 = p1.next
            p2 = p2.next
        return newHead
