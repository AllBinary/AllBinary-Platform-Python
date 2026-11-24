# Generated Code Do Not Modify
# package org.allbinary.image.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


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


def _OpenGLStrings_instance() -> object:
    return OpenGLStrings()

lazy_static(OpenGLStrings, "instance", _OpenGLStrings_instance)

