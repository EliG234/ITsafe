
class Numbers(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def set_num4(self, num3):
        num4 = num3 + self.num1 + self.num2
        print(num4)

    def get_num4(self):
        pass
        #return num4


    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

test = Numbers(5,10)
test.set_num4(15)
print(test.get_num1())
print(test.get_num2())
print(test.get_num4())