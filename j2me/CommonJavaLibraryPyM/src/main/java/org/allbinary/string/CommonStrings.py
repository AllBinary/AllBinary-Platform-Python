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
# package org.allbinary.string

from __future__ import annotations



class CommonStrings:
    instance: CommonStrings = None

    def _init_fields(self) -> None:
        self.EMPTY: str = "Empty"
        self.CREATE_IMAGE: str = "createImage"
        self.PLEASE_WAIT: str = "Please Wait"
        self.PLEASE_WAIT_FOR_SERVER: str = "Please Wait Getting Data From Server..."
        self.PERIODS: str = "..."
        self.LOADING: str = "Loading..."
        self.CONSTRUCTOR: str = "Constructor"
        self.START: str = "Start"
        self.END: str = "End"
        self.EXCEPTION: str = "Exception"
        self.EXCEPTION_LABEL: str = "Exception: "
        self.CLEANUP: str = "cleanup"
        self.INIT: str = "init"
        self.CLOSE: str = "close"
        self.UP: str = "up"
        self.DOWN: str = "down"
        self.LEFT: str = "left"
        self.RIGHT: str = "right"
        self.DIRECTION_NAME: list[str] = [self.DOWN, self.LEFT, self.RIGHT, self.UP]
        self.CREATE: str = "Create"
        self.REMOVE: str = "Remove"
        self.UPDATE: str = "Update"
        self.DELETE: str = "Delete"
        self.delete: str = "delete"
        self.LOAD: str = "load"
        self.SAVE: str = "save"
        self.ADD: str = "Add"
        self.DROP: str = "Drop"
        self.INSERT: str = "Insert"
        self.VISIT: str = "visit"
        self.START_METHOD_NAME: str = self.START
        self.END_METHOD_NAME: str = "end"
        self.GET: str = "get"
        self.PROCESS: str = "process"
        self.GET_INSTANCE: str = "getInstance"
        self.GET_LIST: str = "getList"
        self.RUN: str = "run"
        self.START_RUNNABLE: str = "Start Runnable"
        self.RUNNING: str = "Running"
        self.END_RUNNABLE: str = "End Runnable"
        self.DISABLE: str = "disable"
        self.ENABLE: str = "enable"
        self.SUCCESS: str = "Command Success"
        self.FAILURE: str = "Command Failed"
        self.NOT_IMPLEMENTED: str = "Not Implemented"
        self.UNKNOWN: str = "Unknown"
        self.ON_EVENT: str = "onEvent"
        self.IS_VALID: str = "isValid"
        self.TOSTRING: str = "toString"
        self.ADD_LISTENER: str = "addListener"
        self.REMOVE_LISTENER: str = "removeListener"
        self.SIZE: str = "size"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonStrings:
        return CommonStrings.instance
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty


CommonStrings.instance = CommonStrings()

