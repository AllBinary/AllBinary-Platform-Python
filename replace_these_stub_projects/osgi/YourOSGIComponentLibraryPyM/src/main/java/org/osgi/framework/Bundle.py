# Generated Code Do Not Modify
# package org.osgi.framework

from __future__ import annotations



# Java interface
class Bundle:
    

    def getSymbolicName(self) -> str:
        raise NotImplementedError()
    

    # throws BundleException
    def start(self) -> None:
        raise NotImplementedError()
    

    # throws BundleException
    # Java overloaded method: Python keeps the last definition
    def start(self, options: int) -> None:
        raise NotImplementedError()


