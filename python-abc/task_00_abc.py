#!/usr/bin/python3
"""
This module defines an abstract class Animal and two subclasses: Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for all animal"""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Dog class, inherits from Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class, inherits from Animal"""

    def sound(self):
        return "Meow"
