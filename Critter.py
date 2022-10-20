class Critter(object):
    """"Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        print("В мире появился зверь по имени ", self.name)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "estupendo"
        elif 5 <= unhappiness <= 10:
            m = "bien"
        elif 11 <= unhappiness <= 15:
            m = "no muy bien"
        else:
            m = "fatal"
        return m

    def talk(self):
        print("Me llamo", self.name, "y ahora me siento", self.mood, "\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Mrrr. Gracias *_*")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Jajaja")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        words = "Это зверюшка по имени " + self.name + "\n" + "Сейчас она чувствует себя " + self.mood
        return words


def main():
    crit_name = input("Какое имя ты дашь зверюшке? ")
    crit = Critter(crit_name)
    choice = None
    while choice != '0':
        print("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать настроение зверюшки
        2 - Покормить зверюшку
        3 = Поиграть со зверюшкой
        """)
        # exit
        choice = input()
        if choice == '0':
            print("Adios")
        # talking with crit
        elif choice == '1':
            crit.talk()
        # feeding crit
        elif choice == '2':
            crit.eat()
        # jugar con animal
        elif choice == '3':
            crit.play()
        # if was written some shit
        else:
            print("Escucha me, puta. Alli no hay este punto ", choice)


main()
input("\n\nНажмите Enter, чтобы покинуть зверей")
