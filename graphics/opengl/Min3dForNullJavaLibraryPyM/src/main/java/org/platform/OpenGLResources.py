# Generated Code Do Not Modify
# package org.platform

from __future__ import annotations



class OpenGLResources:
    instance: OpenGLResources = None
    

    @staticmethod
    def getInstance() -> OpenGLResources:
        return OpenGLResources.instance
    

    def init(self) -> None:
        pass
    

    def isExcluded(self, name: str) -> bool:
        raise RuntimeError()
    

    def getIdentifier(self, name: str, defType: str, defPackage: str) -> int:
        raise RuntimeError()
    

    # throws Exception
    def openRawResource(self, id: int) -> InputStream:
        raise RuntimeError()
    

    # throws Exception
    def openRawResourceFromName(self, resourceName: str) -> InputStream:
        raise RuntimeError()
    

    # throws Exception
    def getResourceAsStream(self, resourceName: str) -> InputStream:
        raise RuntimeError()
    

    def getPackageName(self) -> str:
        raise RuntimeError()
# from java.io.InputStream import InputStream


OpenGLResources.instance = OpenGLResources()

