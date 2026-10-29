# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TableInterface import TableInterface


class Table(TableInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def drop(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def create(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def restore(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def backup(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def insert(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def delete(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def update(self) -> str:
        raise RuntimeError()
from org.allbinary.string.CommonStrings import CommonStrings


