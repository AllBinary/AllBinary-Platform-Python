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
# package org.allbinary.logic.visual.transform

from __future__ import annotations

from org.allbinary.logic.visual.transform.BasicTransformer import BasicTransformer


class ContextTransformer(BasicTransformer):
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(abeClientInformation, transformInfoInterface)
        self.setURIResolver(ContextUriResolver(self.getURIResolver()))
# from javax.xml.transform.URIResolver import URIResolver
from org.allbinary.data.tree.dom.BasicUriResolver import BasicUriResolver
from org.allbinary.data.tree.dom.ContextUriResolver import ContextUriResolver
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


