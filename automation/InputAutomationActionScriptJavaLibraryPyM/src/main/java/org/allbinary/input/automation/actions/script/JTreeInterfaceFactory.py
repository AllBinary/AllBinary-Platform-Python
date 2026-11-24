# 
# To change this license header, choose License Headers in Project Properties. 
# To change this template file, choose Tools | Templates 
# and open the template in the editor.  
# Generated Code Do Not Modify
# package org.allbinary.input.automation.actions.script

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class JTreeInterfaceFactory:
    instance: JTreeInterfaceFactory = None

    def _init_fields(self) -> None:
        self.jTreeInterface: JTreeInterface = None

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> JTreeInterfaceFactory:
        return JTreeInterfaceFactory.instance
    

    def set(self, jTreeInterface: JTreeInterface) -> None:
        self.jTreeInterface = jTreeInterface
    

    def getJTreeInterface(self) -> JTreeInterface:
        return self.jTreeInterface


def _JTreeInterfaceFactory_instance() -> object:
    return JTreeInterfaceFactory()

lazy_static(JTreeInterfaceFactory, "instance", _JTreeInterfaceFactory_instance)

