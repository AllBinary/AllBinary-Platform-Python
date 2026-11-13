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

from java.lang.JavaRuntimeStatic import lazy_static
from org.apache.xmlrpc.XmlRpcHandler import XmlRpcHandler


class NullXmlRpcHandler(XmlRpcHandler):
    NULL_XML_RPC_HANDLER: NullXmlRpcHandler = None
    

    # throws Exception
    def execute(self, method: str, params: BasicArrayList) -> object:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.NullUtil import NullUtil
        return NullUtil.getInstance().NULL_OBJECT
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.NullUtil import NullUtil


def _NullXmlRpcHandler_NULL_XML_RPC_HANDLER() -> object:
    return NullXmlRpcHandler()

lazy_static(NullXmlRpcHandler, "NULL_XML_RPC_HANDLER", _NullXmlRpcHandler_NULL_XML_RPC_HANDLER)

