#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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
# package org.allbinary.opengles

from __future__ import annotations

import math


class GLUtil:
    instance: GLUtil = None

    def _init_fields(self) -> None:
        self.BYTES_PER_FLOAT: int = 4

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GLUtil:
        return GLUtil.instance
    

    def makeFloatBuffer3(self, p_a: float, p_b: float, p_c: float) -> FloatBuffer:
        b: ByteBuffer = ByteBuffer.allocateDirect(3 * self.BYTES_PER_FLOAT)
        b.order(ByteOrder.nativeOrder())
        buffer: FloatBuffer = b.asFloatBuffer()
        buffer.put(p_a)
        buffer.put(p_b)
        buffer.put(p_c)
        self.position(buffer, 0)
        return buffer
    

    def makeFloatBuffer4(self, p_a: float, p_b: float, p_c: float, p_d: float) -> FloatBuffer:
        b: ByteBuffer = ByteBuffer.allocateDirect(4 * self.BYTES_PER_FLOAT)
        b.order(ByteOrder.nativeOrder())
        buffer: FloatBuffer = b.asFloatBuffer()
        buffer.put(p_a)
        buffer.put(p_b)
        buffer.put(p_c)
        buffer.put(p_d)
        self.position(buffer, 0)
        return buffer
    

    def makeFloatBuffer(self, byteBuffer: ByteBuffer) -> FloatBuffer:
        b: ByteBuffer = ByteBuffer.allocateDirect(byteBuffer.limit() * self.BYTES_PER_FLOAT)
        b.order(ByteOrder.nativeOrder())
        buffer: FloatBuffer = b.asFloatBuffer()
        unsigned: int = 0
        v: float = 0.0
        while byteBuffer.hasRemaining():
            unsigned = byteBuffer.get() & 0xFF
            v = (float(unsigned)) / 255.0
            buffer.put(v)
        self.position(buffer, 0)
        return buffer
    

    def position(self, buffer: Buffer, newPosition: int) -> Buffer:
        return buffer.position(newPosition)
    

    def rotateUVs(self, uvs: list[float], angleDegrees: float, pivotU: float, pivotV: float) -> None:
        angleRad: float = math.radians(angleDegrees)
        cosA: float = math.cos(angleRad)
        sinA: float = math.sin(angleRad)
        for i in range(0, len(uvs), 2):
            u: float = uvs[i]
            v: float = uvs[i + 1]
            du: float = u - pivotU
            dv: float = v - pivotV
            ru: float = (du * cosA - dv * sinA) + pivotU
            rv: float = (du * sinA + dv * cosA) + pivotV
            uvs[i] = ru
            uvs[i + 1] = rv
# from java.nio.Buffer import Buffer
# from java.nio.ByteBuffer import ByteBuffer
# from java.nio.ByteOrder import ByteOrder
# from java.nio.FloatBuffer import FloatBuffer


GLUtil.instance = GLUtil()

