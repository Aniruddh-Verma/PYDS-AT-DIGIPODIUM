class Animals:
      # constructor of a classs is used to make these properties 
      def __init__(self,name,age,colour,region):       # function which intializes obejects 
            self.name = name
            self.age = age
            self.colour = colour
            self.region = region
      def info(self):
            print('Animals Details')
            print('Name:' , self.name)
            print('Age:', self.age)
            print('color:', self.colour)
            print('Regions:', self.region)

o1 = Animals("fish", 2 , "silver" , "oceans")
o2 = Animals("Lion" , 5 , "yellow" , "africa")
o1.info()
o2.info()