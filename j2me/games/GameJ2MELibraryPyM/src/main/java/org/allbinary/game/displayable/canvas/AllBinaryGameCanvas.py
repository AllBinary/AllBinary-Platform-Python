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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

import time
import threading
from org.allbinary.canvas.RunnableCanvas import RunnableCanvas
from org.allbinary.game.IntermissionCompositeInterface import IntermissionCompositeInterface
from org.allbinary.game.IntermissionEnableListenerInterface import IntermissionEnableListenerInterface
from org.allbinary.graphics.displayable.event.DisplayChangeEventListener import DisplayChangeEventListener
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvasInterface import AllBinaryGameCanvasInterface
from org.allbinary.game.displayable.canvas.GameCanvasRunnableInterface import GameCanvasRunnableInterface
from org.allbinary.game.displayable.canvas.MenuListener import MenuListener
from org.allbinary.game.displayable.canvas.PopupMenuInterface import PopupMenuInterface


class AllBinaryGameCanvas(RunnableCanvas, AllBinaryGameCanvasInterface, GameCanvasRunnableInterface, MenuListener, IntermissionCompositeInterface, IntermissionEnableListenerInterface, PopupMenuInterface, DisplayChangeEventListener, UpdateMyFontInterface):
    id: int = 0
    TYPE: int = 2
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.touchFeatureFactory: TouchFeatureFactory = TouchFeatureFactory.getInstance()
        self.openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        self.touchButtonFactory: TouchButtonFactory = TouchButtonFactory.getInstance()
        self.gameAdStateFactory: GameAdStateFactory = GameAdStateFactory.getInstance()
        self.gameStrings: GameStrings = GameStrings.getInstance()
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        self.gameStateFactory: GameStateFactory = GameStateFactory.getInstance()
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.gameTickDisplayInfoSingleton: GameTickDisplayInfoSingleton = GameTickDisplayInfoSingleton.getInstance()
        self.gameRunnable: GameCanvasRunnable = GameCanvasRunnable(self)
        self.gamePauseRunnable: GameCanvasPauseRunnable = GameCanvasPauseRunnable(self)
        self.formUtil: FormUtil = FormUtil.getInstance()
        self.myFormUtil: MyFormUtil = MyFormUtil.getInstance()
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.gameSpecificPaintable: Paintable = NullPaintable.getInstance()
        self.sensorGameUpdateProcessor: SensorGameUpdateProcessor = SingleSensorGameUpdateProcessor()
        self.endGameInfo: EndGameInfo = EndGameInfo()
        self.startIntermissionInterface: IntermissionInterface = Intermission()
        self.endLevelIntermissionInterface: IntermissionInterface = Intermission()
        self.gameLayerManager: AllBinaryGameLayerManager = AllBinaryGameLayerManager.getNullInstance()
        self.gameState: GameState = self.gameStateFactory.NO_GAME_STATE
        self.gameOver: bool = False
        self.initialized: bool = False
        self.gameStateTimeHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.highScoresHelper: HighScoresHelperBaseInterface = None
        self.highScoreSubmitted: bool = False
        self.realHighScoresPaintable: HighScoresPaintable = HighScoresPaintable()
        self.highScoresPaintable: Paintable = NullPaintable.getInstance()
        self.localPlayerGameInputList: BasicArrayList = BasicArrayListD()
        self.isCheating: bool = False
        self.hashtable: ABHashtable[object, object] = self.stdUtil.NULL_TABLE
        self.isSingleKeyRepeatableProcessing: bool = False
        self.gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory = BasicBuildGameInitializerFactory.NULL_BASE_BUILD_GMAE_INITIALIZER_FACTORY
        self.touchButtonsPaintable: Paintable = NullPaintable.getInstance()
        self.touchPaintable: Paintable = NullPaintable.getInstance()
        self.cheatProcessor: PlayerGameInput = NoPlayerGameInput.getInstance()
        self.gameInputProcessor: Processor = Processor.getInstance()
        self.endGameProcessor: Processor = Processor.getInstance()
        self.realEndGameProcessor: Processor = Processor.getInstance()
        self.startIntermissionProcessor: Processor = Processor.getInstance()
        self.realStartIntermissionProcessor: Processor = Processor.getInstance()
        self.endGamePaintable: Paintable = NullPaintable.getInstance()
        self.endGameStatePaintable: Paintable = NullPaintable.getInstance()
        self.nonBotPaintable: Paintable = NullPaintable.getInstance()
        self.intermissionPaintable: Paintable = NullPaintable.getInstance()
        self.startIntermissionPaintable: InitUpdatePaintable = NullInitUpdatePaintable.getInstance()
        self.mainStateProcessor: Processor = Processor.getInstance()
        self.processGameProcessor: Processor = Processor.getInstance()
        self.highScoresFactoryInterface: HighScoresFactoryInterface = None
        self.startLevel: int = 0
        self.mainMenuInputProcessor: BasicMenuInputProcessor = NoMenuInputProcessor.getInstance()
        self.popupMenuInputProcessor: BasicMenuInputProcessor = NoMenuInputProcessor.getInstance()
        self.menuInputProcessor: BasicMenuInputProcessor = NoMenuInputProcessor.getInstance()
        self.menuForm: ScrollSelectionForm = ScrollSelectionForm.getNullScrollSelectionForm()
        self.formPaintable: Paintable = NullPaintable.getInstance()
        self.openMenuPaintable: Paintable = NullPaintable.getInstance()
        self.menuPaintable: Paintable = NullPaintable.getInstance()
        self.currentTouchInputFactory: BaseTouchInput = NoButtonsTouchInputFactory.getInstance()
        self.colorFillPaintable: ColorFillBasePaintable = ColorFillPaintableFactory.getInstance().getInstance(self.basicColorFactory.BLACK, True)
        self.baseGameStatistics: BaseGameStatistics = GameStatisticsFactory.getInstance()
        self.primaryPlayerQueue: PlayerQueue = PrimaryPlayerQueueFactory.getInstance()
        self.secondaryPlayerQueue: PlayerQueue = SecondaryPlayerQueueFactory.getInstance()
        self.BUILD_GAME: str = "buildGame"
        self.gameTypeFactory: GameTypeFactory = GameTypeFactory.getInstance()
        self.screenCapture: ScreenCapture = ScreenCaptureFactory.getInstance()
        self.basicMotionGesturesHandler: BasicMotionGesturesHandler = BasicMotionGesturesHandler.getInstance()
        self.gameKeyEventHandler: GameKeyEventHandler = GameKeyEventHandler.getInstance()
        self.gameBehavior: DemoGameBehavior = None
        self.menuBehavior: BaseMenuBehavior = None
        self.progressPaintable: PaintableInterface = ProgressCanvasFactory.getLazyInstance()
        self.fontHeightP: int = 0
        self.gameCanvasStartListener: DemoPaintableInterface = NullDemoPaintable.NULL_DEMO_PAINTABLE
        self.rawGameInputProcessor: InputProcessor = GameCanvasInputProcessor(self)
        self.rawInputProcessor: InputProcessor = FormInputProcessor(self)
        self.inputProcessor: InputProcessor = self.getRawGameInputProcessor()
        self.YIELD_SLEEP: int = 100
    

    def __init__(self, commandListener: CommandListener, gameLayerManager: AllBinaryGameLayerManager, highScoresFactoryInterface: HighScoresFactoryInterface, gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory, buffered: bool) -> None:
        from org.allbinary.game.displayable.canvas.BaseGameBehavior import BaseGameBehavior
        from org.allbinary.game.displayable.canvas.DemoGameBehavior import DemoGameBehavior
        from org.allbinary.game.displayable.canvas.BaseMenuBehavior import BaseMenuBehavior
        super().__init__(commandListener, CanvasStrings.getInstance().EMPTY_CHILD_NAME_LIST, True)
        self._init_fields()
        self.highScoresHelper = highScoresFactoryInterface.createHighScoresHelper()
        self.gameInitializationInterfaceFactoryInterface = gameInitializationInterfaceFactoryInterface
        self.init(gameLayerManager, buffered)
        self.highScoresFactoryInterface = highScoresFactoryInterface
        if self.gameLayerManager.getGameInfo().getGameType() == self.gameTypeFactory.BOT or self.gameLayerManager.getGameInfo().getGameType() == self.gameTypeFactory.NONE:
            self.gameBehavior = DemoGameBehavior.getInstance()
            self.menuBehavior = BaseMenuBehavior.getInstance()
        else:
            self.gameBehavior = BaseGameBehavior.getInstance()
            self.menuBehavior = self.getInGameMenuBehavior()
        self.initPopupMenu()
        self.initMenu()
        self.initSpecialPaint()
        DisplayChangeEventHandler.getInstance().addListenerInterface(self)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from org.allbinary.game.displayable.canvas.NoMenuInputProcessor import NoMenuInputProcessor
        try:
            font: Font = graphics.getFont()
            self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).append(self.canvasStrings.FD_WIDTH).appendint(int(MyFontProcessor.defaultCharWidth(font))).append(self.canvasStrings.FD_HEIGHT).appendint(int(font.getHeight()))), self, self.canvasStrings.UPDATE_MEASUREMENT)
            self.fontHeightP = font.getHeight()
            self.myFormUtil.updateMeasurement(graphics)
            popupMenuRectangle: Rectangle = self.myFormUtil.getPopupMenuRectangle()
            basicPopupMenuPaintable: BasicPopupMenuPaintable = (self.getOpenMenuPaintable())
            basicPopupMenuPaintable.init(popupMenuRectangle)
            if self.getPopupMenuInputProcessor() != NoMenuInputProcessor.getInstance():
                popupMenuInputProcessor: PopupMenuInputProcessor = (self.getPopupMenuInputProcessor())
                popupMenuInputProcessor.init(popupMenuRectangle)
            self.myFontProcessor = MyFontProcessor.getInstance()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT, e)
    

    def getInGameMenuBehavior(self) -> BaseMenuBehavior:
        from org.allbinary.game.displayable.canvas.InGameMenuBehavior import InGameMenuBehavior
        return InGameMenuBehavior.getInstance()
    

    def setCurrentThread(self) -> None:
        if J2MEUtil.isHTML():
            super().setCurrentThreadFake()
        else:
            super().setCurrentThread()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        try:
            self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).append(str(DisplayInfoSingleton.getInstance()))), self, self.canvasStrings.UPDATE_MEASUREMENT)
            self.myFontProcessor = self.updateMyFontProcessor
            self.menuBehavior.onDisplayChangeEvent(self, displayChangeEvent)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT, e)
    

    # throws Exception
    def updateMenuFromEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        formType: FormType = FormTypeFactory.getInstance().getFormType()
        rectangle: Rectangle = self.formUtil.createFormRectangle()
        self.menuForm.init(rectangle, formType)
        if self.currentTouchInputFactory != NoButtonsTouchInputFactory.getInstance():
            self.touchButtonFactory.toggle(self.isPaused(), self.currentTouchInputFactory.getList())
        self.myFontProcessor = self.updateMyFontProcessor
    

    # throws Exception
    def processSleep(self) -> None:
        super().processSleep()
        if AllBinaryMediaManager.update():
            if not self.primaryPlayerQueue.process():
                self.secondaryPlayerQueue.process()
        if self.menuInputProcessor.processInputList() != -1:
            self.runnableCanvasRefreshHelper.process()
    

    # throws Exception
    def initPopupMenu(self) -> None:
        from org.allbinary.game.displayable.canvas.NoMenuInputProcessor import NoMenuInputProcessor
        from org.allbinary.game.displayable.canvas.BasicPopupMenuPaintable import BasicPopupMenuPaintable
        from org.allbinary.game.displayable.canvas.PopupMenuInputProcessor import PopupMenuInputProcessor
        if self.popupMenuInputProcessor == NoMenuInputProcessor.getInstance():
            features: Features = Features.getInstance()
            popupMenuRectangle: Rectangle = self.myFormUtil.getPopupMenuRectangle()
            if features.isFeature(self.touchFeatureFactory.TOUCH_ENABLED):
                self.setOpenMenuPaintable(BasicPopupMenuPaintable(popupMenuRectangle, self.gameLayerManager.getBackgroundBasicColor(), self.gameLayerManager.getForegroundBasicColor()))
                self.setPopupMenuInputProcessor(PopupMenuInputProcessor(BasicArrayListD(), -1, self, popupMenuRectangle))
        else:
            pass
    

    def initMenu(self) -> None:
        try:
            self.menuBehavior.initMenu(self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "initMenu", e)
    

    # throws Exception
    def initMenu2(self) -> None:
        from org.allbinary.game.displayable.canvas.GameLimitedCommandTextItemArrayFactory import GameLimitedCommandTextItemArrayFactory
        from org.allbinary.game.displayable.canvas.PopupCommandFormInputProcessor import PopupCommandFormInputProcessor
        self.closeMenu()
        formType: FormType = FormTypeFactory.getInstance().getFormType()
        gameLimitedCommandTextItemArrayFactory: GameLimitedCommandTextItemArrayFactory = GameLimitedCommandTextItemArrayFactory.getInstance()
        commandTextItemArrayFactory: CommandTextItemArrayFactory = gameLimitedCommandTextItemArrayFactory.getCommandTextItemArrayFactory()
        items: list[ABCustomItem] = commandTextItemArrayFactory.getInstance(self.getCommandStack(), self.gameLayerManager.getBackgroundBasicColor(), self.gameLayerManager.getForegroundBasicColor())
        rectangle: Rectangle = self.formUtil.createFormRectangle()
        self.setMenuForm(CommandCurrentSelectionFormFactory.getInstance(StringUtil.getInstance().EMPTY_STRING, items, rectangle, formType, 25, False, self.gameLayerManager.getBackgroundBasicColor(), self.gameLayerManager.getForegroundBasicColor()))
        scrollSelectionForm: ScrollSelectionForm = self.getMenuForm()
        features: Features = Features.getInstance()
        if features.isFeature(self.touchFeatureFactory.TOUCH_ENABLED):
            self.mainMenuInputProcessor = PopupCommandFormInputProcessor(BasicArrayListD(), -1, self, scrollSelectionForm, self.getPopupMenuInputProcessor())
        else:
            pass
        self.setMenuInputProcessor(self.getPopupMenuInputProcessor())
        if scrollSelectionForm != ScrollSelectionFormNoneFactory.getInstance():
            self.setFormPaintable(FormPaintable(scrollSelectionForm))
        else:
            pass
        self.closeMenu()
    

    def updateMenu(self) -> None:
        try:
            self.menuBehavior.updateMenu(self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "initMenu", e)
    

    # throws Exception
    def updateMenu2(self) -> None:
        from org.allbinary.game.displayable.canvas.GameLimitedCommandTextItemArrayFactory import GameLimitedCommandTextItemArrayFactory
        scrollSelectionForm: ScrollSelectionForm = self.getMenuForm()
        scrollSelectionForm.deleteAll()
        gameLimitedCommandTextItemArrayFactory: GameLimitedCommandTextItemArrayFactory = GameLimitedCommandTextItemArrayFactory.getInstance()
        commandTextItemArrayFactory: CommandTextItemArrayFactory = gameLimitedCommandTextItemArrayFactory.getCommandTextItemArrayFactory()
        items: list[ABCustomItem] = commandTextItemArrayFactory.getInstance(self.getCommandStack(), self.gameLayerManager.getBackgroundBasicColor(), self.gameLayerManager.getForegroundBasicColor())
        size: int = len(items)
        for index in range(0, size):
            scrollSelectionForm.append(items[index])
        formType: FormType = FormTypeFactory.getInstance().getFormType()
        rectangle: Rectangle = self.formUtil.createFormRectangle()
        scrollSelectionForm.init(rectangle, formType)
    

    def pause(self) -> None:
        with self._lock:
            return self._pause_unlocked()

    def _pause_unlocked(self) -> None:
        self.gameBehavior.pause(self)
        self.closeMenu()
        super().pause()
        self.touchButtonFactory.toggle(self.isPaused(), BasicArrayListUtil.getInstance().getImmutableInstance())
        self.tsUtil.gc()
    

    def unPause(self) -> None:
        with self._lock:
            return self._unPause_unlocked()

    def _unPause_unlocked(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.gameStrings.UNPAUSE)
        self.closeMenu()
        self.tsUtil.gc()
        super().unPause()
        self.touchButtonFactory.toggle(self.isPaused(), BasicArrayListUtil.getInstance().getImmutableInstance())
        self.gameBehavior.unPause(self)
    

    def isPausable(self) -> bool:
        from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
        if CurrentDisplayableFactory.getInstance().getUsedRunnable() == NullWaitGameRunnable.getInstance():
            return True
        else:
            return False
    

    # throws Exception
    def popupMenu(self) -> None:
        self.menuBehavior.popupMenu(self)
    

    # throws Exception
    def popupMenu2(self) -> None:
        self.primaryPlayerQueue.add(SelectSound.getInstance())
        self.setMenuPaintable(self.getFormPaintable())
        self.setMenuInputProcessor(self.mainMenuInputProcessor)
        self.basicMotionGesturesHandler.addListenerInterface(self.mainMenuInputProcessor)
        self.gameKeyEventHandler.addListener(self.mainMenuInputProcessor)
    

    # throws Exception
    def toggleMenu(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.gameStrings.TOGGLE_MENU)
        if self.getMenuPaintable() == self.getOpenMenuPaintable():
            self.pause()
            self.updateMenu()
            self.popupMenu()
        elif self.getMenuPaintable() == self.getFormPaintable():
            self.primaryPlayerQueue.add(SelectSound.getInstance())
            self.unPause()
    

    def closeMenu(self) -> None:
        self.menuBehavior.closeMenu(self)
    

    def closeMenu2(self) -> None:
        self.setMenuPaintable(self.getOpenMenuPaintable())
        self.basicMotionGesturesHandler.removeListener(self.mainMenuInputProcessor)
        self.gameKeyEventHandler.removeListener(self.mainMenuInputProcessor)
        self.setMenuInputProcessor(self.getPopupMenuInputProcessor())
    

    def open(self) -> None:
        self.basicMotionGesturesHandler.addListenerInterface(self.menuInputProcessor)
        self.gameKeyEventHandler.addListener(self.menuInputProcessor)
    

    def close(self) -> None:
        self.basicMotionGesturesHandler.removeListener(self.menuInputProcessor)
        self.gameKeyEventHandler.removeListener(self.menuInputProcessor)
        self.primaryPlayerQueue.clear()
        self.secondaryPlayerQueue.clear()
    

    # throws Exception
    def processorInit(self) -> None:
        self.setMainStateProcessor(Processor.getInstance())
        self.setProcessGameProcessorInit()
    

    def setProcessGameProcessorInit(self) -> None:
        from org.allbinary.game.displayable.canvas.GameProcessor import GameProcessor
        self.setProcessGameProcessor(GameProcessor(self))
    

    def initSpecialPaint(self) -> None:
        self.menuBehavior.initSpecialPaint(self)
    

    # throws Exception
    def init(self, gameLayerManager: AllBinaryGameLayerManager, buffered: bool) -> None:
        from org.allbinary.game.displayable.canvas.CheatGameInputProcessor import CheatGameInputProcessor
        from org.allbinary.game.displayable.canvas.EndGameProcessor import EndGameProcessor
        from org.allbinary.game.displayable.canvas.StartIntermissionProcessor import StartIntermissionProcessor
        from org.allbinary.game.displayable.canvas.EndGamePaintable import EndGamePaintable
        self.gameStateTimeHelper.setStartTimeTNT()
        self.setHighScoreSubmitted(False)
        self.setLayerManager(gameLayerManager)
        if not buffered:
            BUFF_MESSAGE: str = "XXX Not Buffering Causes Concurrency Issues XXX"
            self.logUtil.putF(BUFF_MESSAGE, self, self.commonStrings.CONSTRUCTOR)
        else:
            raise Exception("Buffering is disabled")
        self.setGameInputProcessor(Processor.getInstance())
        features: Features = Features.getInstance()
        if features.isFeature(GameFeatureFactory.getInstance().CHEATING):
            self.isCheating = True
            self.cheatProcessor = CheatGameInputProcessor(self)
            self.gameKeyEventHandler.addListener(self.cheatProcessor)
        else:
            self.isCheating = False
            self.cheatProcessor = NoPlayerGameInput.getInstance()
        self.realEndGameProcessor = EndGameProcessor(self)
        self.setEndGameProcessor(Processor.getInstance())
        self.realStartIntermissionProcessor = StartIntermissionProcessor(self)
        self.startIntermissionProcessor = Processor.getInstance()
        self.setEndGameStatePaintable(EndGamePaintable(self))
        self.setEndGamePaintable(NullPaintable.getInstance())
        self.setIntermissionPaintable(NullPaintable.getInstance())
        self.getStartIntermissionInterface().setListener(self)
    

    def notifyIntermission(self, enable: bool) -> None:
        if enable:
            self.startIntermissionProcessor = self.realStartIntermissionProcessor
        else:
            self.startIntermissionProcessor = Processor.getInstance()
        if enable:
            self.setIntermissionPaintable(self.getStartIntermissionPaintable())
        else:
            self.setIntermissionPaintable(NullPaintable.getInstance())
    

    # throws Exception
    def mediaInit(self) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
    

    # throws Exception
    def initConfigurable(self, abeClientInformation: AbeClientInformationInterface) -> None:
        with self._lock:
            return self._initConfigurable_unlocked(abeClientInformation)

    def _initConfigurable_unlocked(self, abeClientInformation: AbeClientInformationInterface) -> None:
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.addNormalPortion(50, "Setting Configurables")
        GameInitializationUtil.getInstance().initGame(abeClientInformation, self, self.gameInitializationInterfaceFactoryInterface)
        gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
        changedGameFeatureListener: ChangedGameFeatureListener = ChangedGameFeatureListener.getInstance()
        if changedGameFeatureListener.isChangedFeature(gameFeatureFactory.SOUND):
            features: Features = Features.getInstance()
            self.logUtil.putF(str(StringMaker().append("Sound Changing To: ").appendboolean(features.isFeature(gameFeatureFactory.SOUND))), self, "initConfigurable")
            self.mediaInit()
            changedGameFeatureListener.remove(gameFeatureFactory.SOUND)
        sensorFeatureFactory: SensorFeatureFactory = SensorFeatureFactory.getInstance()
        if changedGameFeatureListener.isChangedFeature(sensorFeatureFactory.ORIENTATION_SENSORS) or changedGameFeatureListener.isChangedFeature(sensorFeatureFactory.NO_ORIENTATION) or changedGameFeatureListener.isChangedFeature(sensorFeatureFactory.SIMULATED_ORIENTATION_SENSORS):
            changedGameFeatureListener.remove(sensorFeatureFactory.NO_ORIENTATION)
            changedGameFeatureListener.remove(sensorFeatureFactory.ORIENTATION_SENSORS)
            changedGameFeatureListener.remove(sensorFeatureFactory.SIMULATED_ORIENTATION_SENSORS)
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        self.loadResourceLoadingLevel(resourceLoadingLevelFactory.LOAD_GAME)
    

    # throws Exception
    def initApp(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.initConfigurable(abeClientInformation)
        self.processorInit()
        self.sensorGameUpdateProcessor.process(self.gameLayerManager)
        self.sensorGameUpdateProcessor.sendNotifications(self.gameLayerManager)
        self.initTouch()
    

    # throws Exception
    def initTouch(self) -> None:
        gameInitializedEvent: GameInitializedEvent = GameInitializationUtil.getInstance().EVENT
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        gameInitializedEvent.setResourceLoadingLevel(resourceLoadingLevelFactory.LOAD_TOUCH)
        GameInitializedEventHandler.getInstance().fireEvent(gameInitializedEvent)
        self.touchButtonFactory.defaultList()
        self.updateTouch()
        self.postInitTouch()
    

    # throws Exception
    def updateCurrentTouchInputFactory(self, nextTouchInput: BaseTouchInput) -> None:
        if nextTouchInput != self.currentTouchInputFactory:
            self.currentTouchInputFactory = nextTouchInput
            PreLogUtil.put(str(self.currentTouchInputFactory), self, self.gameInputStrings.UDPATE_CURRENT_TOUCH_INPUT_FACTORY)
            self.touchButtonFactory.toggle(self.isPaused(), self.currentTouchInputFactory.getList())
    

    # throws Exception
    def updateTouch(self) -> None:
        self.gameBehavior.updateTouch(self)
    

    # throws Exception
    def updateTouch2(self) -> None:
        features: Features = Features.getInstance()
        if features.isFeature(self.touchFeatureFactory.AUTO_HIDE_SHOW_SCREEN_BUTTONS):
            if self.gameLayerManager.getGameInfo().getCurrentLevel() - self.getStartLevel() == 1:
                self.setTouchPaintableP(NullPaintable.getInstance())
    

    # throws Exception
    def postInitTouch(self) -> None:
        self.setTouchButtonsPaintable(TouchButtonsPaintableFactory.getInstance(self.gameLayerManager.getForegroundBasicColor()))
        self.updateScreenButtonPaintable()
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.addCommands()
        self.setCommandListener(cmdListener)
    

    def addCommands(self) -> None:
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        myCommandsFactory: MyCommandsFactory = MyCommandsFactory.getInstance()
        if DebugFactory.getInstance() != NoDebug.getInstance():
            self.addCommand(gameCommandsFactory.START_TRACE)
        self.addCommand(gameCommandsFactory.RESTART_COMMAND)
        self.addCommand(myCommandsFactory.PAUSE_COMMAND)
        self.addCommand(gameCommandsFactory.QUIT_COMMAND)
        isOverScan: bool = OperatingSystemFactory.getInstance().getOperatingSystemInstance().isOverScan()
        if J2MEUtil.isHTML():
            pass
        elif SWTUtil.isSWT:
            pass
        elif not isOverScan:
            if TouchScreenFactory.getInstance().isTouch() and InGameFeatures().isAny():
                self.addCommand(InGameOptionsForm.DISPLAY)
            self.addCommand(gameCommandsFactory.SAVE)
            self.addCommand(gameCommandsFactory.DISPLAY_LOAD_FORM)
    

    def itemStateChanged(self, item: Item) -> None:
        try:
            itemLabel: str = item.getLabel()
            self.logUtil.putF(str(StringMaker().append(self.commonLabels.ITEM_LABEL).append(itemLabel)), self, "itemStateChanged")
            if isinstance(item, ChoiceGroup):
                gameFeatureUtil: GameFeatureUtil = GameFeatureUtil.getInstance()
                if gameFeatureUtil.isExclusive(itemLabel):
                    gameFeatureUtil.updateExclusiveForChoiceGroup(item)
                else:
                    gameFeatureUtil.updateMultiple(item)
            self.sensorGameUpdateProcessor.process(self.gameLayerManager)
            self.updateTouch()
            self.updateScreenButtonPaintable()
            self.sensorGameUpdateProcessor.sendNotifications(self.gameLayerManager)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "itemStateChanged", e)
    

    # throws Exception
    def updateScreenButtonPaintable(self) -> None:
        self.gameBehavior.updateScreenButtonPaintable(self)
    

    def updateScreenButtonPaintable2(self) -> None:
        features: Features = Features.getInstance()
        if features.isFeature(self.touchFeatureFactory.AUTO_HIDE_SHOW_SCREEN_BUTTONS):
            self.setTouchPaintableP(self.getTouchButtonsPaintable())
            self.setStartLevel(self.gameLayerManager.getGameInfo().getCurrentLevel())
        elif features.isFeature(self.touchFeatureFactory.SHOW_SCREEN_BUTTONS):
            self.setTouchPaintableP(self.getTouchButtonsPaintable())
        elif features.isFeature(self.touchFeatureFactory.HIDE_SCREEN_BUTTONS):
            self.setTouchPaintableP(NullPaintable.getInstance())
        else:
            self.setTouchPaintableP(NullPaintable.getInstance())
    

    def getLayerManager(self) -> AllBinaryGameLayerManager:
        return self.gameLayerManager
    

    def setLayerManager(self, layerManager: AllBinaryGameLayerManager) -> None:
        self.gameLayerManager = layerManager
    

    def isGameOver(self) -> bool:
        with self._lock:
            return self._isGameOver_unlocked()

    def _isGameOver_unlocked(self) -> bool:
        return self.gameOver
    

    def setGameOver(self, gameOver: bool) -> None:
        with self._lock:
            return self._setGameOver_unlocked(gameOver)

    def _setGameOver_unlocked(self, gameOver: bool) -> None:
        self.gameOver = gameOver
    

    # throws Exception
    def processGameOver(self) -> None:
        PreLogUtil.put(self.commonStrings.START, self, self.gameStrings.SET_GAME_OVER)
        self.setGameOver(True)
        self.removePauseCommand()
        self.setGameState(self.gameStateFactory.SHOW_END_RESULT_GAME_STATE)
        self.setEndGamePaintable(self.getEndGameStatePaintable())
    

    def isHighScoreSubmitted(self) -> bool:
        return self.highScoreSubmitted
    

    # throws Exception
    def setHighScoreSubmitted(self, highScoreSubmitted: bool) -> None:
        self.highScoreSubmitted = highScoreSubmitted
        if highScoreSubmitted:
            self.highScoresHelper.setSelectedHighScores(NullHighScoresSingletonFactory.getInstance())
        self.logUtil.putF(str(StringMaker().append("isHighScoreSubmitted: ").appendboolean(highScoreSubmitted)), self, "setHighScoreSubmitted")
    

    def getGameState(self) -> GameState:
        return self.gameState
    

    # throws Exception
    def setGameState(self, gameState: GameState) -> None:
        self.logUtil.putF(str(StringMaker().append(self.gameStrings.GAME_STATE).append(self.stringUtil.toString(gameState))), self, self.gameStrings.SET_GAME_STATE)
        self.gameState = gameState
        self.gameStateTimeHelper.setStartTimeTNT()
        self.updateEndGameProcessor()
        self.updateGameKeyEventProcessor()
        self.gameBehavior.setGameState(self)
    

    # throws Exception
    def updateGameState(self) -> None:
        gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
        gameAdState.processAdState(self.gameState, self.gameLayerManager.getGameInfo().getGameType())
        if self.gameState != self.gameStateFactory.PLAYING_GAME_STATE:
            gameAdState.processPageAdState()
    

    def updateGameKeyEventProcessor(self) -> None:
        if self.getGameState() != self.gameStateFactory.PLAYING_GAME_STATE or self.isCheating:
            pass
        else:
            pass
    

    def removeAllGameKeyInputListenersOnBuild(self) -> None:
        self.removeAllGameKeyInputListeners()
    

    def removeAllGameKeyInputListeners(self) -> None:
        self.gameBehavior.removeAllGameKeyInputListeners(self)
    

    def removeAllGameKeyInputListeners2(self) -> None:
        self.logUtil.putF("Remove PlayerInput Listeners", self, "removeAllGameKeyInputListeners")
        for index in range(self.localPlayerGameInputList.size() - 1, 0 - 1, -1):
            playerGameInput: PlayerGameInput = self.localPlayerGameInputList.get(index)
            self.removeKeyInputListener(playerGameInput)
            playerGameInput.removeNonAIInputGameKeyEvents()
    

    def removeKeyInputListener(self, playerGameInput: PlayerGameInput) -> None:
        self.gameKeyEventHandler.removeListener(playerGameInput)
    

    # throws Exception
    def updateEndGameProcessor(self) -> None:
        self.gameBehavior.updateEndGameProcessor(self)
    

    # throws Exception
    def updateEndGameProcessor2(self) -> None:
        if self.getGameState() == self.gameStateFactory.SHOW_END_RESULT_GAME_STATE or self.getGameState() == self.gameStateFactory.SHOW_HIGH_SCORE_GAME_STATE:
            self.setEndGameProcessor(self.realEndGameProcessor)
        else:
            self.setEndGameProcessor(Processor.getInstance())
    

    # throws Exception
    def buildGameInit(self, isPortion: bool) -> None:
        pass
    

    # throws Exception
    def cleanupGame(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CLEANUP)
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.addNormalPortion(10, "Cleaning Up")
        self.primaryPlayerQueue.clear()
        self.secondaryPlayerQueue.clear()
        GameLevelDisplayChangeEventListenersFactory.getInstance().clear()
    

    # throws Exception
    def loadResourceLoadingLevel(self, resourceLoadingLevel: ResourceLoadingLevel) -> None:
        gameInitializedEvent: GameInitializedEvent = GameInitializationUtil.getInstance().EVENT
        gameInitializedEvent.setResourceLoadingLevel(resourceLoadingLevel)
        GameInitializedEventHandler.getInstance().fireEvent(gameInitializedEvent)
    

    # throws Exception
    def loadResources(self, level: int) -> None:
        gameInitializedEvent: GameInitializedEvent = GameInitializationUtil.getInstance().EVENT
        gameInitializedEvent.setLevel(level)
        GameInitializedEventHandler.getInstance().fireEvent(gameInitializedEvent)
    

    # throws Exception
    def updateColor(self) -> None:
        pass
    

    # throws Exception
    def buildGame(self, portion: int) -> None:
        self.screenCapture.endRecording()
        self.screenCapture.startRecording()
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        features: Features = Features.getInstance()
        progressCanvas.addNormalPortion(portion, "Generic Build")
        self.removeAllGameKeyInputListenersOnBuild()
        self.updateTouch()
        progressCanvas.addNormalPortion(portion, "High Scores")
        self.highScoresFactoryInterface.fetchHighScores(self.gameLayerManager.getGameInfo(), self.highScoresHelper)
        self.setHighScoresPaintable(NullPaintable.getInstance())
        progressCanvas.addNormalPortion(portion, "Finishing.")
        self.getEndGameInfoP().update(self.getLayerManager().getGameInfo(), self)
        self.isSingleKeyRepeatableProcessing = features.isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_REPEAT_PRESS)
        self.setGameOver(False)
        progressCanvas.addNormalPortion(portion, "Finishing..")
        self.updateColor()
        self.getStartIntermissionPaintable().update()
        if not self.isRunningInAnotherThread():
            return
        progressCanvas.addNormalPortion(portion, "Finishing...")
        if self.isMainCanvas() or not self.isInitialized():
            if features.isFeature(MainFeatureFactory.getInstance().LOAD_ONDEMAND):
                if self.getCustomCommandListener() is not None:
                    progressCanvas.end()
            else:
                progressCanvas.end()
            self.setInitialized(True)
        if self.getCustomCommandListener() == NullCommandListener.NULL_COMMAND_LISTENER:
            self.logUtil.putF("Show Game Paintable in DemoCanvas Thread", self, self.BUILD_GAME)
            self.gameCanvasStartListener.showGamePaintable()
        else:
            self.logUtil.putF("No GameCanvasStartListener", self, self.BUILD_GAME)
        self.colorFillPaintable.setBasicColorP(self.gameLayerManager.getBackgroundBasicColor())
        self.gameBehavior.buildGame(self)
    

    def buildGame2(self) -> None:
        PreLogUtil.put(str(StringMaker().append(self.gameInputStrings.ENABLE_PLAYER_GAME_INPUTS).appendint(self.localPlayerGameInputList.size())), self, self.BUILD_GAME)
        playerGameInput: PlayerGameInput = None
        for index in range(self.localPlayerGameInputList.size() - 1, 0 - 1, -1):
            playerGameInput = self.localPlayerGameInputList.get(index)
            PreLogUtil.put(str(StringMaker().append(self.gameInputStrings.ENABLE_PLAYER_GAME_INPUT).append(str(playerGameInput))), self, self.BUILD_GAME)
            playerGameInput.removeNonAIInputGameKeyEvents()
            self.addKeyInputListener(playerGameInput)
    

    def addKeyInputListener(self, playerGameInput: PlayerGameInput) -> None:
        GameKeyEventHandler.getInstance().addListenerForPlayer(playerGameInput, playerGameInput.getPlayerInputId())
    

    def setGameCanvasStartListener(self, gameCanvasStartListener: DemoPaintableInterface) -> None:
        self.gameCanvasStartListener = gameCanvasStartListener
    

    # throws Exception
    def loadState(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.LOAD)
        hashtable: ABHashtable[object, object] = self.getLoadStateHashtable()
        if hashtable is not None and hashtable.size() > 0:
            levelAsString: str = hashtable.get(GameInfo.LEVEL_NAME)
            level: int = int(str(levelAsString))
            gameInfo: GameInfo = self.gameLayerManager.getGameInfo()
            gameInfo.setCurrentLevel(level)
    

    # throws Exception
    def getLoadStateHashtable(self) -> ABHashtable[object, object]:
        self.logUtil.putF(str(StringMaker().append(self.commonLabels.START_LABEL).append(self.stringUtil.toString(self.hashtable))), self, "getLoadStateHashtable")
        return self.hashtable
    

    def setLoadStateHashtable(self, hashtable: ABHashtable[object, object]) -> None:
        self.logUtil.putF(str(StringMaker().append(self.commonLabels.START_LABEL).append(self.stringUtil.toString(hashtable))), self, "setLoadStateHashtable")
        self.hashtable = hashtable
    

    def getCurrentStateHashtable(self) -> ABHashtable[object, object]:
        hashtable: ABHashtable[object, object] = self.stdUtil.createHashtable()
        level: int = self.gameLayerManager.getGameInfo().getCurrentLevel()
        hashtable.put(str(GameInfo.LEVEL_NAME), str(level))
        self.logUtil.putF(str(StringMaker().append("End: ").append(self.stringUtil.toString(hashtable))), self, "getCurrentStateHashtable")
        return hashtable
    

    def paintGameOver(self, graphics: Graphics) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
    

    def draw(self, graphics: Graphics) -> None:
        self.colorFillPaintable.paint(graphics)
        self.basicSetColorUtil.setBasicColorP(graphics, self.gameLayerManager.getForegroundBasicColor())
        self.gameSpecificPaintable.paint(graphics)
    

    def clear(self, graphics: Graphics) -> None:
        self.colorFillPaintable.paint(graphics)
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        self.baseGameStatistics.nextRefresh()
        self.draw(graphics)
        self.menuPaintable.paint(graphics)
        self.progressPaintable.paint(graphics)
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    # throws Exception
    def processEndLevelIntermissionGameState(self) -> None:
        pass
    

    def nonBotPaint(self, graphics: Graphics) -> None:
        self.endGamePaintable.paint(graphics)
        self.intermissionPaintable.paint(graphics)
        self.paintIntermission(graphics)
        self.touchPaintable.paint(graphics)
    

    def paintIntermission(self, graphics: Graphics) -> None:
        pass
    

    def keyPressed(self, keyCode: int) -> None:
        self.keyPressedByDevice(keyCode, 0)
    

    def keyReleased(self, keyCode: int) -> None:
        self.keyReleasedByDevice(keyCode, 0)
    

    def keyRepeated(self, keyCode: int) -> None:
        self.keyRepeatedByDevice(keyCode, 0)
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.inputProcessor.keyPressedByDevice(keyCode, deviceId)
    

    def keyRepeatedByDevice(self, keyCode: int, deviceId: int) -> None:
        if self.isSingleKeyRepeatableProcessing:
            self.inputProcessor.keyPressedByDevice(keyCode, deviceId)
    

    def keyReleasedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.inputProcessor.keyReleasedByDevice(self, keyCode, deviceId)
    

    # throws Exception
    def handleRawKey(self, keyCode: int, deviceId: int, repeated: bool) -> None:
        pass
    

    def endProgress(self, isProgress: bool) -> int:
        portion: int = 30
        if isProgress and self.isMainCanvas():
            myCommandsFactory: MyCommandsFactory = MyCommandsFactory.getInstance()
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            progressCanvas.start()
            self.getCustomCommandListener().commandAction(myCommandsFactory.SET_DISPLAYABLE, progressCanvas)
            portion = 4
        return portion
    

    # throws Exception
    def processPlayingGame(self) -> None:
        self.cheatProcessor.update()
        self.sensorGameUpdateProcessor.getInputSensor().update()
        self.gameInputProcessor.process()
        self.gameLayerManager.process()
        self.startIntermissionProcessor.process()
    

    # throws Exception
    def threadInit(self) -> None:
        pass
    

    # throws Exception
    def processGame(self) -> None:
        super().process()
        if AllBinaryMediaManager.update():
            if not self.primaryPlayerQueue.process():
                self.secondaryPlayerQueue.process()
        self.mainStateProcessor.process()
        self.menuInputProcessor.processInputList()
        self.endGameProcessor.process()
        self.baseGameStatistics.nextFrame()
    

    def notifyDonePainting(self) -> None:
        with self._lock:  # synchronized (self)
            self.threadObjectUtil.notifyObject(self)
    

    # throws Exception
    def shouldWait(self) -> None:
        features: Features = Features.getInstance()
        if AndroidUtil.isAndroid():
            pass
        elif features.isFeature(self.openGLFeatureFactory.OPENGL_2D):
            pass
        else:
            if features.isDefault(self.openGLFeatureFactory.OPENGL):
                openGLImageSpecificFactory: OpenGLImageSpecificFactory = OpenGLImageSpecificFactory.getInstance()
                while openGLImageSpecificFactory.updating:
                    time.sleep((self.YIELD_SLEEP) / 1000)
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START_RUNNABLE, self, self.commonStrings.RUN)
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            progressCanvas.addNormalPortion(50, "Game Thread")
            self.setCurrentThread()
            self.setRunning(True)
            if self.getCustomCommandListener() == NullCommandListener.NULL_COMMAND_LISTENER:
                time.sleep((self.YIELD_SLEEP) / 1000)
            self.shouldWait()
            self.threadInit()
            if self.getCustomCommandListener() == NullCommandListener.NULL_COMMAND_LISTENER:
                time.sleep((self.YIELD_SLEEP) / 1000)
            self.open()
            gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
            gameAdState.init()
            gameAdState.setGameIsReady(True)
            self.gameBehavior.run(self)
            self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
    

    # throws Exception
    def run2(self) -> None:
        features: Features = Features.getInstance()
        if features.isDefault(self.openGLFeatureFactory.OPENGL_AS_GAME_THREAD) or J2MEUtil.isHTML():
            if features.isDefault(self.openGLFeatureFactory.OPENGL_AS_GAME_THREAD):
                self.logUtil.putF(self.openGLFeatureFactory.OPENGL_AS_GAME_THREAD.getName(), self, self.commonStrings.RUN)
            if J2MEUtil.isHTML():
                self.logUtil.putF(GraphicsStrings.getInstance().HTML, self, self.commonStrings.RUN)
            currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
            currentDisplayableFactory.setRunnable(self.gameRunnable)
            currentDisplayableFactory.setDisplayable(self)
            OpenGLThreadUtil.getInstance().onResume()
        elif features.isDefault(self.openGLFeatureFactory.OPENGL_AND_GAME_HAVE_DIFFERENT_THREADS):
            self.logUtil.putF(self.openGLFeatureFactory.OPENGL_AND_GAME_HAVE_DIFFERENT_THREADS.getName(), self, self.commonStrings.RUN)
            OpenGLThreadUtil.getInstance().onResume()
            while self.isRunning():
                self.run3()
            self.end()
        else:
            self.logUtil.putF("this thread", self, self.commonStrings.RUN)
            while self.isRunning():
                self.run3()
            self.end()
    

    # throws Exception
    def run3(self) -> None:
        self.loopTimeHelper.setStartTime(self.gameTickTimeDelayHelper.setStartTime())
        self.gameTickDisplayInfoSingleton.update()
        self.processGame()
        self.processLoopSleep()
    

    def setRunning(self, running: bool) -> None:
        super().setRunning(running)
        try:
            features: Features = Features.getInstance()
            if running:
                pass
            else:
                if features.isDefault(self.openGLFeatureFactory.OPENGL) or SWTUtil.isSWT:
                    if self.gameLayerManager.getGameInfo().getGameType() != self.gameTypeFactory.BOT:
                        currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
                        currentDisplayableFactory.clearRunnable()
                    self.end()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.SET_RUNNING, e)
    

    # throws Exception
    def end(self) -> None:
        self.screenCapture.endRecording()
        self.baseGameStatistics.add(str(StringMaker().append(str(self.baseGameStatistics)).append(CommonSeps.getInstance().NEW_LINE)))
        self.baseGameStatistics.init()
        self.gameKeyEventHandler.removeListener(self.cheatProcessor)
        self.close()
        self.removeAllGameKeyInputListeners()
        self.endGameThread()
    

    # throws Exception
    def endGameThread(self) -> None:
        DisplayChangeEventHandler.getInstance().removeListener(self)
        GameLevelDisplayChangeEventListenersFactory.getInstance().clear()
        gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
        gameAdState.notPlayingAdState()
    

    def createHighScore(self, score: int) -> HighScore:
        gameInfo: GameInfo = self.gameLayerManager.getGameInfo()
        return HighScore(0, "NONE", GameInfo(gameInfo.getGameType(), gameInfo.getGameMode(), PlayerTypesFactory.getInstance().PLAYER_TYPE_ONE, 0, 0), score)
    

    # throws Exception
    def setHighScore(self, abeClientInformation: AbeClientInformationInterface, name: str, score: int, autoSubmit: bool, isLast: bool) -> None:
        self.gameBehavior.setHighScore(abeClientInformation, self, name, score, autoSubmit, isLast)
    

    # throws Exception
    def setHighScore2(self, abeClientInformation: AbeClientInformationInterface, name: str, score: int, autoSubmit: bool, isLast: bool) -> None:
        from org.allbinary.game.displayable.canvas.SaveHighScoreRunnable import SaveHighScoreRunnable
        highScore: HighScore = self.createHighScore(score)
        textBox: HighScoreTextBox = HighScoreTextBox(self.highScoresFactoryInterface, self.highScoresHelper, abeClientInformation, self.gameLayerManager.getGameInfo(), self.getCustomCommandListener(), name, highScore, self.gameLayerManager.getBackgroundBasicColor(), self.gameLayerManager.getForegroundBasicColor())
        if isLast:
            self.getCustomCommandListener().commandAction(GameCommandsFactory.getInstance().SET_MENU_DISPLAYABLE, textBox)
        if autoSubmit:
            class SaveHighScoreRunnable(object):
                _lock = threading.RLock()

                def _init_fields(self) -> None:
                    self.progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()

                def __init__(self) -> None:
                    self._init_fields()
                

                def run(self) -> None:
                    logUtil: LogUtil = LogUtil.getInstance()
                    try:
                        if self.isLast:
                            self.textBox.submit()
                        else:
                            self.textBox.saveHighScore()
                    except Exception as e:
                        commonStrings: CommonStrings = CommonStrings.getInstance()
                        logUtil.put(commonStrings.EXCEPTION, self, "run", e)
                        self.progressCanvas.end()
            SecondaryThreadPool.getInstance().runTask(SaveHighScoreRunnable())
    

    def getGameStateTimeHelper(self) -> TimeDelayHelper:
        return self.gameStateTimeHelper
    

    def setInitialized(self, initialized: bool) -> None:
        self.initialized = initialized
    

    def isInitialized(self) -> bool:
        return self.initialized
    

    def getSourceId(self) -> int:
        return AllBinaryGameCanvas.id
    

    def setProgressPaintable(self, paintable: PaintableInterface) -> None:
        self.progressPaintable = paintable
    

    def getStartIntermissionInterface(self) -> IntermissionInterface:
        return self.startIntermissionInterface
    

    def getEndLevelIntermissionInterface(self) -> IntermissionInterface:
        return self.endLevelIntermissionInterface
    

    def setTouchPaintableP(self, paintable: Paintable) -> None:
        self.touchPaintable = paintable
    

    def getTouchPaintableP(self) -> Paintable:
        return self.touchPaintable
    

    def setEndGamePaintable(self, endGamePaintable: Paintable) -> None:
        self.endGamePaintable = endGamePaintable
    

    def getEndGamePaintable(self) -> Paintable:
        return self.endGamePaintable
    

    def setIntermissionPaintable(self, intermissionPaintable: Paintable) -> None:
        self.intermissionPaintable = intermissionPaintable
    

    def getIntermissionPaintable(self) -> Paintable:
        return self.intermissionPaintable
    

    def getEndGameInfoP(self) -> EndGameInfo:
        return self.endGameInfo
    

    def setHighScoresPaintable(self, highScoresPaintable: Paintable) -> None:
        self.highScoresPaintable = highScoresPaintable
    

    def getHighScoresPaintable(self) -> Paintable:
        return self.highScoresPaintable
    

    def getRealHighScoresPaintable(self) -> HighScoresPaintable:
        return self.realHighScoresPaintable
    

    def clearPlayerGameInputList(self) -> None:
        playerGameInput: PlayerGameInput = None
        for index in range(self.localPlayerGameInputList.size() - 1, 0 - 1, -1):
            playerGameInput = self.localPlayerGameInputList.get(index)
            self.gameKeyEventHandler.removeListener(playerGameInput)
        self.localPlayerGameInputList.clear()
    

    def addPlayerGameInput(self, playerGameInput: PlayerGameInput) -> None:
        self.localPlayerGameInputList.add(playerGameInput)
    

    def setMenuInputProcessor(self, menuInputProcessor: BasicMenuInputProcessor) -> None:
        self.menuInputProcessor = menuInputProcessor
    

    def getMenuInputProcessor(self) -> BasicMenuInputProcessor:
        return self.menuInputProcessor
    

    def getMenuForm(self) -> ScrollSelectionForm:
        return self.menuForm
    

    def setMenuForm(self, menuForm: ScrollSelectionForm) -> None:
        self.menuForm = menuForm
    

    def getStartLevel(self) -> int:
        return self.startLevel
    

    def setStartLevel(self, startLevel: int) -> None:
        self.startLevel = startLevel
    

    def setTouchButtonsPaintable(self, touchButtonsPaintable: Paintable) -> None:
        self.touchButtonsPaintable = touchButtonsPaintable
    

    def getTouchButtonsPaintable(self) -> Paintable:
        return self.touchButtonsPaintable
    

    def setGameInputProcessor(self, gameInputProcessor: Processor) -> None:
        self.gameInputProcessor = gameInputProcessor
    

    def getGameInputProcessor(self) -> Processor:
        return self.gameInputProcessor
    

    def setEndGameProcessor(self, endGameProcessor: Processor) -> None:
        self.endGameProcessor = endGameProcessor
    

    def getEndGameProcessor(self) -> Processor:
        return self.endGameProcessor
    

    def setEndGameStatePaintable(self, endGameStatePaintable: Paintable) -> None:
        self.endGameStatePaintable = endGameStatePaintable
    

    def getEndGameStatePaintable(self) -> Paintable:
        return self.endGameStatePaintable
    

    def setNonBotPaintableP(self, nonBotPaintable: Paintable) -> None:
        self.nonBotPaintable = nonBotPaintable
    

    def getNonBotPaintableP(self) -> Paintable:
        return self.nonBotPaintable
    

    def setStartIntermissionPaintable(self, startIntermissionPaintable: InitUpdatePaintable) -> None:
        self.startIntermissionPaintable = startIntermissionPaintable
    

    def getStartIntermissionPaintable(self) -> InitUpdatePaintable:
        return self.startIntermissionPaintable
    

    def setMainStateProcessor(self, mainStateProcessor: Processor) -> None:
        self.mainStateProcessor = mainStateProcessor
    

    def getMainStateProcessor(self) -> Processor:
        return self.mainStateProcessor
    

    def setProcessGameProcessor(self, processGameProcessor: Processor) -> None:
        self.processGameProcessor = processGameProcessor
    

    def getProcessGameProcessor(self) -> Processor:
        return self.processGameProcessor
    

    def setOpenMenuPaintable(self, openMenuPaintable: Paintable) -> None:
        self.openMenuPaintable = openMenuPaintable
    

    def getOpenMenuPaintable(self) -> Paintable:
        return self.openMenuPaintable
    

    def setPopupMenuInputProcessor(self, popupMenuInputProcessor: BasicMenuInputProcessor) -> None:
        self.popupMenuInputProcessor = popupMenuInputProcessor
    

    def getPopupMenuInputProcessor(self) -> BasicMenuInputProcessor:
        return self.popupMenuInputProcessor
    

    def getSensorGameUpdateProcessor(self) -> SensorGameUpdateProcessor:
        return self.sensorGameUpdateProcessor
    

    def getRawGameInputProcessor(self) -> InputProcessor:
        return self.rawGameInputProcessor
    

    def getRawInputProcessor(self) -> InputProcessor:
        return self.rawInputProcessor
    

    def setInputProcessor(self, inputProcessor: InputProcessor) -> None:
        self.inputProcessor = inputProcessor
    

    def getInputProcessor(self) -> InputProcessor:
        return self.inputProcessor
    

    def setMenuPaintable(self, menuPaintable: Paintable) -> None:
        self.menuPaintable = menuPaintable
    

    def getMenuPaintable(self) -> Paintable:
        return self.menuPaintable
    

    def setFormPaintable(self, formPaintable: Paintable) -> None:
        self.formPaintable = formPaintable
    

    def getFormPaintable(self) -> Paintable:
        return self.formPaintable
    

    def setGameSpecificPaintableP(self, gameSpecificPaintable: Paintable) -> None:
        self.gameSpecificPaintable = gameSpecificPaintable
    

    def getGameSpecificPaintableP(self) -> Paintable:
        return self.gameSpecificPaintable
    

    def isSingleThread(self) -> bool:
        return OpenGLFeatureUtil.getInstance().isAnyThreed() or SWTUtil.isSWT
    

    def isRunningInAnotherThread(self) -> bool:
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        if features.isDefault(openGLFeatureFactory.OPENGL_AS_GAME_THREAD):
            return True
        else:
            return self.isRunning()
    

    def getType(self) -> int:
        return AllBinaryGameCanvas.TYPE
# from javax.microedition.lcdui.ChoiceGroup import ChoiceGroup
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Item import Item
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.business.advertisement.GameAdStateFactory import GameAdStateFactory
from org.allbinary.canvas.BaseGameStatistics import BaseGameStatistics
from org.allbinary.canvas.GameStatisticsFactory import GameStatisticsFactory
from org.allbinary.canvas.Processor import Processor
from org.allbinary.debug.DebugFactory import DebugFactory
from org.allbinary.debug.NoDebug import NoDebug
from org.allbinary.game.GameAdState import GameAdState
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.GameStrings import GameStrings
from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.game.Intermission import Intermission
from org.allbinary.game.IntermissionInterface import IntermissionInterface
from org.allbinary.game.PlayerTypesFactory import PlayerTypesFactory
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.InGameFeatures import InGameFeatures
from org.allbinary.game.configuration.InGameOptionsForm import InGameOptionsForm
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.game.configuration.event.GameInitializedEvent import GameInitializedEvent
from org.allbinary.game.configuration.event.GameInitializedEventHandler import GameInitializedEventHandler
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.game.configuration.feature.GameFeatureUtil import GameFeatureUtil
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory
from org.allbinary.game.configuration.feature.TouchFeatureFactory import TouchFeatureFactory
from org.allbinary.game.displayable.GameLevelDisplayChangeEventListenersFactory import GameLevelDisplayChangeEventListenersFactory
from org.allbinary.game.init.BasicBuildGameInitializerFactory import BasicBuildGameInitializerFactory
from org.allbinary.game.init.GameInitializationUtil import GameInitializationUtil
from org.allbinary.game.input.GameInputStrings import GameInputStrings
from org.allbinary.game.input.InputProcessor import InputProcessor
from org.allbinary.game.input.NoPlayerGameInput import NoPlayerGameInput
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.SWTUtil import SWTUtil
from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable
from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
from org.allbinary.game.resource.ResourceLoadingLevel import ResourceLoadingLevel
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.game.score.HighScore import HighScore
from org.allbinary.game.score.HighScoresHelperBaseInterface import HighScoresHelperBaseInterface
from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
from org.allbinary.game.score.HighScoresPaintable import HighScoresPaintable
from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
from org.allbinary.game.score.displayable.HighScoreTextBox import HighScoreTextBox
from org.allbinary.game.state.GameState import GameState
from org.allbinary.game.state.GameStateFactory import GameStateFactory
from org.allbinary.graphics.GraphicsStrings import GraphicsStrings
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.ScreenCapture import ScreenCapture
from org.allbinary.graphics.ScreenCaptureFactory import ScreenCaptureFactory
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.displayable.GameTickDisplayInfoSingleton import GameTickDisplayInfoSingleton
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.displayable.event.DisplayChangeEventHandler import DisplayChangeEventHandler
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.form.CommandCurrentSelectionFormFactory import CommandCurrentSelectionFormFactory
from org.allbinary.graphics.form.FormPaintable import FormPaintable
from org.allbinary.graphics.form.FormType import FormType
from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.graphics.form.ScrollSelectionFormNoneFactory import ScrollSelectionFormNoneFactory
from org.allbinary.graphics.form.item.CommandTextItemArrayFactory import CommandTextItemArrayFactory
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.opengles.CurrentDisplayableFactory import CurrentDisplayableFactory
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.graphics.opengles.OpenGLThreadUtil import OpenGLThreadUtil
from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable
from org.allbinary.graphics.paint.NullInitUpdatePaintable import NullInitUpdatePaintable
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.image.opengles.OpenGLImageSpecificFactory import OpenGLImageSpecificFactory
from org.allbinary.input.gyro.SensorGameUpdateProcessor import SensorGameUpdateProcessor
from org.allbinary.input.gyro.SingleSensorGameUpdateProcessor import SingleSensorGameUpdateProcessor
from org.allbinary.input.motion.button.BaseTouchInput import BaseTouchInput
from org.allbinary.input.motion.button.NoButtonsTouchInputFactory import NoButtonsTouchInputFactory
from org.allbinary.input.motion.button.TouchButtonFactory import TouchButtonFactory
from org.allbinary.input.motion.button.TouchButtonsPaintableFactory import TouchButtonsPaintableFactory
from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.audio.AllBinaryMediaManager import AllBinaryMediaManager
from org.allbinary.media.audio.PlayerQueue import PlayerQueue
from org.allbinary.media.audio.PrimaryPlayerQueueFactory import PrimaryPlayerQueueFactory
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.media.audio.SelectSound import SelectSound
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.SecondaryThreadPool import SecondaryThreadPool
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.game.displayable.canvas.GameCanvasRunnable import GameCanvasRunnable
from org.allbinary.game.displayable.canvas.GameCanvasPauseRunnable import GameCanvasPauseRunnable
from org.allbinary.game.displayable.canvas.FormUtil import FormUtil
from org.allbinary.game.displayable.canvas.MyFormUtil import MyFormUtil
from org.allbinary.game.displayable.canvas.EndGameInfo import EndGameInfo
from org.allbinary.game.displayable.canvas.NoMenuInputProcessor import NoMenuInputProcessor
from org.allbinary.game.displayable.canvas.NullDemoPaintable import NullDemoPaintable
from org.allbinary.game.displayable.canvas.GameCanvasInputProcessor import GameCanvasInputProcessor
from org.allbinary.game.displayable.canvas.FormInputProcessor import FormInputProcessor


