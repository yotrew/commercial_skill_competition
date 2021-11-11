#Ref:https://zh.wikipedia.org/wiki/%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B
class Duck:
    def quack(self):
        print("這鴨子正在嘎嘎叫")

    def feathers(self):
        print("這鴨子擁有白色和灰色的羽毛")

class Person:
    def quack(self):
        print("這人正在模仿鴨子")

    def feathers(self):
        #print("這人在地上拿起1根羽毛然後給其他人看")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()
