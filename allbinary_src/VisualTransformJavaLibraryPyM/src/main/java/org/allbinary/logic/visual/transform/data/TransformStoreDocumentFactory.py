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



class TransformStoreDocumentFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance_j2(pageContext: PageContext, weblisketSession: WeblisketSession) -> TransformDocumentInterface:
        from org.allbinary.logic.visual.transform.data.TransformStoreDocument import TransformStoreDocument
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        return TransformStoreDocument(pageContext, weblisketSession)
    

    # throws Exception
    @staticmethod
    def getInstance_j1(searchRequest: SearchRequest) -> TransformDocumentInterface:
        from org.allbinary.logic.visual.transform.data.TransformStoreDocument import TransformStoreDocument
        from org.allbinary.logic.control.search.SearchRequest import SearchRequest
        return TransformStoreDocument(searchRequest)

    @staticmethod
    def getInstance(*args):
        return getattr(TransformStoreDocumentFactory, "getInstance_j" + str(len(args)))(*args)
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.control.search.SearchRequest import SearchRequest


