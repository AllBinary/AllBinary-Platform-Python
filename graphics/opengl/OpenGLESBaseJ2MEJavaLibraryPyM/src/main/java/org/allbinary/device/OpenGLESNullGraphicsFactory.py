# Generated Code Do Not Modify
# package org.allbinary.device

from __future__ import annotations

from org.allbinary.device.OpenGLESGraphics import OpenGLESGraphics


class OpenGLESNullGraphicsFactory:
    instance: OpenGLESGraphics = OpenGLESGraphics()
    

    @staticmethod
    def getInstance() -> OpenGLESGraphics:
        return OpenGLESNullGraphicsFactory.instance


