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
# package admin.taghelpers

from __future__ import annotations



# Java interface
class BasicTableInterface:
    

    # throws Exception
    def drop(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def create(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def restore(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def backup(self) -> str:
        raise NotImplementedError()


