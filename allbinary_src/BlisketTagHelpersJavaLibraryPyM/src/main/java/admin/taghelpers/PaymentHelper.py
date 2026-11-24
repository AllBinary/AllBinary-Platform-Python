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

from admin.taghelpers.Table import Table


class PaymentHelper(Table):

    def _init_fields(self) -> None:
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.request: HttpServletRequest = None
        self.value: str = None
        self.portion: Portion = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.portion = Portion(hashMap)
        self.getFormData()
    

    def getFormData(self) -> None:
        self.value = self.request.getParameter("VALUE")
    

    def insert(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.PaymentFactory import PaymentFactory
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Added Payment"
            paymentEntity: PaymentEntity = PaymentEntityFactory.getInstance().getPaymentEntityInstance()
            paymentInterface: PaymentInterface = PaymentFactory.getInstance(self.request)
            paymentEntity.add(self.weblisketSession.getUserName(), paymentInterface)
            paymentEntity.setDefault(self.weblisketSession.getUserName(), int(paymentEntity.getLastId(self.weblisketSession.getUserName())))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "addPayment()")
            return success
        except Exception as e:
            error: str = "Failed to add Payment"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "addPayment()", e)
            return error
    

    def select(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Selected Payment"
            paymentEntity: PaymentEntity = PaymentEntityFactory.getInstance().getPaymentEntityInstance()
            paymentEntity.setDefault(self.weblisketSession.getUserName(), int(self.value))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "selectPayment()")
            return success
        except Exception as e:
            error: str = "Failed to select Payment"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "selectPayment()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Removed Payment"
            paymentEntity: PaymentEntity = PaymentEntityFactory.getInstance().getPaymentEntityInstance()
            paymentEntity.remove(self.weblisketSession.getUserName(), int(self.value))
            paymentInterface: PaymentInterface = paymentEntity.getDefault(self.weblisketSession.getUserName())
            if paymentInterface is None:
                paymentEntity.setDefault(self.weblisketSession.getUserName(), int(paymentEntity.getLastId(self.weblisketSession.getUserName())))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "removePayment()")
            return success
        except Exception as e:
            error: str = "Failed to remove Payment"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "removePayment()", e)
            return error
    

    def drop(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentEntity: PaymentEntity = PaymentEntityFactory.getInstance().getPaymentEntityInstance()
            success: str = paymentEntity.dropTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop Admin table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentEntity: PaymentEntity = PaymentEntityFactory.getInstance().getPaymentEntityInstance()
            success: str = paymentEntity.createTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create user table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(PaymentEntityFactory.getInstance().getPaymentEntityInstance(), self.portion)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Backup Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(PaymentEntityFactory.getInstance().getPaymentEntityInstance())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
    

    # throws LicensingException
    def update(self) -> str:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        return self.commonStrings.NOT_IMPLEMENTED
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.business.user.commerce.money.payment.PaymentFactory import PaymentFactory
# from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
# from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntity import PaymentEntity
# from org.allbinary.data.tables.user.commerce.money.payment.PaymentEntityFactory import PaymentEntityFactory
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


