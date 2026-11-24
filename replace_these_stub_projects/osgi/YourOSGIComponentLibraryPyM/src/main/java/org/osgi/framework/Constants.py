# Generated Code Do Not Modify
# package org.osgi.framework

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


# Java interface
class Constants:
    BUNDLE_SYMBOLICNAME: str = None
# from org.allbinary.logic.string.StringUtil import StringUtil


def _Constants_BUNDLE_SYMBOLICNAME() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return StringUtil.getInstance().EMPTY_STRING

lazy_static(Constants, "BUNDLE_SYMBOLICNAME", _Constants_BUNDLE_SYMBOLICNAME)

