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
# package org.allbinary.input.automation.module

from __future__ import annotations



class TestInputAutomationWorker:

    def _init_fields(self) -> None:
        if "captureWorker" not in vars(self): self.captureWorker: ScreenCaptureImagesWorker = None
        if "imageComparisonWorker" not in vars(self): self.imageComparisonWorker: ImageComparisonWorker = None
        if "motionRectanglesWorker" not in vars(self): self.motionRectanglesWorker: MotionRectanglesWorker = None
        if "changedPixelsImageComparisonResultsWorker" not in vars(self): self.changedPixelsImageComparisonResultsWorker: SaveImageComparisonWorker = None
        if "saveMotionRectanglesAsImagesWorker" not in vars(self): self.saveMotionRectanglesAsImagesWorker: SaveMotionRectanglesResultsWorker = None
        if "moveMouseToFirstMotionRectanglesResultsWorker" not in vars(self): self.moveMouseToFirstMotionRectanglesResultsWorker: TestInputForMotionRectanglesResultsWorker = None
    

    def __init__(self) -> None:
        from org.allbinary.input.media.image.capture.ScreenCaptureImagesWorker import ScreenCaptureImagesWorker
        from org.allbinary.media.image.comparison.SaveImageComparisonWorker import SaveImageComparisonWorker
        from org.allbinary.media.image.comparison.motion.SaveMotionRectanglesResultsWorker import SaveMotionRectanglesResultsWorker
        from org.allbinary.media.image.comparison.motion.TestInputForMotionRectanglesResultsWorker import TestInputForMotionRectanglesResultsWorker
        __class__._init_fields(self)
        self.captureWorker = ScreenCaptureImagesWorker()
        self.changedPixelsImageComparisonResultsWorker = SaveImageComparisonWorker()
        self.saveMotionRectanglesAsImagesWorker = SaveMotionRectanglesResultsWorker()
        self.moveMouseToFirstMotionRectanglesResultsWorker = TestInputForMotionRectanglesResultsWorker()
        self.motionRectanglesWorker.addListenerInterface(self.saveMotionRectanglesAsImagesWorker)
        self.motionRectanglesWorker.addListenerInterface(self.moveMouseToFirstMotionRectanglesResultsWorker)
        self.imageComparisonWorker.addListenerInterface(self.changedPixelsImageComparisonResultsWorker)
        self.imageComparisonWorker.addListenerInterface(self.motionRectanglesWorker)
        self.captureWorker.addListenerInterface(self.imageComparisonWorker)
# from org.allbinary.input.media.image.capture.ScreenCaptureImagesWorker import ScreenCaptureImagesWorker
# from org.allbinary.media.image.comparison.ImageComparisonWorker import ImageComparisonWorker
# from org.allbinary.media.image.comparison.SaveImageComparisonWorker import SaveImageComparisonWorker
# from org.allbinary.media.image.comparison.motion.MotionRectanglesWorker import MotionRectanglesWorker
# from org.allbinary.media.image.comparison.motion.SaveMotionRectanglesResultsWorker import SaveMotionRectanglesResultsWorker
# from org.allbinary.media.image.comparison.motion.TestInputForMotionRectanglesResultsWorker import TestInputForMotionRectanglesResultsWorker


