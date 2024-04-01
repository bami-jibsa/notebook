# mom = False

# if mom:
#     feed = True
# else:
#     feed = False

# if feed:
#     print('바미가 밥을 먹는다.')
# else:
#     print('바미가 굶는다')
    

# import sys 

# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end='')

# result = 0
# result1 = 0

# def add(num):
#     global result
#     result += num
#     return result

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# print(add(3))
# print(add(4))
# print(add1(3))

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def add(self, num):
#         self.result += num
#         return self.result
#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()
# caal2 = Calculator()

# print(cal1.add(3))
# print(cal1.sub(1))

# print(caal2.add(3))
# print(caal2.sub(6))


# class experiment:
#     pass

# experiment1 = experiment()
# print(experiment1)

class experiment:
    def __init__(self):
        self.result = 0
    def setdata(self, first, secend):
        self.first = first
        self.secend = secend
    def add(self):
        self.result =  self.first + self.secend
        return self.result

a = experiment()
a.setdata(3, 4)
print(a.result)




























































































































































