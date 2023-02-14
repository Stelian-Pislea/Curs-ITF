"""
Factory Method

Factory Method is a Creational Design Pattern that allows an interface
or a class to create an object, but lets subclasses decide which class or object
to instantiate. Using the Factory method, we have the best ways to create an object.
Here, objects are created without exposing the logic to the client, and for creating
the new type of object, the client uses the same common interface.

PRO:
    * We can easily add new types of products without disturbing the existing client code.
    * Generally, tight coupling is being avoided between the products and the creator classes and objects.
CONS
    * To create a particular concrete product object, the client might have to sub-class the creator class.
    * You end up with a huge number of small files i.e, cluttering the files.
"""
# LINK https://www.youtube.com/watch?v=-a1PFtooGo4&t=165s
# LINK https://www.youtube.com/watch?v=s_4ZrtQs8Do

# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))


"""
Facade Design Pattern
The Facade Pattern is a structural design pattern. 
It provides a simplified interface to a set of other interfaces, 
abstractions and implementations within a system that may be full 
of complexity and/or tightly coupled.

PRO

    Façade method helps us to isolate our code from the complexity of a subsystem.
    It provides the loose coupling between the client and the subsystems.
    It makes the testing process easy since it contains convenient methods for common testing task.
CONS

    Applying the façade method is expensing. It is not cheap to establish 
    façade method for system reliability.
    Façade method violates can violates the construction of the façade layer.
    Façade object can become a supreme object coupled to all classes of an app.
    If we make the change in the subsequent method, that may bring change 
    in the Façade method which is not acceptable.
"""

# LINK  https://www.youtube.com/watch?v=VrRDami28N0
# LINK  https://www.youtube.com/watch?v=bn8Pc1VZowI



class SubSystemClassA:
    @staticmethod
    def method():
        return "A"


class SubSystemClassB:
    @staticmethod
    def method():
        return "B"


class SubSystemClassC:
    @staticmethod
    def method():
        return "C"


# facade
class Facade:
    def __init__(self):
        self.sub_system_class_a = SubSystemClassA()
        self.sub_system_class_b = SubSystemClassB()
        self.sub_system_class_c = SubSystemClassC()

    def create(self):
        result = self.sub_system_class_a.method()
        result += self.sub_system_class_b.method()
        result += self.sub_system_class_c.method()
        return result


# client
FACADE = Facade()
RESULT = FACADE.create()
print("The Result = %s" % RESULT)



"""
State Pattern
Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.

PRO
    Open/Closed Principle: We can easily introduce the new states without changing 
    the content of existing states of client’s code.
    Single Responsibility Principle: It helps in organizing the code of particular 
    states into the separate classes which helps in making the code feasible for the other developers too.
    Improves Cohesion: It also improves the Cohesion since state-specific behaviors 
    are aggregated into the ConcreteState classes, which are placed in one location in the code.
    
CONS
    Making System complex: If a system has only a few number of states, 
    then its not a good choice to use the State Method as you will end up with adding unnecessary code.
    Changing states at run-time: State method is used when we need to change the state 
    at run-time by inputting at different sub-classes, this will be considered as a 
    disadvantage as well because we have a clear separate State classes with some logic 
    and from the other hand the number of classes grows up.
    Sub-Classes Dependencies: Here the each state derived class is coupled to its sibling, 
    which directly or indirectly introduces the dependencies between sub-classes.
"""

#LINK  https://www.youtube.com/watch?v=8rynRTOr4mE

import abc


class Context:
    """
    Define the interface of interest to clients.
    Maintain an instance of a ConcreteState subclass that defines the
    current state.
    """

    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()


class State(metaclass=abc.ABCMeta):
    """
    Define an interface for encapsulating the behavior associated with a
    particular state of the Context.
    """

    @abc.abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    """
    Implement a behavior associated with a state of the Context.
    """

    def handle(self):
        pass


class ConcreteStateB(State):
    """
    Implement a behavior associated with a state of the Context.
    """

    def handle(self):
        pass


def main():
    concrete_state_a = ConcreteStateA()
    context = Context(concrete_state_a)
    context.request()


if __name__ == "__main__":
    main()