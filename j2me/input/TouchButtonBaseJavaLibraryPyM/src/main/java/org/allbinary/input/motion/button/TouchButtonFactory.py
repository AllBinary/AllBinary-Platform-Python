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
# package org.allbinary.input.motion.button

from __future__ import annotations

import threading


class TouchButtonFactory:
    SINGLETON: TouchButtonFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.LIST: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.list_: BasicArrayList = self.LIST
        self.savedList: BasicArrayList = self.LIST
        self.saved: bool = False
    

    @staticmethod
    def getInstance() -> TouchButtonFactory:
        return TouchButtonFactory.SINGLETON
    

    def __init__(self) -> None:
        self._init_fields()
    

    def defaultList(self) -> None:
        self.list_ = self.LIST
        self.toggle(False, self.LIST)
    

    def toggle(self, save: bool, list_: BasicArrayList) -> None:
        with self._lock:
            return self._toggle_unlocked(save, list_)

    def _toggle_unlocked(self, save: bool, list_: BasicArrayList) -> None:
        if list_ != BasicArrayListUtil.getInstance().getImmutableInstance():
            self.savedList = list_
            if not self.saved:
                self.list_ = self.savedList
        else:
            if save:
                if not self.saved:
                    self.saved = True
                    self.savedList = self.list_
                    self.list_ = self.LIST
                else:
                    pass
            else:
                self.list_ = self.savedList
                self.saved = False
    

    # throws Exception
    def setList(self, list_: BasicArrayList) -> None:
        if list_ is None:
            raise Exception("Null List")
        self.list_ = list_
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


TouchButtonFactory.SINGLETON = TouchButtonFactory()

