# Generated Code Do Not Modify
# package org.platform.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.image.opengles.OpenGLImageUtilBase import OpenGLImageUtilBase


class OpenGLImageUtil(OpenGLImageUtilBase):
    instance: OpenGLImageUtil = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> OpenGLImageUtil:
        return OpenGLImageUtil.instance


def _OpenGLImageUtil_instance() -> object:
    return OpenGLImageUtil()

lazy_static(OpenGLImageUtil, "instance", _OpenGLImageUtil_instance)

