# Generated Code Do Not Modify
# package org.allbinary.android

from __future__ import annotations



class ToastUtil:
    instance: ToastUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ToastUtil:
        return ToastUtil.instance
    

    def makeToast(self, view: View, context: Context, message: str, time: int) -> None:
        from org.allbinary.android.MakeToast import MakeToast
        class MakeToast(object):

            def _init_fields(self) -> None:
                self.string: str = None
            

            def __init__(self, string: str) -> None:
                self._init_fields()
                self.string = string
            

            def run(self) -> None:
                logUtil: LogUtil = LogUtil.getInstance()
                try:
                    Toast.makeText(self.context, self.string, self.time).show()
                except Exception as e:
                    commonStrings: CommonStrings = CommonStrings.getInstance()
                    logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
        view.post(MakeToast(message))
from android.content.Context import Context
from android.view.View import View
from android.widget.Toast import Toast
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


ToastUtil.instance = ToastUtil()

