import random
from apple import Apple

class AppleTree:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.dead = False
        self.appling = []
        
    
    def age_tree(self):
        self.age += 1
        if self.height < random.randint(17,23):
            self.height += 2
        if self.age > random.randint(20, 30):
            self.dead = True
        if self.age >= 1:
            count = random.randint(3,40)
            while count > 0:
                new_apple = Apple(random.randint(2,6))
                self.appling.append(new_apple.diameter)
                count -= 1
             
    def is_dead(self):
        if self.age > 30:
            self.dead = True
        return self.dead
        
    def any_apples(self):
        if len(self.appling) > 0:
            return True

    def pick_an_apple(self):
        return self.appling.pop()
        raise Exception('No apples on your tree')
        # Read the tests before coding.


tree1 = AppleTree()
counter = 5
while counter > 0:
    tree1.age_tree()
    counter -= 1

print(tree1.appling)
print(tree1.pick_an_apple())