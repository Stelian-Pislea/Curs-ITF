# o clasa abstracta este o clasa care are cel putin o metoda abstracta
# o metoda abstracta este o metoda fara corp(are Pass in interior)
# o clasa abstracta NU poate fi instantiata

from abc import abstractmethod, ABC  # Abstract Base Class


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        print('ham ham!')

    def sleep(self):
        print('Zzzzzz')

class Cat(Animal):
    def sound(self):
        print('Meow')

    def sleep(self):
        print('Prrrr')

cat1 = Cat()
dog1 = Dog()

cat1.sleep()
cat1.sound()

dog1.sleep()
dog1.sound()

# a = Animal() -> EROARE pentru ca NU se paote instantia o clasa abstracta
# a.sleep()


