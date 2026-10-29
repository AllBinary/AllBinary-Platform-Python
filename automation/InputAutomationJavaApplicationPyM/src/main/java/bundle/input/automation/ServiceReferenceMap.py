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
# package bundle.input.automation

from __future__ import annotations

# from java.util.Map import Map


class ServiceReferenceMap(Map):

    def _init_fields(self) -> None:
        self.serviceReference: ServiceReference = None
    

    def __init__(self, serviceReference: ServiceReference) -> None:
        self._init_fields()
        self.serviceReference = serviceReference
    

    def size(self) -> int:
        return -1
    

    def isEmpty(self) -> bool:
        return False
    

    def containsKey(self, key: object) -> bool:
        return False
    

    def containsValue(self, value: object) -> bool:
        return False
    

    def get(self, key: object) -> object:
        return self.serviceReference.getProperty(key)
    

    def put(self, key: object, value: object) -> object:
        return None
    

    def remove(self, key: object) -> object:
        return None
    

    def putAll(self, m: Map) -> None:
        pass
    

    def clear(self) -> None:
        pass
    

    def keySet(self) -> Set:
        keyStringArray: list[str] = self.serviceReference.getPropertyKeys()
        return None
    

    def values(self) -> Collection[object]:
        return None
    

    def entrySet(self) -> Set:
        return None
    

    @staticmethod
    def toString(map: Map) -> str:
        stringBuffer: StringMaker = StringMaker()
        return str(stringBuffer)
# from java.util.Collection import Collection
# from java.util.Set import Set
from org.osgi.framework.ServiceReference import ServiceReference
from org.allbinary.logic.string.StringMaker import StringMaker


