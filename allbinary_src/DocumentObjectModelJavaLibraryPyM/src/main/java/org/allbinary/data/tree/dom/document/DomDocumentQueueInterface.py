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
# package org.allbinary.data.tree.dom.document

from __future__ import annotations



# Java interface
class DomDocumentQueueInterface:
    

    # throws Exception
    def offer(self, domDocumentMappingInterface: DomDocumentMappingInterface) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def remove(self) -> DomDocumentMappingInterface:
        raise NotImplementedError()
from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface


