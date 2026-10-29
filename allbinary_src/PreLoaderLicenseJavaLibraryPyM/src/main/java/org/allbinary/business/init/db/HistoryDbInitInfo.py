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
# package org.allbinary.business.init.db

from __future__ import annotations

from org.allbinary.business.init.db.DbInitInfo import DbInitInfo


class HistoryDbInitInfo(DbInitInfo):
    INITFILE: str = "historydbinitdata.dat"

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__(HistoryDbInitInfo.INITFILE, True)
    

    def _constructor1(self, read: bool) -> None:
        super().__init__(HistoryDbInitInfo.INITFILE, read)


