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
# package views.business.context.modules.storefront.customizer.bodies.generic

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.customizer.bodies.generic.GenericBodyCustomizerView import GenericBodyCustomizerView


class InsertGenericBodyValidationView(GenericBodyCustomizerView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        requestHashMap: dict = RequestParams(self.getPageContext()).toHashMap()
        self.body = GenericBodyValidation(requestHashMap)
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        return None
    

    def isValid(self) -> bool:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Started Validation", self, self.commonStrings.IS_VALID)
            isValid: bool = self.body.isValid()
            if isValid == True:
                CustomizerUtil.getInstance().insert(self.getTransformInfoInterface(), self.body)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.body.validationInfo())
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def view(self) -> str:
        try:
            return StoreCustomizerComponentUtil.getInstance().generate(self.abeClientInformation, self.getTransformInfoInterface())
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.template.customizer.bodies.GenericBodyValidation import GenericBodyValidation
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from views.business.context.modules.storefront.customizer.CustomizerUtil import CustomizerUtil
from views.business.context.modules.storefront.customizer.StoreCustomizerComponentUtil import StoreCustomizerComponentUtil


