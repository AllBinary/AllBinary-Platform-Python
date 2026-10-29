# Generated Code Do Not Modify
# package org.platform.graphics

from __future__ import annotations

from org.allbinary.image.opengles.OpenGLImageUtilBase import OpenGLImageUtilBase


class OpenGLImageUtil(OpenGLImageUtilBase):
    instance: OpenGLImageUtil = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> OpenGLImageUtil:
        return OpenGLImageUtil.instance


OpenGLImageUtil.instance = OpenGLImageUtil()

