# Generated Code Do Not Modify
# package org.allbinary.media.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate


# Shares image operations between the SWT and OpenGL implementations. 
class SwtOpenGLESImageBridge:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def addImage(util: OpenGLUtil, image: Image) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.opengles.OpenGLUtil import OpenGLUtil
        return util.addImage(image)
    

    @staticmethod
    def isCustomScaling(util: OpenGLESImageExclusionUtil, image: Image) -> bool:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.image.opengles.OpenGLESImageExclusionUtil import OpenGLESImageExclusionUtil
        return util.isCustomScaling(image)
    

    @staticmethod
    def getOpenGLESImage(image: Image) -> OpenGLESImage:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
        return image
    

    @staticmethod
    def getBitmapImage(image: OpenGLESImage) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
        return image.openGLBitmap.getImage()
    

    @staticmethod
    def asImage(image: OpenGLESImage) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
        return image
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.opengles.OpenGLUtil import OpenGLUtil
# from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
# from org.allbinary.image.opengles.OpenGLESImageExclusionUtil import OpenGLESImageExclusionUtil


