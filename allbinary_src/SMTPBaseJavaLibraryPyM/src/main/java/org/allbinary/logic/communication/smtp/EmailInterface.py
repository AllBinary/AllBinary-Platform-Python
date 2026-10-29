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
# package org.allbinary.logic.communication.smtp

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface


# Java interface
class EmailInterface(DomNodeInterface, DomDocumentMappingInterface):
    

    def getDebugInfo(self) -> str:
        raise NotImplementedError()
    

    def getMimeMessage(self) -> MimeMessage:
        raise NotImplementedError()
    

    # throws Exception
    def log(self) -> str:
        raise NotImplementedError()
# from javax.mail.internet.MimeMessage import MimeMessage


