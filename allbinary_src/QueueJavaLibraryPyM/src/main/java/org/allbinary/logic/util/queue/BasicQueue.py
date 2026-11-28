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
# package org.allbinary.logic.util.queue

from __future__ import annotations

import threading


class BasicQueue:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.queueVector: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def offer(self, anyType: object) -> bool:
        with self._lock:
            return __class__.__dict__["_offer_unlocked"].__get__(self, __class__)(anyType)

    def _offer_unlocked(self, anyType: object) -> bool:
        self.queueVector.add(anyType)
        return True
    

    def remove(self, anyType: object) -> None:
        with self._lock:
            return __class__.__dict__["_remove_unlocked"].__get__(self, __class__)(anyType)

    def _remove_unlocked(self, anyType: object) -> None:
        self.queueVector.remove(anyType)
    

    def removeLast(self) -> object:
        with self._lock:
            return __class__.__dict__["_removeLast_unlocked"].__get__(self, __class__)()

    def _removeLast_unlocked(self) -> object:
        anyType: object = self.queueVector.get(self.queueVector.size() - 1)
        self.queueVector.remove(anyType)
        return anyType
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


