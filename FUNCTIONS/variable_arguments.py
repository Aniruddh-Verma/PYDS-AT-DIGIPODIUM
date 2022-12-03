# flexible paramenters in a functions 4
# *args , **kwargs
def mean(*numbers):
      total = 0 
      for item in numbers:
            if isinstance(item,(int,float)):
                  total +=item
      return total / len(numbers)

def report(**marks):
      total_marks = 0
      for k,v in marks.items():
            print(f'{k} got {v} marks')
            total_marks += v
      return total_marks

print(report(ram=90,shyam=70,hari=85))
print(mean(1,2,3,4,5,6,7))
print(mean(23,34,5,56,67,87,121,12))
print(mean(12,'a',123,'123',123,12))
