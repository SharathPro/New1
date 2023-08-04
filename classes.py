'''class dog:
    def __init__(self,color,breed,height):
        self.color=color
        self.breed=breed
        self.height=height
    def bark(self):
        print("dog barks")
    def run(self):
        pass
    def walk(self):
        pass
obj=dog("red","dash",6)
print(obj.bark())'''

'''class dog:
    def __init__(self):
        pass
    def greeting(self):
        return "hi gdmng"
    def greet2(self):
        return  "hi gudnt"
obj=dog()
print(obj.greeting())
print(obj.greet2())'''
#2nd way
# print(dog().greeting())
# print(dog().greet2())'''

'''def morning(name):
    print("hey gdmng ----->"+str(name))
morning("releaseowl")'''

#passing parameters in functions
'''class greetings:
    def __init__(self):
        pass
    def morning(self,name):
        print("hi good morning ---->"+str(name))
    def gdevng(self):
        print("hey gdevng")
greetings().morning("bharath")'''

'''class greetings:
    def __init__(self):
        pass
    def morning(self,name):
        return "hi good morning ---->"+str(name)
    def gdevng(self):
        return "hey gdevng"
print(greetings().morning("bharath"))'''

'''class greetings:
    def __init__(self,name):
        self.name=name
    def morning(self):
        print("hi good morning----->"+str(self.name))
    def gdevng(self):
        print("hey gdevng--------->"+str(self.name))

obj=greetings("bharath").morning()
obj1=greetings("bharath").gdevng()'''