# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot 
#   
# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles.shader

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.opengles.shader.ShaderUpdater import ShaderUpdater


@java_inherited_overloads
class CompositeShaderUpdater(ShaderUpdater):
    instanceC: CompositeShaderUpdater = None
    def _java_defaults(self):
        vars(self).setdefault("commonSeps", None)
        vars(self).setdefault("shaderStrings", None)
        vars(self).setdefault("uniformBlockHandleArray", None)
        vars(self).setdefault("uniformBlockArray", None)
        vars(self).setdefault("uniformHandleArray", None)
        vars(self).setdefault("uniformArray", None)
        vars(self).setdefault("attributeHandleArray", None)
        vars(self).setdefault("attributeArray", None)

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonSeps import CommonSeps
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.shaderStrings: ShaderStrings = ShaderStrings.getInstance()
        if "uniformBlockHandleArray" not in vars(self): self.uniformBlockHandleArray: list[int] = None
        if "uniformBlockArray" not in vars(self): self.uniformBlockArray: list[str] = None
        if "uniformHandleArray" not in vars(self): self.uniformHandleArray: list[int] = None
        if "uniformArray" not in vars(self): self.uniformArray: list[str] = None
        if "attributeHandleArray" not in vars(self): self.attributeHandleArray: list[int] = None
        if "attributeArray" not in vars(self): self.attributeArray: list[str] = None
    

    @staticmethod
    def getInstance() -> CompositeShaderUpdater:
        return CompositeShaderUpdater.instanceC
    

    def __init__(self, uniformBlockArray: list[str], uniformArray: list[str], attributeArray: list[str], attributeHandleArray: list[int]) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.uniformBlockArray = uniformBlockArray
        self.uniformBlockHandleArray = [0] * (len(self.uniformBlockArray))
        self.uniformArray = uniformArray
        self.uniformHandleArray = [0] * (len(self.uniformArray))
        self.attributeArray = attributeArray
        self.attributeHandleArray = attributeHandleArray
    

    def onSurfaceCreated(self, gl: GL10, eglConfig: EGLConfig, programHandle: int) -> None:
        from javax.microedition.khronos.egl.EGLConfig import EGLConfig
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
    

    def onSurfaceDestroyed(self, gl: GL10) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
# from javax.microedition.khronos.egl.EGLConfig import EGLConfig
# from javax.microedition.khronos.opengles.GL10 import GL10
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.graphics.opengles.shader.ShaderStrings import ShaderStrings


def _CompositeShaderUpdater_instanceC() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    from org.allbinary.logic.string.StringUtil import StringUtil
    return CompositeShaderUpdater(StringUtil.getInstance().getArrayInstance(), StringUtil.getInstance().getArrayInstance(), StringUtil.getInstance().getArrayInstance(), NullUtil.getInstance().NULL_INT_ARRAY)

lazy_static(CompositeShaderUpdater, "instanceC", _CompositeShaderUpdater_instanceC)

