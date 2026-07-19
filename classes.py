class MathOperations:
    pi=3.2324
    @classmethod
    def area_of_circle(cls,radius):
        return cls.pi*(radius **2)
print(MathOperations.pi)
print(MathOperations.area_of_circle(5))

# Python program to 
# demonstrate static methods 
class Maths(): 
	
	@staticmethod
	def addNum(num1, num2): 
		return num1 + num2 
		
# Driver's code 
if __name__ == "__main__": 
	
	# Calling method of class 
	# without creating instance 
	res = Maths.addNum(1, 2) 
	print("The result is", res) 
