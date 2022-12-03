import random
# class subclass(super_classs)
class Mylist(list):       # inherits from list class
      def shuffle(self):
            random.shuffle(self)
      def get_random(self):
            return random.choice(self)
      



# object 
a = Mylist([12,121,23,32,45,67,322,345,646])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list =",a.get_random())



