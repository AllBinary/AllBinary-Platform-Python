# Generated Code Do Not Modify
# package org.allbinary.device

from __future__ import annotations



class OpenGLESGraphicsFactory:
    

    def getOpenGLESGraphicsInstance(self) -> OpenGLESGraphics:
        from org.allbinary.device.OpenGLESNullGraphicsFactory import OpenGLESNullGraphicsFactory
        return OpenGLESNullGraphicsFactory.getInstance()


