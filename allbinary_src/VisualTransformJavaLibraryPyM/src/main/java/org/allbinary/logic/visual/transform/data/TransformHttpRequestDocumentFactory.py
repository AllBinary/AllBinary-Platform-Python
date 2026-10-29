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
# package org.allbinary.logic.visual.transform.data

from __future__ import annotations



class TransformHttpRequestDocumentFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(pageContext: PageContext, weblisketSession: WeblisketSession) -> TransformDocumentInterface:
        from org.allbinary.logic.visual.transform.data.TransformHttpRequestDocument import TransformHttpRequestDocument
        return TransformHttpRequestDocument(pageContext, weblisketSession)
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession


