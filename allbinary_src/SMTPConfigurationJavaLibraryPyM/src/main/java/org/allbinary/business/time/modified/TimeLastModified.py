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
# package org.allbinary.business.time.modified

from __future__ import annotations

from org.allbinary.business.time.Time import Time


class TimeLastModified(Time):

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)
    

    def _constructor1_1(self, time: str) -> None:
        super().__init__(int(time))
    

    def _constructor1_2(self, time: int) -> None:
        super().__init__(time)


