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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.animation.resource.BaseResourceAnimationInterfaceFactoryInterfaceFactory import BaseResourceAnimationInterfaceFactoryInterfaceFactory


class TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory(BaseResourceAnimationInterfaceFactoryInterfaceFactory):
    

    @staticmethod
    def createFactory() -> TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory:
        return TouchButtonResourceAnimationInterfaceFactoryInterfaceFactory("TouchButton Animations")
    

    def __init__(self, name: str) -> None:
        super().__init__(name, StdUtil.getInstance().createHashtable(), StdUtil.getInstance().createHashtable(), StdUtil.getInstance().createHashtable())
    

    # throws Exception
    def init(self, level: int) -> None:
        self.initImageCache(ImageCacheFactory.getInstance(), level)
    

    # throws Exception
    def initImageCache(self, imageCache: ImageCache, level: int) -> None:
        from org.allbinary.input.motion.button.TouchButtonBlankResource import TouchButtonBlankResource
        from org.allbinary.input.motion.button.TouchButtonGenericActionResource import TouchButtonGenericActionResource
        from org.allbinary.input.motion.button.TouchButtonStartResource import TouchButtonStartResource
        from org.allbinary.input.motion.button.TouchButtonUpResource import TouchButtonUpResource
        from org.allbinary.input.motion.button.TouchButtonDownResource import TouchButtonDownResource
        from org.allbinary.input.motion.button.TouchButtonTurnLeftResource import TouchButtonTurnLeftResource
        from org.allbinary.input.motion.button.TouchButtonTurnRightResource import TouchButtonTurnRightResource
        from org.allbinary.input.motion.button.TouchButtonStrafeLeftResource import TouchButtonStrafeLeftResource
        from org.allbinary.input.motion.button.TouchButtonStrafeRightResource import TouchButtonStrafeRightResource
        from org.allbinary.input.motion.button.TouchButtonStartResource import TouchButtonStartResource
        from org.allbinary.input.motion.button.TouchButtonStartResource import TouchButtonStartResource
        if self.isInitialized():
            return
        portion: int = 140
        loadingString: str = str(StringMaker().append(str(self)).append(" Loading: "))
        index: int = 0
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        touchButtonBlankResource: TouchButtonResource = TouchButtonBlankResource.getInstance()
        touchButtonGenericActionResource: TouchButtonResource = TouchButtonGenericActionResource.getInstance()
        touchButtonStartResource: TouchButtonResource = TouchButtonStartResource.getInstance()
        touchButtonUpResource: TouchButtonResource = TouchButtonUpResource.getInstance()
        touchButtonDownResource: TouchButtonResource = TouchButtonDownResource.getInstance()
        touchButtonTurnLeftResource: TouchButtonResource = TouchButtonTurnLeftResource.getInstance()
        touchButtonTurnRightResource: TouchButtonResource = TouchButtonTurnRightResource.getInstance()
        touchButtonStrafeLeftResource: TouchButtonResource = TouchButtonStrafeLeftResource.getInstance()
        touchButtonStrafeRightResource: TouchButtonResource = TouchButtonStrafeRightResource.getInstance()
        touchButtonBlankResourceImage: Image = imageCache.getWithKey(touchButtonBlankResource.RESOURCE)
        touchButtonGenericActionResourceImage: Image = imageCache.getWithKey(touchButtonGenericActionResource.RESOURCE)
        touchButtonStartResourceImage: Image = imageCache.getWithKey(touchButtonStartResource.RESOURCE)
        touchButtonUpResourceImage: Image = imageCache.getWithKey(touchButtonUpResource.RESOURCE)
        touchButtonDownResourceImage: Image = imageCache.getWithKey(touchButtonDownResource.RESOURCE)
        touchButtonTurnLeftResourceImage: Image = imageCache.getWithKey(touchButtonTurnLeftResource.RESOURCE)
        touchButtonTurnRightResourceImage: Image = imageCache.getWithKey(touchButtonTurnRightResource.RESOURCE)
        touchButtonStrafeLeftResourceImage: Image = imageCache.getWithKey(touchButtonStrafeLeftResource.RESOURCE)
        touchButtonStrafeRightResourceImage: Image = imageCache.getWithKey(touchButtonStrafeRightResource.RESOURCE)
        nullAnimationFactory: NullAnimationFactory = NullAnimationFactory.getFactoryInstance()
        if OperatingSystemFactory.getInstance().getOperatingSystemInstance().isOverScan():
            imageCache.getWithKey(TouchButtonStartResource.getInstance().HINT)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil: ImageCompleteUtil = ImageCompleteUtil.getInstance()
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonBlankResourceImage, touchButtonBlankResource.RESOURCE)
        self.add(touchButtonBlankResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonBlankResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonBlankResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonGenericActionResourceImage, touchButtonGenericActionResource.RESOURCE)
        self.add(touchButtonGenericActionResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonGenericActionResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonGenericActionResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonStartResourceImage, touchButtonStartResource.RESOURCE)
        self.add(touchButtonStartResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonStartResourceImage, AnimationBehaviorFactory.getInstance()))
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonUpResourceImage, touchButtonUpResource.RESOURCE)
        self.add(touchButtonUpResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonUpResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonUpResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonDownResourceImage, touchButtonDownResource.RESOURCE)
        self.add(touchButtonDownResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonDownResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonDownResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonTurnLeftResourceImage, touchButtonTurnLeftResource.RESOURCE)
        self.add(touchButtonTurnLeftResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonTurnLeftResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonTurnLeftResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonTurnRightResourceImage, touchButtonTurnRightResource.RESOURCE)
        self.add(touchButtonTurnRightResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonTurnRightResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonTurnRightResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonStrafeLeftResourceImage, touchButtonStrafeLeftResource.RESOURCE)
        self.add(touchButtonStrafeLeftResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonStrafeLeftResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonStrafeLeftResource.HINT, nullAnimationFactory)
        progressCanvas.addPortion(portion, loadingString, ((index := index + 1) - 1))
        imageCompleteUtil.waitForImage(touchButtonStrafeRightResourceImage, touchButtonStrafeRightResource.RESOURCE)
        self.add(touchButtonStrafeRightResource.RESOURCE, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonStrafeRightResourceImage, AnimationBehaviorFactory.getInstance()))
        self.add(touchButtonStrafeRightResource.HINT, nullAnimationFactory)
        if OperatingSystemFactory.getInstance().getOperatingSystemInstance().isOverScan():
            touchButtonStartHintResource: Image = imageCache.getWithKey(TouchButtonStartResource.getInstance().HINT)
            self.add(touchButtonStartResource.HINT, OneRowSpriteIndexedAnimationFactory.createFactory(touchButtonStartHintResource, AnimationBehaviorFactory.getInstance()))
        else:
            self.add(touchButtonStartResource.HINT, nullAnimationFactory)
        super().init(level)
    

    def isLoadingLevel(self, level: int) -> bool:
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if level == resourceLoadingLevelFactory.LOAD_TOUCH.getLevel():
            return True
        else:
            return super().isLoadingLevel(level)
    

    def isFeature(self) -> bool:
        if not Features.getInstance().isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            return True
        else:
            return False
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.image.sprite.OneRowSpriteIndexedAnimationFactory import OneRowSpriteIndexedAnimationFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.media.image.ImageCompleteUtil import ImageCompleteUtil


