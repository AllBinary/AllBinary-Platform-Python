# Generated Code Do Not Modify
# package javax.microedition.khronos.opengles

from __future__ import annotations

from javax.microedition.khronos.opengles.GL import GL


# Java interface
class GL11Ext(GL):
    GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES: int = 35742
    GL_MATRIX_INDEX_ARRAY_OES: int = 34884
    GL_MATRIX_INDEX_ARRAY_POINTER_OES: int = 34889
    GL_MATRIX_INDEX_ARRAY_SIZE_OES: int = 34886
    GL_MATRIX_INDEX_ARRAY_STRIDE_OES: int = 34888
    GL_MATRIX_INDEX_ARRAY_TYPE_OES: int = 34887
    GL_MATRIX_PALETTE_OES: int = 34880
    GL_MAX_PALETTE_MATRICES_OES: int = 34882
    GL_MAX_VERTEX_UNITS_OES: int = 34468
    GL_TEXTURE_CROP_RECT_OES: int = 35741
    GL_WEIGHT_ARRAY_BUFFER_BINDING_OES: int = 34974
    GL_WEIGHT_ARRAY_OES: int = 34477
    GL_WEIGHT_ARRAY_POINTER_OES: int = 34476
    GL_WEIGHT_ARRAY_SIZE_OES: int = 34475
    GL_WEIGHT_ARRAY_STRIDE_OES: int = 34474
    GL_WEIGHT_ARRAY_TYPE_OES: int = 34473
    

    def glTexParameterfv(self, target: int, pname: int, param: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    def glCurrentPaletteMatrixOES(self, matrixpaletteindex: int) -> None:
        raise NotImplementedError()
    

    def glDrawTexfOES(self, x: float, y: float, z: float, width: float, height: float) -> None:
        raise NotImplementedError()
    

    def glDrawTexfvOES(self, coords: list[float], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glDrawTexfvOES(self, coords: FloatBuffer) -> None:
        raise NotImplementedError()
    

    def glDrawTexiOES(self, x: int, y: int, z: int, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def glDrawTexivOES(self, coords: list[int], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glDrawTexivOES(self, coords: IntBuffer) -> None:
        raise NotImplementedError()
    

    def glDrawTexsOES(self, x: int, y: int, z: int, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def glDrawTexsvOES(self, coords: list[int], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glDrawTexsvOES(self, coords: ShortBuffer) -> None:
        raise NotImplementedError()
    

    def glDrawTexxOES(self, x: int, y: int, z: int, width: int, height: int) -> None:
        raise NotImplementedError()
    

    def glDrawTexxvOES(self, coords: list[int], offset: int) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glDrawTexxvOES(self, coords: IntBuffer) -> None:
        raise NotImplementedError()
    

    def glEnable(self, cap: int) -> None:
        raise NotImplementedError()
    

    def glEnableClientState(self, array: int) -> None:
        raise NotImplementedError()
    

    def glLoadPaletteFromModelViewMatrixOES(self) -> None:
        raise NotImplementedError()
    

    def glMatrixIndexPointerOES(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glMatrixIndexPointerOES(self, size: int, type_: int, stride: int, offset: int) -> None:
        raise NotImplementedError()
    

    def glWeightPointerOES(self, size: int, type_: int, stride: int, pointer: Buffer) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def glWeightPointerOES(self, size: int, type_: int, stride: int, offset: int) -> None:
        raise NotImplementedError()
# from java.nio.Buffer import Buffer
# from java.nio.FloatBuffer import FloatBuffer
# from java.nio.IntBuffer import IntBuffer
# from java.nio.ShortBuffer import ShortBuffer


