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
        return getattr(self, "start_j" + str(len(args)))(*args)


