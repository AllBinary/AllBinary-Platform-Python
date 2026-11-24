# Generated Code Do Not Modify
# package java.util

from __future__ import annotations



#J2SE to J2ME compatibility
class Objects:
    

    @staticmethod
    def requireNonNull_j1(value: T) -> T:
        if value is None:
            raise AttributeError()
        else:
            return value
    

    @staticmethod
    def requireNonNull_j2(value: T, message: str) -> T:
        if value is None:
            raise AttributeError(message)
        else:
            return value

    @staticmethod
    def requireNonNull(*args):
        return getattr(Objects, "requireNonNull_j" + str(len(args)))(*args)


