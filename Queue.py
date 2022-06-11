import numpy as np

# that's file created by Asem Abdallah

'''Data struct Queue 
created from asem abdallah'''

class Queue:

    def __init__(self, rng) -> None:
        self.rng = rng

    list1 = []

    def add_to_Queue(self, argument):
        self.argument = argument
        
        if len(self.list1) < self.rng:
            Queue.list1.append(self.argument)

        else:
            Queue.list1.pop(0)
            Queue.list1.append(self.argument)

        self.arr1 = np.array(Queue.list1)

    def delete_from_Queue(self, n):

        Queue.list1.pop(n)

        self.arr1 = np.array(Queue.list1)

    def get_Queue(self):
        return self.arr1


#-------------------------------------------
# obj = Queue(3) 

# obj.add_to_Queue(11)
# obj.add_to_Queue(22)
# obj.add_to_Queue(33)
# obj.add_to_Queue(44)

# obj.delete_from_Queue(1)

# print(obj.get_Queue())
#-------------------------------------------
