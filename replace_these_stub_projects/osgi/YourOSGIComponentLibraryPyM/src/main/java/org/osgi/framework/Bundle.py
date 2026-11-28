# Generated Code Do Not Modify
# package org.osgi.framework

from __future__ import annotations



# Java interface
class Bundle:
    

    def getSymbolicName(self) -> str:
        raise NotImplementedError()
    

    # throws BundleException
    def start_j0(self) -> None:
        raise NotImplementedError()
    

    # throws BundleException
    def start_j1(self, options: int) -> None:
        raise NotImplementedError()

    def start(self, *args):
        implementation = __class__.__dict__.get("start_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().start(*args)


