# Generated Code Do Not Modify
# package org.allbinary.image.opengles

from __future__ import annotations



class OpenGLStrings:
    instance: OpenGLStrings = None

    def _init_fields(self) -> None:
        self.GL_ERROR_LABEL: str = "GLError: "
        self.SET: str = "set(GL10)"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLStrings:
        return OpenGLStrings.instance


OpenGLStrings.instance = OpenGLStrings()

