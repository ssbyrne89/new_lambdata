#!/usr/bin/env python

import pandas as pd

# the first class invoked below shows how
# to call another class into your own class


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0  # a point in
        # the lecture at q&a how this
        # becomes a method even w/o
        # defining it in the __init__ method.

    def receive_upvote(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """
    general representation of animals
    """

    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = weight
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + ' is delicious, yum!'

# class below demonstrates an example
# of inheritance from another class


class Tiger(Animal):
    """Representation of tigers, a subclass of Animal"""

    def __init__(self, name, weight, diet_type, num_stripes):
        # you don't need to retype the methods from the parent class
        super().__init__(name, weight, diet_type)
        # don't call the methods like the
        # lines below (don't W.E.T.)
        # use the above super().... line instead
        # this keeps your code D.R.Y.
        # self.name = str(name)
        # self.weight = weight
        # self.diet_type = diet_type)
        self.num_stripes = num_stripes

        def say_great(self):
        return "It's GREEAAAAAT!"

    # Example of overriding
    def run(self):
        return 'Scamperwoosh!'
    pass
