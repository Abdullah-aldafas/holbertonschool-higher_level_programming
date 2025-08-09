#!/usr/bin/python3


class Fish:
    """Represents a fish with swimming ability and a water habitat."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("“The fish lives in water")


class Bird:
    """Represents a bird with flying ability and a sky habitat."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A creature that can both swim and fly, living in water and the sky."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
