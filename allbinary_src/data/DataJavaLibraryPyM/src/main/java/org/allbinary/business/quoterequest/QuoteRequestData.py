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
# package org.allbinary.business.quoterequest

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class QuoteRequestData:
    instance: QuoteRequestData = None

    def _init_fields(self) -> None:
        self.ID: str = "QUOTEREQUEST_ID"
        self.PROJECT_INFO: str = "QUOTEREQUEST_PROJECT_INFO"
        self.CUSTOMER_COMMENTS: str = "QUOTEREQUEST_CUSTOMER_COMMENTS"
        self.BUDGET: str = "QUOTEREQUEST_BUDGET"
        self.TIMEFRAME: str = "QUOTEREQUEST_TIMEFRAME"
        self.COMMENTS: str = "QUOTEREQUEST_COMMENTS"
    

    @staticmethod
    def getInstance() -> QuoteRequestData:
        return QuoteRequestData.instance
    

    def __init__(self) -> None:
        self._init_fields()


def _QuoteRequestData_instance() -> object:
    return QuoteRequestData()

lazy_static(QuoteRequestData, "instance", _QuoteRequestData_instance)

