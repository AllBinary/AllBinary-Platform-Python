#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.logic.java.proxy

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.reflect.InvocationHandler import InvocationHandler


class InterfaceCastProxy(InvocationHandler):

    def _init_fields(self) -> None:
        if "anyType" not in vars(self): self.anyType: object = None
    

    def __init__(self, anyType: object) -> None:
        __class__._init_fields(self)
        self.anyType = anyType
    

    @staticmethod
    def newInstance(anyType: object) -> object:
        return Proxy.newProxyInstance(__import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.getSystemClassLoader(), type(anyType).getInterfaces(), InterfaceCastProxy(anyType))
    

    # throws Throwable
    def invoke(self, proxyObject: object, proxyMethod: Method, proxyArgs: list[object]) -> object:
        methodName: str = proxyMethod.getName()
        realMethod: Method = type(self.anyType).getMethod(methodName, proxyMethod.getParameterTypes())
        if not (java_predicate(realMethod, "isAccessible")):
            realMethod.setAccessible(True)
        return proxyMethod.invoke(self.anyType, proxyArgs)
# from java.lang.reflect.Method import Method
# from java.lang.reflect.Proxy import Proxy


