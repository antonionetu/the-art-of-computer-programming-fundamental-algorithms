"""
[15] Imagine four railroad cars positioned on the input side of the 
track in Fig. 1, numbered 1, 2, 3, and 4, from left to right. Suppose 
we perform the following sequence of operations (which is compatible 
with the direction of the arrows in the diagram and does not require 
cars to "jump over" other cars): (a) move car 1 into the stack; (b) 
move car 2 into the stack; (c) move car 2 into the output; (d) move 
car 3 into the stack; (e) move car 4 into the stack; (f) move car 4 
into the output; (g) move car 3 into the output; (h) move car 1 into 
the output.

As a result of these operations the original order of the cars, 1234,
has been changed into 2431. It is the purpose of this exercise and the 
following exercises to examine what permutations are obtainable in such 
a manner from stacks, queues, or deques.

If there are six railroad cars numbered 123456, can they be permuted into 
the order 325641? Can they be permuted into the order 154623? (In case it 
is possible, show how to do it.)
"""

class Cars:
    def __init__(self, cars):
        self.cars = cars
        self.stack = []
        self.output = []

    def stack_car(self):
        car = self.cars.pop(0)
        self.stack.append(car)

    def unstack_car(self):
        car = self.stack.pop()
        self.output.append(car)

    def return_car(self):
        car = self.stack.pop()
        self.cars.append(car)

    def show(self):
        print(self.output)


# Case 1 (325641)
case1 = Cars([1, 2, 3, 4, 5, 6])
case1.stack_car()
case1.stack_car()
case1.stack_car()
case1.unstack_car()
case1.unstack_car()
case1.stack_car()
case1.stack_car()
case1.unstack_car()
case1.stack_car()
case1.unstack_car()
case1.unstack_car()
case1.unstack_car()
case1.show() # Possible


# Case 1 (154623)
case2 = Cars([1, 2, 3, 4, 5, 6])
case2.stack_car()
case2.unstack_car()
case2.stack_car()
case2.stack_car()
case2.stack_car()
case2.stack_car()
case2.unstack_car()
case2.unstack_car()
case2.stack_car()
case2.unstack_car()
case2.return_car()
case2.unstack_car()
case2.stack_car()
case2.unstack_car()
case2.show() # Possible with some tricks
