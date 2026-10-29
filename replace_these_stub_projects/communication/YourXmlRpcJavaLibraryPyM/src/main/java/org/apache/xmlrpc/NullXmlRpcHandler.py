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
# package org.apache.xmlrpc

from __future__ import annotations

from org.apache.xmlrpc.XmlRpcHandler import XmlRpcHandler


class NullXmlRpcHandler(XmlRpcHandler):
    NULL_XML_RPC_HANDLER: NullXmlRpcHandler = None
    

    # throws Exception
    def execute(self, method: str, params: BasicArrayList) -> object:
        return NullUtil.getInstance().NULL_OBJECT
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.NullUtil import NullUtil


NullXmlRpcHandler.NULL_XML_RPC_HANDLER = NullXmlRpcHandler()

