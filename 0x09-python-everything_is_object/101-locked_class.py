#!/usr/bin/python3

'''This module defines an empty Lockedclass
It contains 1 class ``LockedClass``
'''


class LockedClass:
    '''Defines a locked class,
    that Prevents the user from dynamically creating a new instance attribute
    Attributes:
        None
    '''
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        '''Creates a LockedClass instance'''
        self.first_name = first_name
