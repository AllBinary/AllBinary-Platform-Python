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

import threading
from org.allbinary.canvas.RunnableCanvas import RunnableCanvas
from org.allbinary.graphics.displayable.event.DisplayChangeEventListener import DisplayChangeEventListener
from org.allbinary.game.displayable.canvas.GameCanvasRunnableInterface import GameCanvasRunnableInterface
from org.allbinary.game.displayable.canvas.MenuListener import MenuListener
from org.allbinary.game.displayable.canvas.DemoPaintableInterface import DemoPaintableInterface


class DemoCanvas(RunnableCanvas, GameCanvasRunnableInterface, MenuListener, DisplayChangeEventListener, DemoPaintableInterface):
    id: int = 0
    BOT_GAME_STATS: str = "Bot Game Statistics: "
    TYPE: int = 3
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.myCommandsFactory: MyCommandsFactory = MyCommandsFactory.getInstance()
        self.gameAdStateFactory: GameAdStateFactory = GameAdStateFactory.getInstance()
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        self.gameStateFactory: GameStateFactory = GameStateFactory.getInstance()
        self.threadFactoryUtil: ThreadFactoryUtil = ThreadFactoryUtil.getInstance()
        self.formUtil: FormUtil = FormUtil.getInstance()
        self.fullscreenPaintable: Paintable = FullScreenPaintableFactory.getInstance().paintable
        self.basicGameDemoPaintable: StatePaintable = StatePaintableFactory.getInstance()
        self.specialAnimationInterface: SpecialAnimation = SpecialAnimation.getInstance()
        self.paintedSpecialAnimationInterface: Animation = SpecialAnimation.getInstance()
        self.fullScreenUtil: FullScreenUtil = FullScreenUtil.getInstance()
        self.gameCanvas: AllBinaryGameCanvas = NullGameCanvas.getInstance()
        self.highScoresHelper: HighScoresHelperBase = HighScoresHelper()
        self.realHighScoresPaintable: HighScoresPaintable = HighScoresPaintable()
        self.highScoresPaintable: Paintable = NullPaintable.getInstance()
        self.state: int = 0
        self.canvasThread: threading.Thread = NullThread.NULL_THREAD
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(6000)
        self.basicColor: BasicColor = self.basicColorFactory.RED
        self.abeClientInformation: AbeClientInformationInterface = None
        self.highScoresFactoryInterface: HighScoresFactoryInterface = None
        self.menuInputProcessor: BasicMenuInputProcessor = NoMenuInputProcessor.getInstance()
        self.menuForm: ScrollSelectionForm = ScrollSelectionForm.getNullScrollSelectionForm()
        self.gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory = None
        self.initialized: bool = False
        self.demoGameRunnable: DemoGameStartupRunnable = None
        self.defaultPaintableInterface: Paintable = NullPaintable.getInstance()
        self.paintableInterface: PaintableInterface = NullPaintable.getInstance()
        self.overlayPaintable: InitUpdatePaintable = None
        self.progressPaintable: PaintableInterface = ProgressCanvasFactory.getLazyInstance()
        self.tempWait: int = NullWaitGameRunnable.getInstance().WAIT
        self.inputToGameKeyMapping: InputToGameKeyMapping = PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping()
        self.gameRunnable: GameRunnable = NullWaitGameRunnable.getInstance()
        self.isSingleKeyRepeatableProcessing: bool = Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_REPEAT_PRESS)
        self.NONE: GameKey = GameKeyFactory.getInstance().NONE
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.lastKeyNotMapped: int = -1
        self.SET_STATE: str = "setState"
        self.baseGameStatistics: BaseGameStatistics = GameStatisticsFactory.getInstance()
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, commandListener: CommandListener, highScoresFactoryInterface: HighScoresFactoryInterface, paintable: Paintable, overlayPaintable: InitUpdatePaintable, gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory, isContinue: bool) -> None:
        from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
        from org.allbinary.game.displayable.canvas.DemoGameStartupRunnable import DemoGameStartupRunnable
        super().__init__(commandListener, CurrentDisplayableFactory.getInstance().DEFAULT_CHILD_NAME_LIST, True)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.setWait(NullWaitGameRunnable.getInstance().WAIT)
        self.gameInitializationInterfaceFactoryInterface = gameInitializationInterfaceFactoryInterface
        GameInitializationUtil.getInstance().initDemo(abeClientInformation, self, gameInitializationInterfaceFactoryInterface)
        ResizableListenerHandler.getInstance().fireEvent(False)
        self.overlayPaintable = overlayPaintable
        self.highScoresFactoryInterface = highScoresFactoryInterface
        self.setDefaultPaintableInterface(paintable)
        self.setPaintableInterface(self.getDefaultPaintableInterface())
        if isContinue:
            self.addCommand(GameCommandsFactory.getInstance().CONTINUE_COMMAND)
        if ChangedGameFeatureListener.getInstance().isChangedFeature(GameFeatureFactory.getInstance().SOUND):
            self.mediaInit()
        self.demoGameRunnable = DemoGameStartupRunnable(self)
        DisplayChangeEventHandler.getInstance().addListenerInterface(self)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        try:
            self.logUtil.putF(str(StringMaker().append(self.commonLabels.START_LABEL).append(str(self.displayInfo))), self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT)
            scrollSelectionForm: ScrollSelectionForm = self.getMenuForm()
            if scrollSelectionForm is not None:
                formType: FormType = FormTypeFactory.getInstance().getFormType()
                rectangle: Rectangle = self.formUtil.createFormRectangle()
                scrollSelectionForm.init(rectangle, formType)
            self.overlayPaintable.init()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT, e)
    

    def getCustomCommands(self) -> list[object]:
        from org.allbinary.game.displayable.canvas.GameInputMappingCanvas import GameInputMappingCanvas
        from org.allbinary.game.displayable.canvas.GameInputMappingCanvas import GameInputMappingCanvas
        from org.allbinary.game.displayable.canvas.GameInputMappingCanvas import GameInputMappingCanvas
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        if J2MEUtil.isHTML():
            commandArray: list[object] = [gameCommandsFactory.START_COMMAND, HighScoreCommands.getInstance().DISPLAY, GameInputMappingCanvas.DISPLAY, gameCommandsFactory.DISPLAY_ABOUT]
            return commandArray
        else:
            commandList: BasicArrayList = BasicArrayListD()
            commandList.add(gameCommandsFactory.START_COMMAND)
            inApplicationPurchaseFactory: InApplicationPurchaseFactory = InApplicationPurchaseFactory.getInstance()
            if inApplicationPurchaseFactory.isEnabled():
                list_: BasicArrayList = LockableFeatureFactory.getInstance().getList()
                if list_.size() > 0 and not inApplicationPurchaseFactory.isPurchased(list_.get(0)):
                    commandList.add(gameCommandsFactory.BUY_COMMAND)
            commandList.add(HighScoreCommands.getInstance().DISPLAY)
            try:
                isOverScan: bool = OperatingSystemFactory.getInstance().getOperatingSystemInstance().isOverScan()
                if SWTUtil.isSWT:
                    commandList.add(GameInputMappingCanvas.DISPLAY)
                elif not isOverScan:
                    commandList.add(gameCommandsFactory.DISPLAY_OPTIONS)
                    commandList.add(gameCommandsFactory.DISPLAY_LOAD_FORM)
                    commandList.add(GameInputMappingCanvas.DISPLAY)
            except Exception as e:
                pass
            commandList.add(gameCommandsFactory.DISPLAY_ABOUT)
            commandArray: list[object] = commandList.toArray()
            return commandArray
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        commandArray: list[object] = self.getCustomCommands()
        size: int = len(commandArray)
        for index in range(0, size):
            self.addCommand(commandArray[index])
        CustomGameMenuUtil.add(self)
        self.setCommandListener(cmdListener)
    

    # throws Exception
    def initPostPaint(self) -> None:
        pass
    

    # throws Exception
    def mediaInit(self) -> None:
        AllBinaryMediaManager.init(EarlySoundsFactory.getInstance())
    

    def itemStateChanged(self, item: Item) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
    

    # throws Exception
    def initMenu(self) -> None:
        from org.allbinary.game.displayable.canvas.DemoLimitedCommandTextItemArrayFactory import DemoLimitedCommandTextItemArrayFactory
        from org.allbinary.game.displayable.canvas.CommandFormInputProcessor import CommandFormInputProcessor
        self.close()
        commandTextItemArrayFactory: CommandTextItemArrayFactory = DemoLimitedCommandTextItemArrayFactory.getInstance().getCommandTextItemArrayFactory()
        items: list[ABCustomItem] = commandTextItemArrayFactory.getInstance(self.getCommandStack(), self.basicColorFactory.BLACK, self.basicColorFactory.WHITE)
        formType: FormType = FormTypeFactory.getInstance().getFormType()
        rectangle: Rectangle = self.formUtil.createFormRectangle()
        PreLogUtil.put(str(StringMaker().append(self.commonLabels.START_LABEL).append(str(self.displayInfo))), self, "initMenu")
        scrollSelectionForm: ScrollSelectionForm = CommandCurrentSelectionFormFactory.getInstance(StringUtil.getInstance().EMPTY_STRING, items, rectangle, formType, 15, True, self.basicColorFactory.BLACK, self.basicColorFactory.WHITE)
        self.setMenuForm(scrollSelectionForm)
        formType2: FormType = FormTypeFactory.getInstance().getFormType()
        rectangle2: Rectangle = self.formUtil.createFormRectangle()
        scrollSelectionForm.init(rectangle2, formType2)
        if self.getMenuForm() != ScrollSelectionFormNoneFactory.getInstance():
            self.setMenuInputProcessor(CommandFormInputProcessor(BasicArrayListD(), -1, self, self.getMenuForm()))
        self.open()
    

    def open(self) -> None:
        BasicMotionGesturesHandler.getInstance().addListenerInterface(self.getMenuInputProcessor())
        GameKeyEventHandler.getInstance().addListener(self.getMenuInputProcessor())
    

    def close(self) -> None:
        BasicMotionGesturesHandler.getInstance().removeListener(self.getMenuInputProcessor())
        GameKeyEventHandler.getInstance().removeListener(self.getMenuInputProcessor())
    

    def getSourceId(self) -> int:
        return DemoCanvas.id
    

    def keyPressed(self, keyCode: int) -> None:
        self.keyPressedByDevice(keyCode, 0)
    

    def keyReleased(self, keyCode: int) -> None:
        self.keyReleasedByDevice(keyCode, 0)
    

    def keyRepeated(self, keyCode: int) -> None:
        self.keyRepeatedByDevice(keyCode, 0)
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.addGameKeyEvent(keyCode, False)
    

    def keyReleasedByDevice(self, keyCode: int, deviceId: int) -> None:
        self.removeGameKeyEvent(keyCode, False)
    

    def keyRepeatedByDevice(self, keyCode: int, deviceId: int) -> None:
        if self.isSingleKeyRepeatableProcessing:
            self.addGameKeyEvent(keyCode, True)
    

    def addGameKeyEvent(self, keyCode: int, repeated: bool) -> None:
        try:
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(self, keyCode)
            if gameKey != self.NONE:
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self, gameKey)
                DownGameKeyEventHandler.getInstance().fireEvent(gameKeyEvent)
            else:
                if self.lastKeyNotMapped != keyCode:
                    self.lastKeyNotMapped = keyCode
                    self.logUtil.putF(str(StringMaker().append(self.gameInputStrings.NO_KEY).appendint(keyCode)), self, self.gameInputStrings.ADD_KEY_EVENT)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.ADD_KEY_EVENT, e)
    

    def removeGameKeyEvent(self, keyCode: int, repeated: bool) -> None:
        try:
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(self, keyCode)
            if gameKey != self.NONE:
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self, gameKey)
                UpGameKeyEventHandler.getInstance().fireEvent(gameKeyEvent)
            else:
                self.logUtil.putF(str(StringMaker().append(self.gameInputStrings.NO_KEY).appendint(keyCode)), self, self.gameInputStrings.REMOVE_KEY_EVENT)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.REMOVE_KEY_EVENT, e)
    

    def pause(self) -> None:
        with self._lock:
            return self._pause_unlocked()

    def _pause_unlocked(self) -> None:
        from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
        self.close()
        self.setPaused(True)
        self.gameRunnable = NullWaitGameRunnable.getInstance()
        self.gameCanvas.pause()
    

    def unPause(self) -> None:
        with self._lock:
            return self._unPause_unlocked()

    def _unPause_unlocked(self) -> None:
        self.open()
        self.gameCanvas.unPause()
        self.gameRunnable = self.gameCanvas.gameRunnable
        self.setPaused(False)
    

    def isPausable(self) -> bool:
        from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
        if CurrentDisplayableFactory.getInstance().getUsedRunnable() == NullWaitGameRunnable.getInstance():
            return True
        else:
            return False
    

    def isGameOver(self) -> bool:
        self.logUtil.putF(str(StringMaker().append(self.commonStrings.NOT_IMPLEMENTED).append(" since not a game")), self, "isGameOver")
        return False
    

    # throws Exception
    def setLoadStateHashtable(self, hashtable: ABHashtable[object, object]) -> None:
        self.logUtil.putF("Trying to continue a demo lol - only continue a game canvas not the demo", self, "setLoadStateHashtable")
    

    # throws Exception
    def getLoadStateHashtable(self) -> ABHashtable[object, object]:
        self.logUtil.putF("Trying to continue a demo lol - only continue a game canvas not the demo", self, "getLoadStateHashtable")
        return self.stdUtil.NULL_TABLE
    

    # throws Exception
    def getCurrentStateHashtable(self) -> ABHashtable[object, object]:
        self.logUtil.putF("Trying to save the AI lol", self, "getCurrentStateHashtable")
        return self.stdUtil.NULL_TABLE
    

    def setHighScoreSubmitted(self, isNotUsed: bool) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        self.paintableInterface.paint(graphics)
        self.paintedSpecialAnimationInterface.paintXY(graphics, 0, 0)
        self.highScoresPaintable.paint(graphics)
        self.getBasicGameDemoPaintable().paint(graphics)
        self.overlayPaintable.paint(graphics)
        self.fullscreenPaintable.paint(graphics)
        self.progressPaintable.paint(graphics)
    

    def paintThreed(self, graphics: Graphics) -> None:
        self.paintableInterface.paintThreed(graphics)
        self.paintedSpecialAnimationInterface.paintThreedXYZ(graphics, 0, 0, 0)
    

    def processGameOver(self) -> None:
        with self._lock:
            return self._processGameOver_unlocked()

    def _processGameOver_unlocked(self) -> None:
        self.logUtil.putF("Not Implemented since not a game", self, "setGameOver")
    

    def demoStateChange(self) -> None:
        newState: int = self.state + 1
        if newState > 2:
            newState = 0
        elif newState == 2:
            if not self.highScoresHelper.isAnyHighScores():
                newState = 0
            else:
                highScores: HighScores = self.highScoresHelper.getNextHighScores()
                if highScores == NullHighScoresSingletonFactory.getInstance():
                    newState = 0
                else:
                    self.getRealHighScoresPaintable().setHighScores(highScores)
        self.setState(newState)
        self.updateDemoState()
    

    def updateDemoState(self) -> None:
        PreLogUtil.put(str(SmallIntegerSingletonFactory.getInstance().createInstance(self.state)), self, self.SET_STATE)
        self.getBasicGameDemoPaintable().setState(self.state)
        if self.state == 0:
            self.highScoresPaintable = NullPaintable.getInstance()
            self.paintedSpecialAnimationInterface = self.getSpecialAnimationInterface()
            if not self.demoGameRunnable.isRunning() and self.gameCanvas.isInitialized():
                self.getSpecialAnimationInterface().reset()
        elif self.state == 1:
            self.paintedSpecialAnimationInterface = SpecialAnimation.getInstance()
        elif self.state == 2:
            self.highScoresPaintable = self.getRealHighScoresPaintable()
        gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
        gameAdState.processPageAdState()
    

    # throws Exception
    def getNextRandom(self) -> int:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def createGameLayerManager(self, randomValue: int) -> AllBinaryGameLayerManager:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def createRunnable(self, randomLevel: int) -> GameCanvasRunnableInterface:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def create(self) -> None:
        PreLogUtil.put(self.commonStrings.START, self, "create")
        self.highScoresPaintable = NullPaintable.getInstance()
        randomLevel: int = self.getNextRandom()
        self.gameCanvas = self.createRunnable(randomLevel)
        self.basicColor = self.gameCanvas.getLayerManager().getForegroundBasicColor()
        self.getRealHighScoresPaintable().setBasicColorP(self.basicColor)
        self.gameCanvas.setGameCanvasStartListener(self)
        gameInfo: GameInfo = self.gameCanvas.getLayerManager().getGameInfo()
        self.getHighScoresFactoryInterface().fetchHighScores(gameInfo, self.highScoresHelper)
    

    # throws Exception
    def start(self) -> None:
        from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
        gameCanvas: AllBinaryGameCanvas = self.gameCanvas
        PreLogUtil.put(str(StringMaker().append("Game Thread in DemoCanvas: ").append(self.stringUtil.toString(gameCanvas))), self, self.commonStrings.START)
        self.canvasThread = self.threadFactoryUtil.getInstanceGameCanvasRunnable(gameCanvas)
        self.gameCanvas.setThread(self.canvasThread)
        self.threadFactoryUtil.start(self.canvasThread)
        if self.getWait() == NullWaitGameRunnable.getInstance().WAIT:
            self.setWait(self.getTempWait())
    

    def preDemoProcess(self) -> None:
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        if not self.gameCanvas.isInitialized() or self.gameCanvas.getTitle() == NullGameCanvas.NO_GAME:
            if AllBinaryMediaManager.update():
                if not PrimaryPlayerQueueFactory.getInstance().process():
                    SecondaryPlayerQueueFactory.getInstance().process()
        self.overlayPaintable.update()
    

    # throws Exception
    def process(self) -> None:
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        super().process()
        self.getMenuInputProcessor().processInputList()
        self.preDemoProcess()
        if self.state == 0:
            indexedAnimationBehavior: IndexedAnimationBehavior = (self.getSpecialAnimationInterface().getAnimationBehavior())
            if indexedAnimationBehavior.loopIndex < 1:
                self.timeDelayHelper.setStartTimeTNT()
            demoGameMidlet: DemoGameMidlet = self.getCustomCommandListener()
            if self.gameCanvas != NullGameCanvas.getInstance() and self.gameCanvas.isGameOver():
                self.stopGameDemo()
                randomLevel: int = self.getNextRandom()
                gameInfo: GameInfo = self.gameCanvas.getLayerManager().getGameInfo()
                gameInfo.setCurrentLevel(randomLevel)
                self.gameCanvas.setGameOver(False)
                self.start()
            elif self.gameCanvas == NullGameCanvas.getInstance() and demoGameMidlet.isReady():
                if not self.demoGameRunnable.isRunning():
                    self.startDemoGame()
                    self.demoGameRunnable.setRunning(True)
                    thread: threading.Thread = self.threadFactoryUtil.getInstanceForRunnable(self.demoGameRunnable)
                    self.demoGameRunnable.setThread(thread)
                    self.threadFactoryUtil.start(thread)
    

    # throws Exception
    def startDemoGame(self) -> None:
        from org.allbinary.game.displayable.canvas.DemoCanvasProgressUtil import DemoCanvasProgressUtil
        DemoCanvasProgressUtil.showProgress(self)
    

    # throws Exception
    def stopGameDemo(self) -> None:
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        if self.gameCanvas != NullGameCanvas.getInstance():
            self.logUtil.putF("Set Running False", self, "stopGameDemo")
            self.gameCanvas.setRunning(False)
        ThreadUtil.getInstance().join(self.canvasThread)
    

    def showGamePaintable(self) -> None:
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
        METHOD_NAME: str = "showGamePaintable"
        PreLogUtil.put(self.commonStrings.START, self, METHOD_NAME)
        isDefault: bool = J2MEUtil.isHTML()
        if self.gameCanvas != NullGameCanvas.getInstance() and (self.gameCanvas.isRunning() or isDefault or SWTUtil.isSWT) and not (self.gameCanvas.getType() == NullGameCanvas.TYPE):
            self.gameRunnable = self.gameCanvas.gameRunnable
            PreLogUtil.put("Showing Game", self, METHOD_NAME)
            self.setPaintableInterface(self.gameCanvas)
        else:
            self.gameRunnable = NullWaitGameRunnable.getInstance()
            PreLogUtil.put("Not Showing Game", self, METHOD_NAME)
            self.setPaintableInterface(self.getDefaultPaintableInterface())
    

    def isReadyForStateChange(self) -> bool:
        return not self.demoGameRunnable.isRunning() and self.gameCanvas.isInitialized()
    

    # throws Exception
    def processGame(self) -> None:
        self.gameRunnable.run()
        if not self.specialAnimationInterface.isComplete() and self.isReadyForStateChange():
            self.specialAnimationInterface.nextFrame()
        if self.timeDelayHelper.isTimeTNT() and self.isReadyForStateChange():
            self.demoStateChange()
        else:
            self.process()
    

    def run(self) -> None:
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        from org.allbinary.game.displayable.canvas.DemoGameRunnable import DemoGameRunnable
        from org.allbinary.game.displayable.canvas.DemoGameRunnable import DemoGameRunnable
        self.logUtil.putF(self.commonStrings.START_RUNNABLE, self, self.commonStrings.RUN)
        try:
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            features: Features = Features.getInstance()
            openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
            progressCanvas.addNormalPortion(50, "Demo Thread")
            self.setCurrentThread()
            self.setRunning(True)
            if features.isFeature(MainFeatureFactory.getInstance().LOAD_ONDEMAND):
                progressCanvas.end()
            else:
                progressCanvas.addNormalPortion(50, "Demo Thread Running")
            self.fullScreenUtil.initOnRun(self, self.getCustomCommandListener())
            self.initMenu()
            self.initPostPaint()
            self.updateDemoState()
            if features.isDefault(openGLFeatureFactory.OPENGL_AS_GAME_THREAD):
                while self.gameCanvas == NullGameCanvas.getInstance() or not self.gameCanvas.isInitialized():
                    self.loopTimeHelper.setStartTimeTNT()
                    self.processGame()
                    self.processLoopSleep()
                demoGameRunnable: DemoGameRunnable = DemoGameRunnable(self)
                currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
                currentDisplayableFactory.setRunnable(demoGameRunnable)
                currentDisplayableFactory.setMyCanvas(self)
                OpenGLThreadUtil.getInstance().onResume()
            if features.isDefault(openGLFeatureFactory.OPENGL_AS_GAME_THREAD) or J2MEUtil.isHTML():
                demoGameRunnable: DemoGameRunnable = DemoGameRunnable(self)
                currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
                currentDisplayableFactory.setRunnable(demoGameRunnable)
                currentDisplayableFactory.setMyCanvas(self)
            else:
                while self.isRunning():
                    self.run3()
                self.end()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
        self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
    

    # throws Exception
    def run3(self) -> None:
        self.loopTimeHelper.setStartTimeTNT()
        self.processGame()
        self.processLoopSleep()
    

    def setRunning(self, running: bool) -> None:
        super().setRunning(running)
        try:
            features: Features = Features.getInstance()
            openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
            if running:
                pass
            else:
                if (features.isDefault(openGLFeatureFactory.OPENGL) or J2MEUtil.isHTML()) or SWTUtil.isSWT:
                    currentDisplayableFactory: CurrentDisplayableFactory = CurrentDisplayableFactory.getInstance()
                    currentDisplayableFactory.clearRunnable()
                    self.end()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.SET_RUNNING, e)
    

    # throws Exception
    def end(self) -> None:
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        features: Features = Features.getInstance()
        self.baseGameStatistics.add(str(StringMaker().append(DemoCanvas.BOT_GAME_STATS).append(str(self.baseGameStatistics)).append(CommonSeps.getInstance().NEW_LINE)))
        self.baseGameStatistics.init()
        if features.isFeature(MainFeatureFactory.getInstance().LOAD_ONDEMAND):
            progressCanvas.start()
        self.logUtil.putF("Demo End", self, self.commonStrings.RUN)
        self.close()
        DisplayChangeEventHandler.getInstance().removeListener(self)
        self.stopGameDemo()
    

    def setGameState(self, gameState: GameState) -> None:
        pass
    

    def getGameState(self) -> GameState:
        return self.gameStateFactory.PLAYING_GAME_STATE
    

    def getGameCanvasRunnableInterface(self) -> AllBinaryGameCanvas:
        return self.gameCanvas
    

    def isDemoLoading(self) -> bool:
        from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
        gameCanvas: AllBinaryGameCanvas = self.gameCanvas
        if gameCanvas == NullGameCanvas.getInstance():
            return True
        elif gameCanvas.isInitialized():
            return False
        return True
    

    def getState(self) -> int:
        return self.state
    

    def setState(self, state: int) -> None:
        self.state = state
    

    def isHighScoreSubmitted(self) -> bool:
        self.logUtil.putF("Wow the AI got a high score!", self, "isHighScoreSubmitted")
        return False
    

    def getRealHighScoresPaintable(self) -> HighScoresPaintable:
        return self.realHighScoresPaintable
    

    def setSpecialAnimationInterface(self, specialAnimationInterface: SpecialAnimation) -> None:
        specialAnimationInterface.setFrame(0)
        self.specialAnimationInterface = specialAnimationInterface
    

    def getSpecialAnimationInterface(self) -> SpecialAnimation:
        return self.specialAnimationInterface
    

    def setPaintableInterface(self, paintableInterface: PaintableInterface) -> None:
        self.paintableInterface = paintableInterface
    

    def getPaintableInterface(self) -> PaintableInterface:
        return self.paintableInterface
    

    def setDefaultPaintableInterface(self, defaultPaintableInterface: Paintable) -> None:
        self.defaultPaintableInterface = defaultPaintableInterface
    

    def getDefaultPaintableInterface(self) -> Paintable:
        return self.defaultPaintableInterface
    

    def getHighScoresFactoryInterface(self) -> HighScoresFactoryInterface:
        return self.highScoresFactoryInterface
    

    def setMenuInputProcessor(self, menuInputProcessor: BasicMenuInputProcessor) -> None:
        self.menuInputProcessor = menuInputProcessor
    

    def getMenuInputProcessor(self) -> BasicMenuInputProcessor:
        return self.menuInputProcessor
    

    def getMenuForm(self) -> ScrollSelectionForm:
        return self.menuForm
    

    def setMenuForm(self, menuForm: ScrollSelectionForm) -> None:
        self.menuForm = menuForm
    

    def isInitialized(self) -> bool:
        return self.initialized
    

    def getOverlayPaintable(self) -> Paintable:
        return self.overlayPaintable
    

    def setBasicGameDemoPaintable(self, basicGameDemoPaintable: StatePaintable) -> None:
        self.basicGameDemoPaintable = basicGameDemoPaintable
    

    def getBasicGameDemoPaintable(self) -> StatePaintable:
        return self.basicGameDemoPaintable
    

    def setTempWait(self, tempWait: int) -> None:
        self.tempWait = tempWait
    

    def getTempWait(self) -> int:
        return self.tempWait
    

    def isSingleThread(self) -> bool:
        return OpenGLFeatureUtil.getInstance().isAnyThreed() or SWTUtil.isSWT
    

    def isRunningInAnotherThread(self) -> bool:
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        if features.isDefault(openGLFeatureFactory.OPENGL_AS_GAME_THREAD):
            return True
        else:
            return self.isRunning()
    

    def getGameInitializationInterfaceFactoryInterface(self) -> BasicBuildGameInitializerFactory:
        return self.gameInitializationInterfaceFactoryInterface
    

    def getType(self) -> int:
        return DemoCanvas.TYPE
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Item import Item
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
from org.allbinary.animation.special.SpecialAnimation import SpecialAnimation
from org.allbinary.business.advertisement.GameAdStateFactory import GameAdStateFactory
from org.allbinary.canvas.BaseGameStatistics import BaseGameStatistics
from org.allbinary.canvas.CustomGameMenuUtil import CustomGameMenuUtil
from org.allbinary.canvas.FullScreenUtil import FullScreenUtil
from org.allbinary.canvas.GameStatisticsFactory import GameStatisticsFactory
from org.allbinary.game.GameAdState import GameAdState
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.game.init.BasicBuildGameInitializerFactory import BasicBuildGameInitializerFactory
from org.allbinary.game.init.GameInitializationUtil import GameInitializationUtil
from org.allbinary.game.input.GameInputStrings import GameInputStrings
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.SWTUtil import SWTUtil
from org.allbinary.game.midlet.DemoGameMidlet import DemoGameMidlet
from org.allbinary.game.score.HighScoreCommands import HighScoreCommands
from org.allbinary.game.score.HighScores import HighScores
from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
from org.allbinary.game.score.HighScoresHelper import HighScoresHelper
from org.allbinary.game.score.HighScoresHelperBase import HighScoresHelperBase
from org.allbinary.game.score.HighScoresPaintable import HighScoresPaintable
from org.allbinary.game.score.NullHighScoresSingletonFactory import NullHighScoresSingletonFactory
from org.allbinary.game.state.GameState import GameState
from org.allbinary.game.state.GameStateFactory import GameStateFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.ResizableListenerHandler import ResizableListenerHandler
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.displayable.event.DisplayChangeEventHandler import DisplayChangeEventHandler
from org.allbinary.graphics.displayable.screen.FullScreenPaintableFactory import FullScreenPaintableFactory
from org.allbinary.graphics.form.CommandCurrentSelectionFormFactory import CommandCurrentSelectionFormFactory
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
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.graphics.paint.StatePaintable import StatePaintable
from org.allbinary.graphics.paint.StatePaintableFactory import StatePaintableFactory
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.InApplicationPurchaseFactory import InApplicationPurchaseFactory
from org.allbinary.logic.system.security.licensing.LockableFeature import LockableFeature
from org.allbinary.logic.system.security.licensing.LockableFeatureFactory import LockableFeatureFactory
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.audio.AllBinaryMediaManager import AllBinaryMediaManager
from org.allbinary.media.audio.EarlySoundsFactory import EarlySoundsFactory
from org.allbinary.media.audio.PrimaryPlayerQueueFactory import PrimaryPlayerQueueFactory
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.thread.NullThread import NullThread
from org.allbinary.thread.ThreadFactoryUtil import ThreadFactoryUtil
from org.allbinary.thread.ThreadUtil import ThreadUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.displayable.canvas.FormUtil import FormUtil
from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
from org.allbinary.game.displayable.canvas.NoMenuInputProcessor import NoMenuInputProcessor
from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable


