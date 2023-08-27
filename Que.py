#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mahesh
#
# Created:     15-06-2023
# Copyright:   (c) Mahesh 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Queue:
 def __init__(self):
  self.items = []
 def isEmpty(self):
  return self.items == []
 def enqueue(self,item):
  self.items.append(item)
  print(item)
 def dequeue(self):
  return self.items.pop(0)
 def front(self):
  return self.items[len(self.items)-1]
 def size(self):
  return len(self.items)
q=Queue()
print(q.isEmpty(),"- because queue is empty")
print("Enquee")
q.enqueue(15)
q.enqueue(16)
q.enqueue(17)
print("Front",q.front())
print("Dequee")
print(q.dequeue())
print(q.dequeue())
print("Size",q.size())
