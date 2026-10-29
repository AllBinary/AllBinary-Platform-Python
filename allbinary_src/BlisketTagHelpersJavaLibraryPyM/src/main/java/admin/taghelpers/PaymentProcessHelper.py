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

from admin.taghelpers.TagHelper import TagHelper


class PaymentProcessHelper(TagHelper):

    def _init_fields(self) -> None:
        self.paymentProcessorComponent: PaymentProcessorComponent = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        transformInfoInterface: TransformInfoHttpInterface = TransformInfoHttpFactory.getInstance(propertiesHashMap, pageContext)
        self.paymentProcessorComponent = PaymentProcessorComponent(transformInfoInterface)
    

    # throws Exception
    def process(self) -> str:
        return self.paymentProcessorComponent.view()
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.visual.transform.info.TransformInfoHttpFactory import TransformInfoHttpFactory
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from views.admin.payment.PaymentProcessorComponent import PaymentProcessorComponent


