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
# package org.allbinary.animation.image.sprite

from __future__ import annotations

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class ImageCaptionIndexedAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationFactoryImageScaleUtil: AnimationFactoryImageScaleUtil = AnimationFactoryImageScaleUtil.getInstance()
        self.animationFactorySpriteScaleUtil: AnimationFactorySpriteScaleUtil = AnimationFactorySpriteScaleUtil.getInstance()
        self.captionImage: Image = None
        self.spriteMovieImage: Image = None
        self.frameWidth: int = None
        self.frameHeight: int = None
        self.captionDx: int = None
        self.captionDy: int = None
        self.dx: int = None
        self.dy: int = None
        self.time: int = None
        self.soundInterface: Sound = None
        self.scaleProperties: ScaleProperties = ScaleProperties.instance
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, captionImage: Image, spriteMovieImage: Image, soundInterface: Sound, frameWidth: int, frameHeight: int, captionDx: int, captionDy: int, dx: int, dy: int, time: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        if animationBehaviorFactory == AnimationBehaviorFactory.getInstance():
            ForcedLogUtil.log("Using default AnimationBehaviorFactory with IndexedAnimationFactory", self)
        self.captionImage = captionImage
        self.spriteMovieImage = spriteMovieImage
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        self.captionDx = captionDx
        self.captionDy = captionDy
        self.dx = dx
        self.dy = dy
        self.time = time
        self.soundInterface = soundInterface
        self.animationBehaviorFactory = animationBehaviorFactory
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.sprite.SpriteIndexedAnimation import SpriteIndexedAnimation
        scaledImage: Image = self.animationFactoryImageScaleUtil.createImage(self.captionImage, self.captionImage.getWidth(), self.captionImage.getHeight(), self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        animationInterface: Animation = ImageAnimation(scaledImage, self.animationBehaviorFactory.getOrCreateInstance())
        sprite: Sprite = self.animationFactorySpriteScaleUtil.createImage(self.spriteMovieImage, self.frameWidth, self.frameHeight, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        movieIndexedAnimationInterface: IndexedAnimation = SpriteIndexedAnimation(sprite, self.spriteMovieImage, BasicColorUtil.getInstance().ZERO_ARRAY, self.animationBehaviorFactory.getOrCreateInstance())
        player: Player = self.soundInterface.getPlayerP()
        if player is None:
            raise Exception("Sound Was not Initialized")
        return CaptionIndexedAnimation(animationInterface, movieIndexedAnimationInterface, player, self.captionDx, self.captionDy, self.dx, self.dy, self.time, self.animationBehaviorFactory.getOrCreateInstance())
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        self.scaleProperties = scaleProperties
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
# from javax.microedition.media.Player import Player
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.caption.CaptionIndexedAnimation import CaptionIndexedAnimation
from org.allbinary.animation.image.ImageAnimation import ImageAnimation
from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil
from org.allbinary.image.AnimationFactoryImageScaleUtil import AnimationFactoryImageScaleUtil
from org.allbinary.image.sprite.AnimationFactorySpriteScaleUtil import AnimationFactorySpriteScaleUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.media.audio.Sound import Sound


