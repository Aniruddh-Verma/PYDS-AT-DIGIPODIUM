class Cat:
      name = ""      # all these variables are known as properties of a class 
      age = 0
      fur_color = ""
      breed = ""
      
      # functions in A class are known as methods

      def eat(self):
            print("cat is eating!")

      def sleep(self):
            print('cat is sleeping!')

# creating objects 
tom = Cat()
snow = Cat()
tom.name = "Tom"
tom.age = 3
tom.fur_color = "gray"
tom.breed = "City Cat"
snow.name = "snowbell"
snow.age = 4
snow.fur_color = "white"
snow.breed = 'persian'
 

# calling methods 
tom.eat()
snow.sleep()
tom.sleep()


# distributing attributes 
print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.name, snow.fur_color,snow.age,snow.breed)
