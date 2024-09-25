class Animal:
    name = []
    alive = True #(живой)
    fed = False #(накормленный)

    def __init__(self, name): #, alive, fed):
        self.name = name  #индивидуальное название каждого животного
class Plant:
    edible = False #(съедобность)
    def __init__(self, edible, food_name, food):
        self.edible = edible
        self.food_name = food_name
        #self.food = food

class Mammal(Animal, Plant):
    food_name = []
    name = []

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')
        self.fed = True
class  Predator(Animal, Plant):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')
        self.alive = False

class Flower(Animal, Plant):
    food_name = []
    edible = False

class Fruit(Animal, Plant):
    food_name = []
    edible = True

#2 класса родителя: Animal, Plant
#Для класса Animal атрибуты alive = True(живой)
#и fed = False(накормленный), name - индивидуальное
# название каждого животного.
#Для класса Plant атрибут edible = False(съедобность),
# name - индивидуальное название каждого растения

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб,
# млекопитающее съело фрукт и насытилось.
