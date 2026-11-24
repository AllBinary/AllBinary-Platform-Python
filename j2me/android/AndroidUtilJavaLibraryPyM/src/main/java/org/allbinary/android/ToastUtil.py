# Generated Code Do Not Modify
# package org.allbinary.android

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ToastUtil:
    instance: ToastUtil = None
    #A member class instead of a local class using the method parameters since most of the converted languages do not have local classes.
    class MakeToast(object):

        def _init_fields(self) -> None:
            from android.content.Context import Context
            self.context: Context = None
            self.string: str = None
            self.time: int = None
        

        def __init__(self, context: Context, string: str, time: int) -> None:
            from android.content.Context import Context
            self._init_fields()
            self.context = context
            self.string = string
            self.time = time
        

        def run(self) -> None:
            from android.widget.Toast import Toast
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            try:
                Toast.makeText(self.context, self.string, self.time).show()
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ToastUtil:
        return ToastUtil.instance
    

    def makeToast(self, view: View, context: Context, message: str, time: int) -> None:
        from android.content.Context import Context
        from android.view.View import View
        view.post(ToastUtil.MakeToast(context, message, time))
# from android.content.Context import Context
# from android.view.View import View
# from android.widget.Toast import Toast
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


def _ToastUtil_instance() -> object:
    return ToastUtil()

lazy_static(ToastUtil, "instance", _ToastUtil_instance)

