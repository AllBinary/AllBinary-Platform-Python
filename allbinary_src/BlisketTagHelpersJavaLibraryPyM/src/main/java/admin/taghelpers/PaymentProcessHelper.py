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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.TagHelper import TagHelper


@java_inherited_overloads
class PaymentProcessHelper(TagHelper):
    def _java_defaults(self):
        vars(self).setdefault("paymentProcessorComponent", None)

    def _init_fields(self) -> None:
        if "paymentProcessorComponent" not in vars(self): self.paymentProcessorComponent: PaymentProcessorComponent = None
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpFactory import TransformInfoHttpFactory
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from views.admin.payment.PaymentProcessorComponent import PaymentProcessorComponent
        super().__init__()
        __class__._init_fields(self)
        transformInfoInterface: TransformInfoHttpInterface = TransformInfoHttpFactory.getInstance(propertiesHashMap, pageContext)
        self.paymentProcessorComponent = PaymentProcessorComponent(transformInfoInterface)
    

    # throws Exception
    def process(self) -> str:
        return self.paymentProcessorComponent.view()
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpFactory import TransformInfoHttpFactory
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from views.admin.payment.PaymentProcessorComponent import PaymentProcessorComponent


