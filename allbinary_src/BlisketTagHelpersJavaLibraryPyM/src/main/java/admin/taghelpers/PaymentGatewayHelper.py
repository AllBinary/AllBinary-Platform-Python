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

from admin.taghelpers.BasicTable import BasicTable


class PaymentGatewayHelper(BasicTable):

    def _init_fields(self) -> None:
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.httpServletRequest: HttpServletRequest = None
        self.portion: Portion = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        self._init_fields()
        try:
            self.weblisketSession = WeblisketSession(hashMap, pageContext)
            self.httpServletRequest = pageContext.getRequest()
            self.portion = Portion(hashMap)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENTERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    def insert(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactory import PaymentGatewayInterfaceFactory
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentGatewayInterface: PaymentGatewayInterface = PaymentGatewayInterfaceFactory().getInstance(self.httpServletRequest)
            paymentGatewayInterface.setStoreName(self.weblisketSession.getStoreName())
            PaymentGatewayEntityFactory.getInstance().add(paymentGatewayInterface)
            success: str = "Successfully Added New Payment Gateway"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success + "<br/>"
        except Exception as e:
            error: str = "Failed to add"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error + "<br>" + "Exception: " + str(e) + "<br>"
    

    def update(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactory import PaymentGatewayInterfaceFactory
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentGatewayInterface: PaymentGatewayInterface = PaymentGatewayInterfaceFactory().getInstance(self.httpServletRequest)
            paymentGatewayInterface.setStoreName(self.weblisketSession.getStoreName())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Gateway Name: ")
                stringBuffer.append(paymentGatewayInterface.getName())
                stringBuffer.append(" HashMap=")
                stringBuffer.append(str(paymentGatewayInterface.toHashMap(True)))
                self.logUtil.putF(str(stringBuffer), self, "update()")
            PaymentGatewayEntityFactory.getInstance().update(paymentGatewayInterface)
            success: str = "Successfully Updated Payment Gateway information"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success + "<br/>"
        except Exception as e:
            error: str = "Failed to update payment gateway information"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error + "<br/>" + "Exception: " + str(e) + "<br/>"
    

    def delete(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactory import PaymentGatewayInterfaceFactory
        from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentGatewayInterface: PaymentGatewayInterface = PaymentGatewayInterfaceFactory().getInstance(self.httpServletRequest)
            paymentGatewayInterface.setStoreName(self.weblisketSession.getStoreName())
            storeName: str = paymentGatewayInterface.getStoreName()
            gatewayName: str = paymentGatewayInterface.getName()
            PaymentGatewayEntityFactory.getInstance().remove(storeName, BasicPaymentTypeUtil.getInstance().get(gatewayName))
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Successfully Removed payment gateway where store name=")
            stringBuffer.append(storeName)
            stringBuffer.append(" and gateway name=")
            stringBuffer.append(gatewayName)
            success: str = str(stringBuffer)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success + "<br/>"
        except Exception as e:
            error: str = "Failed to remove payment gateway from table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "remove()", e)
            return error + "<br/>" + "Exception: " + str(e) + "<br>"
    

    def drop(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = PaymentGatewayEntityFactory.getInstance().dropTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop payment transaction result table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = PaymentGatewayEntityFactory.getInstance().createTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create payment transaction result table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(PaymentGatewayEntityFactory.getInstance(), self.portion)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(PaymentGatewayEntityFactory.getInstance())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
# from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactory import PaymentGatewayInterfaceFactory
# from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
# from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


