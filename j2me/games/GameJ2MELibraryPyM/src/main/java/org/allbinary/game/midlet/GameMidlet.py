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
# package org.allbinary.game.midlet

from __future__ import annotations

import threading
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.midlet.ProgressMidlet import ProgressMidlet


class GameMidlet(ProgressMidlet, CommandListener):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.features: Features = Features.getInstance()
        self.midletStrings: MidletStrings = MidletStrings.getInstance()
        self.myCommandsFactory: MyCommandsFactory = MyCommandsFactory.getInstance()
        self.gameStrings: GameStrings = GameStrings.getInstance()
        self.gameAdStateFactory: GameAdStateFactory = GameAdStateFactory.getInstance()
        self.gameStateFactory: GameStateFactory = GameStateFactory.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.DISPLAYABLE: str = " Displayable: "
        self.COMMAND_NAME: str = "command Name/Label: "
        self.NO_COMMAND: str = "No Command"
        self.NO_DISPLAYABLE: str = "No Displayable"
        self.COMMAND_ACTION: str = str(StringMaker().append("GameMidlet::").append(self.midletStrings.COMMAND_ACTION))
        self.PAUSE_APP_BACKGROUND: str = "pauseAppBackground"
        self.UN_PAUSE_APP_BACKGROUND: str = "unPauseAppBackground"
        self.aboutCommandProcessor: AboutCommandProcessor = AboutCommandProcessor.getInstance()
        self.webCommandProcessor: WebCommandProcessor = WebCommandProcessor.getInstance()
        self.gameMidletStateFactory: GameMidletStateFactory = GameMidletStateFactory.getInstance()
        self.gameStartTimeHelper: TimeDelayHelper = TimeDelayHelper(240)
        self.fullScreenUtil: FullScreenUtil = FullScreenUtil.getInstance()
        self.debugInterface: DebugInterface = None
        self.allbinaryGameCanvasRunnableInterface: GameCanvasRunnableInterface = NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE
        self.thread: threading.Thread = NullThread.NULL_THREAD
        self.loadGameForm: CommandForm = None
        self.isFullScreen: bool = False
        self.resized: bool = False
        self.startedBefore: bool = False
    

    def __init__(self, clientInformationFactory: ClientInformationFactory) -> None:
        super().__init__(clientInformationFactory)
        self._init_fields()
        SmallIntegerSingletonFactory.getInstance().initWithRange(0x291, 6)
        self.loadGameForm = CommandForm.getNullCommandForm()
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.init(self)
        GameFeatureEventHandler.getInstance().addListenerInterface(ChangedGameFeatureListener.getInstance())
        GamePersistanceSingleton.getInstance().clear()
        self.debugInterface = DebugFactory.getInstance()
        self.init()
    

    def init(self) -> None:
        pass
    

    # throws Exception
    def setDemo(self) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def createGame(self) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def mediaShutdown(self) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def stopAll(self) -> None:
        pass
    

    def pauseApp(self) -> None:
        self.pauseAppBackground(True)
        gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
        gameAdState.getAdvertisements().stopAll()
    

    def pauseAppBackground(self, background: bool) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.PAUSE_APP_BACKGROUND)
        if self.allbinaryGameCanvasRunnableInterface != NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE:
            self.allbinaryGameCanvasRunnableInterface.pause()
        else:
            self.logUtil.putF("<<<<<< Null", self, self.PAUSE_APP_BACKGROUND)
        AllBinarySensorManager.getInstance().shutdown()
    

    def unPauseApp(self) -> None:
        self.unPauseAppBackground(True)
        gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
        gameAdState.getAdvertisements().startAll()
    

    def unPauseAppBackground(self, background: bool) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.UN_PAUSE_APP_BACKGROUND)
        AllBinarySensorManager.getInstance().init()
        gameCanvasRunnableInterface: GameCanvasRunnableInterface = self.allbinaryGameCanvasRunnableInterface
        if gameCanvasRunnableInterface != NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE:
            gameCanvasRunnableInterface.unPause()
        else:
            self.logUtil.putF("<<<<<< Null", self, self.UN_PAUSE_APP_BACKGROUND)
    

    def destroyAppInRunnable(self, unconditional: bool, isProgress: bool) -> None:
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        if isProgress:
            progressCanvas.start()
            self.commandAction(self.myCommandsFactory.SET_DISPLAYABLE, progressCanvas)
        self.destroyApp(unconditional)
        if isProgress:
            progressCanvas.end()
    

    def destroyApp(self, unconditional: bool) -> None:
        METHOD_NAME: str = "GameMidlet::destroyApp"
        try:
            PreLogUtil.put(str(GameStatisticsFactory.getInstance()), self, METHOD_NAME)
            gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
            gameAdState.getAdvertisements().stopAll()
            if not self.isDestroyed():
                self.stopGameCanvasRunnableInterface()
                self.setGameCanvasRunnableInterface(NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE)
                self.mediaShutdown()
            else:
                self.logUtil.putF("Midlet Managment Error: Midlet Should Only Be Destroyed Once", self, METHOD_NAME)
            super().destroyApp(True)
            PreLogUtil.put(self.commonStrings.END, self, METHOD_NAME)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, METHOD_NAME, e)
        self.logUtil.putF(self.commonStrings.END, self, METHOD_NAME)
    

    # throws MIDletStateChangeException
    def startApp(self) -> None:
        try:
            gameAdState: GameAdState = self.gameAdStateFactory.getCurrentInstance()
            gameAdState.getAdvertisements().startAll()
            START_APP: str = "startApp"
            self.logUtil.putF(self.commonStrings.START, self, START_APP)
            gameCanvasRunnableInterface: object = self.allbinaryGameCanvasRunnableInterface
            if gameCanvasRunnableInterface == NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE:
                self.gameMidletStateFactory.setCurrentGameState(self.gameStateFactory.NO_GAME_STATE)
                self.setDemo()
            else:
                self.logUtil.putF("GameCanvasRunnableInterface is available", self, START_APP)
                if gameCanvasRunnableInterface == self.getCurrentDisplayable():
                    self.unPauseAppBackground(False)
                else:
                    self.logUtil.putF("GameCanvasRunnableInterface is not current displayable", self, START_APP)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "startApp", e)
            self.destroyApp(False)
            self.notifyDestroyed()
    

    def commandAction(self, command: Command, displayable: Displayable) -> None:
        with self._lock:
            return self._commandAction_unlocked(command, displayable)

    def _commandAction_unlocked(self, command: Command, displayable: Displayable) -> None:
        from org.allbinary.game.midlet.GameMidletEventHandler import GameMidletEventHandler
        from org.allbinary.game.midlet.GameMidletEventHandler import GameMidletEventHandler
        from org.allbinary.game.midlet.DemoGameMidletEvent import DemoGameMidletEvent
        from org.allbinary.game.midlet.DemoGameMidletStateFactory import DemoGameMidletStateFactory
        try:
            displayableAsString: str = self.NO_DISPLAYABLE
            if displayable is not None:
                displayableAsString = str(displayable)
            label: str = self.NO_COMMAND
            if command is not None:
                label = command.getLabel()
            PreLogUtil.put(str(StringMaker().append(self.COMMAND_NAME).append(label).append(self.DISPLAYABLE).append(displayableAsString)), self, self.COMMAND_ACTION)
            gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
            allbinaryGameCanvasRunnableInterface: GameCanvasRunnableInterface = self.allbinaryGameCanvasRunnableInterface
            gameCanvasRunnableInterface: object = allbinaryGameCanvasRunnableInterface
            if command == gameCommandsFactory.SHOW_GAME_CANVAS:
                if self.getDisplay().getCurrent() != gameCanvasRunnableInterface and allbinaryGameCanvasRunnableInterface.getType() != NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE.getType():
                    self.setDisplay(gameCanvasRunnableInterface)
                self.unPauseAppBackground(False)
            elif command == gameCommandsFactory.CLOSE_AND_SHOW_GAME_CANVAS:
                menuListener: MenuListener = displayable
                menuListener.close()
                self.setDisplay(gameCanvasRunnableInterface)
                self.unPauseAppBackground(False)
            elif command == gameCommandsFactory.EXIT_COMMAND:
                if GameMidletEventHandler.getInstance().getEventListenerInterfaceListP().size() == 0:
                    self.exitProgress(True)
                GameMidletEventHandler.getInstance().fireEvent(DemoGameMidletEvent(self, DemoGameMidletStateFactory.getInstance().NONE))
            elif command == gameCommandsFactory.EXIT_WITHOUT_PROGRESS_COMMAND:
                self.exitProgress(False)
            elif command == gameCommandsFactory.START_COMMAND or command == gameCommandsFactory.RESTART_COMMAND or command == gameCommandsFactory.CONTINUE_COMMAND:
                if self.gameMidletStateFactory.getCurrentGameState() != self.gameStateFactory.PLAYING_GAME_STATE or command == gameCommandsFactory.RESTART_COMMAND:
                    if self.gameStartTimeHelper.isTimeTNT():
                        if command == gameCommandsFactory.START_COMMAND and self.isDemoLoading():
                            self.logUtil.putF("Trying to Start Game Before Loading Complete", self, self.midletStrings.COMMAND_ACTION)
                        else:
                            self.startedBefore = True
                            self.createGame()
                            self.gameMidletStateFactory.setCurrentGameState(self.gameStateFactory.PLAYING_GAME_STATE)
                    else:
                        self.logUtil.putF("Starting Game Too Often", self, self.midletStrings.COMMAND_ACTION)
                else:
                    self.logUtil.putF("Already in playing state", self, self.COMMAND_ACTION)
            elif command == gameCommandsFactory.BUY_COMMAND:
                inApplicationPurchaseFactory: InApplicationPurchaseFactory = InApplicationPurchaseFactory.getInstance()
                list_: BasicArrayList = LockableFeatureFactory.getInstance().getList()
                lockableFeature: LockableFeature = list_.get(0)
                if list_.size() > 0 and not inApplicationPurchaseFactory.isPurchased(lockableFeature):
                    inApplicationPurchaseFactory.purchase(lockableFeature)
                else:
                    TextNotificationUtil.getInstance().fireSuccess("Already Purchased")
            elif command == gameCommandsFactory.QUIT_COMMAND:
                if self.gameStartTimeHelper.isTimeTNT():
                    if isinstance(displayable, HighScoreTextBox):
                        menuListener: MenuListener = displayable
                        menuListener.close()
                    self.stopGameCanvasRunnableInterface()
                    self.gameMidletStateFactory.setCurrentGameState(self.gameStateFactory.NO_GAME_STATE)
                    self.setDemo()
            elif command == self.myCommandsFactory.RESUME_COMMAND:
                self.unPauseAppBackground(False)
            elif command == self.myCommandsFactory.PAUSE_COMMAND:
                self.pauseAppBackground(False)
            elif command == self.myCommandsFactory.SET_DISPLAYABLE:
                self.pauseAppBackground(False)
                self.setDisplay(displayable)
            elif command == gameCommandsFactory.SET_MENU_DISPLAYABLE:
                self.pauseAppBackground(False)
                menuListener: MenuListener = displayable
                menuListener.open()
                self.setDisplay(displayable)
            elif command == gameCommandsFactory.START_TRACE:
                self.debugInterface.start()
                gameCanvas: AllBinaryGameCanvas = allbinaryGameCanvasRunnableInterface
                gameCanvas.addCommand(gameCommandsFactory.STOP_TRACE)
                gameCanvas.removeCommand(gameCommandsFactory.START_TRACE)
            elif command == gameCommandsFactory.STOP_TRACE:
                self.pauseAppBackground(False)
                self.debugInterface.stop()
                self.unPauseAppBackground(False)
                gameCanvas: AllBinaryGameCanvas = allbinaryGameCanvasRunnableInterface
                gameCanvas.addCommand(gameCommandsFactory.START_TRACE)
                gameCanvas.removeCommand(gameCommandsFactory.STOP_TRACE)
            elif command == gameCommandsFactory.DEFAULT_OPTIONS:
                tempDisplayable: Displayable = displayable
                if isinstance(tempDisplayable, GameOptionsForm):
                    GameFeatureFormUtil.getInstance().setDefault(tempDisplayable)
            elif command == GameInputMappingInstructionsCanvas.DISPLAY:
                tempDisplayable: Displayable = displayable
                if isinstance(tempDisplayable, GameInputMappingCanvas):
                    gameInputMappingCanvas: GameInputMappingCanvas = tempDisplayable
                    gameInputMappingCanvas.update()
                self.commandAction(gameCommandsFactory.SET_MENU_DISPLAYABLE, self.getInputMappingInstructionsCanvas())
            elif HighScoreCommandsFactory.getInstance().isHighScoreCommand(command):
                tempDisplayable: Displayable = displayable
                if isinstance(tempDisplayable, HighScoresCanvas):
                    highScoresCanvas: HighScoresCanvas = tempDisplayable
                    highScoresCanvas.updateCommand(command)
            elif command == HighScoreCommands.getInstance().DISPLAY:
                self.commandAction(gameCommandsFactory.SET_MENU_DISPLAYABLE, self.createHighScoresCanvas())
            elif command == GameInputMappingInstructionsCanvas.CLOSE:
                menuListener: MenuListener = displayable
                menuListener.close()
                self.commandAction(GameInputMappingCanvas.DISPLAY, NullCanvas.NULL_CANVAS)
            elif command == GameInputMappingCanvas.DISPLAY:
                if J2MEUtil.isHTML():
                    self.pauseAppBackground(False)
                self.commandAction(gameCommandsFactory.SET_MENU_DISPLAYABLE, self.getInputMappingCanvas())
            elif command == GameInputMappingCanvas.DEFAULT:
                tempDisplayable: Displayable = displayable
                if isinstance(tempDisplayable, GameInputMappingCanvas):
                    gameInputMappingCanvas: GameInputMappingCanvas = tempDisplayable
                    gameInputMappingCanvas.setDefault()
            elif command == InGameOptionsForm.DISPLAY:
                self.pauseAppBackground(False)
                progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
                progressCanvas.addNormalPortion(50, "In Game Options")
                layerManager: AllBinaryGameLayerManager = self.createGameLayerManager()
                inGameOptionsFormFactory: InGameOptionsFormFactory = InGameOptionsFormFactory.getInstance()
                inGameOptionsFormFactory.init(self, InGameFeatures(), "Options In Game", layerManager.getBackgroundBasicColor(), layerManager.getForegroundBasicColor())
                inGameOptionsForm: CommandForm = inGameOptionsFormFactory.get()
                inGameOptionsForm.setItemStateListener(allbinaryGameCanvasRunnableInterface)
                self.commandAction(gameCommandsFactory.SET_MENU_DISPLAYABLE, inGameOptionsForm)
            elif command == InGameOptionsForm.DEFAULT:
                inGameOptionsForm: InGameOptionsForm = InGameOptionsFormFactory.getInstance().get()
                GameFeatureFormUtil.getInstance().setDefault(inGameOptionsForm)
            elif command == gameCommandsFactory.DISPLAY_OPTIONS:
                AllBinaryMediaManager.setMuted(True)
                self.stopAll()
                mainFeatureFactory: MainFeatureFactory = MainFeatureFactory.getInstance()
                self.isFullScreen = self.features.isFeature(mainFeatureFactory.FULL_SCREEN)
                ResizableListenerHandler.getInstance().fireEvent(True)
                self.setResized(False)
                self.commandAction(gameCommandsFactory.SET_MENU_DISPLAYABLE, self.getGameOptionsForm())
            elif command == gameCommandsFactory.CLOSE_OPTIONS:
                ResizableListenerHandler.getInstance().fireEvent(False)
                self.commandAction(gameCommandsFactory.CLOSE_AND_SHOW_GAME_CANVAS, displayable)
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Close isFullScreen/change: ")
                stringBuffer.appendboolean(self.isFullScreen)
                stringBuffer.appendboolean(self.fullScreenUtil.isScreenChange(self.isFullScreen))
                stringBuffer.append(" isResized: ")
                stringBuffer.appendboolean(self.isResized())
                PreLogUtil.put(str(stringBuffer), self, self.COMMAND_ACTION)
                if self.isResized() or self.fullScreenUtil.isScreenChange(self.isFullScreen):
                    self.updateFullScreen()
                AllBinaryMediaManager.setMuted(False)
            elif command == gameCommandsFactory.DISPLAY_LOAD_FORM:
                self.pauseAppBackground(False)
                keyValuePersistance: KeyValuePersistance = GamePersistanceSingleton.getInstance()
                keyValuePersistance.clear()
                keyValuePersistance.loadAll(self.abeClientInformation)
                if self.getLoadGameForm() == CommandForm.getNullCommandForm():
                    layerManager: AllBinaryGameLayerManager = self.createGameLayerManager()
                    self.setLoadGameForm(LoadGameForm(self, "Load Game", layerManager.getBackgroundBasicColor(), layerManager.getForegroundBasicColor()))
                else:
                    self.getLoadGameForm().update()
                self.commandAction(gameCommandsFactory.SET_MENU_DISPLAYABLE, self.getLoadGameForm())
            elif command == gameCommandsFactory.LOAD_FILE:
                loadGameForm: LoadGameForm = self.getLoadGameForm()
                index: int = loadGameForm.getSelectedId()
                if index != -1:
                    keyValuePersistance: KeyValuePersistance = GamePersistanceSingleton.getInstance()
                    self.setStartStateHashtable(keyValuePersistance.get(index))
                    menuListener: MenuListener = self.getLoadGameForm()
                    menuListener.close()
                    PreLogUtil.put(str(BasicMotionGesturesHandler.getInstance()), self, self.COMMAND_ACTION)
                    self.commandAction(gameCommandsFactory.START_COMMAND, NullCanvas.NULL_CANVAS)
                    PreLogUtil.put(str(BasicMotionGesturesHandler.getInstance()), self, self.COMMAND_ACTION)
            elif command == gameCommandsFactory.DELETE_FILE:
                loadGameForm: LoadGameForm = self.getLoadGameForm()
                index: int = loadGameForm.getSelectedText()
                if index != -1:
                    keyValuePersistance: KeyValuePersistance = GamePersistanceSingleton.getInstance()
                    keyValuePersistance.delete(self.abeClientInformation, index)
                    keyValuePersistance.clear()
                    keyValuePersistance.loadAllSize(self.abeClientInformation, 1)
                    self.getLoadGameForm().update()
            elif command == gameCommandsFactory.SAVE:
                keyValuePersistance: KeyValuePersistance = GamePersistanceSingleton.getInstance()
                self.pauseAppBackground(False)
                keyValuePersistance.save(self.abeClientInformation, self.getCurrentStateHashtable())
                self.unPauseAppBackground(False)
            elif command == HighScoreUtil.SUBMIT_TEXTBOX_COMMAND:
                self.logUtil.putF("Submitted Score", self, self.COMMAND_ACTION)
                if isinstance(displayable, HighScoreTextBox):
                    highScoreTextBox: HighScoreTextBox = displayable
                    highScoreTextBox.submitted = True
                allbinaryGameCanvasRunnableInterface.setHighScoreSubmitted(True)
                self.commandAction(gameCommandsFactory.CLOSE_AND_SHOW_GAME_CANVAS, displayable)
            elif command == gameCommandsFactory.DISPLAY_ABOUT:
                self.aboutCommandProcessor.process(self, gameCommandsFactory.SET_MENU_DISPLAYABLE, self.getAboutCanvas())
            elif command == gameCommandsFactory.OPEN_WEB_URL:
                self.webCommandProcessor.process(self, gameCommandsFactory.OPEN_WEB_URL, NullCanvas.NULL_CANVAS)
            elif command == gameCommandsFactory.TOGGLE_KEYBOARD:
                virtualKeyboardEventHandler: VirtualKeyboardEventHandler = VirtualKeyboardEventHandler.getInstance()
                virtualKeyboardEventHandler.fireEvent(virtualKeyboardEventHandler.SHOW_EVENT)
            elif ((command.getLabel() > gameCommandsFactory.TOGGLE_FULLSCREEN.getLabel()) - (command.getLabel() < gameCommandsFactory.TOGGLE_FULLSCREEN.getLabel())) == 0:
                mainFeatureFactory: MainFeatureFactory = MainFeatureFactory.getInstance()
                isFullScreen: bool = self.features.isFeature(mainFeatureFactory.FULL_SCREEN)
                if isFullScreen:
                    self.features.removeDefault(mainFeatureFactory.FULL_SCREEN)
                else:
                    self.features.addDefault(mainFeatureFactory.FULL_SCREEN)
                self.updateFullScreen()
        except Exception as e:
            self.logUtil.put(str(StringMaker().append(self.commonStrings.EXCEPTION_LABEL).append(command.getLabel())), self, self.midletStrings.COMMAND_ACTION, e)
            if command != GameCommandsFactory.getInstance().EXIT_COMMAND:
                self.exitProgress(False)
    

    def updateFullScreen(self) -> None:
        mainFeatureFactory: MainFeatureFactory = MainFeatureFactory.getInstance()
        isFullScreen: bool = self.features.isFeature(mainFeatureFactory.FULL_SCREEN)
        displayable: Displayable = self.getDisplay().getCurrent()
        if isinstance(displayable, Canvas):
            canvas: Canvas = displayable
            canvas.setFullScreenMode(isFullScreen)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def getInputMappingInstructionsCanvas(self) -> MyCanvas:
        return GameInputMappingInstructionsCanvas(self, self.createGameLayerManager())
    

    # throws Exception
    def getInputMappingCanvas(self) -> MyCanvas:
        return GameInputMappingCanvas(self.abeClientInformation, self, self.createGameLayerManager(), self.getHelpPaintable())
    

    # throws Exception
    def getAboutCanvas(self) -> MyCanvas:
        return BasicPaintablesCanvas(self, CanvasStrings.getInstance().ABOUT, self.createGameLayerManager(), AboutPaintableFactory.getInstance().paintableArray)
    

    # throws Exception
    def getHelpPaintable(self) -> HelpPaintable:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def createHighScoresCanvas(self) -> HighScoresCanvas:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def startGameCanvasRunnableInterface(self) -> None:
        threadFactoryUtil: ThreadFactoryUtil = ThreadFactoryUtil.getInstance()
        self.thread = threadFactoryUtil.getInstanceGameCanvasRunnable(self.allbinaryGameCanvasRunnableInterface)
        self.logUtil.putF(str(StringMaker().append("Thread Priority: ").appendint(int(self.thread.getPriority()))), self, "startGameCanvasRunnableInterface")
        self.allbinaryGameCanvasRunnableInterface.setThread(self.thread)
        threadFactoryUtil.start(self.thread)
    

    # throws Exception
    def stopGameCanvasRunnableInterface(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.gameStrings.STOP_GAME_CANVAS_RUNNABLE_INTERFACE)
        GameNotificationEventHandler.getInstance().removeAllListeners()
        ColorChangeEventHandler.getInstance().removeAllListeners()
        GameEventHandlerUtil.removeAllListeners()
        gameCanvasRunnableInterface: GameCanvasRunnableInterface = self.allbinaryGameCanvasRunnableInterface
        if gameCanvasRunnableInterface != NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE:
            self.logUtil.putF(str(StringMaker().append("Set Running False: ").append(str(gameCanvasRunnableInterface))), self, self.gameStrings.STOP_GAME_CANVAS_RUNNABLE_INTERFACE)
            gameCanvasRunnableInterface.setRunning(False)
        else:
            self.logUtil.putF("StopGame - Could Not Stop", self, self.gameStrings.STOP_GAME_CANVAS_RUNNABLE_INTERFACE)
        ThreadUtil.getInstance().join(self.thread)
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        if self.features.isFeature(MainFeatureFactory.getInstance().LOAD_ALL):
            progressCanvas.addNormalPortion(50, "Stopped Game Runnable")
        else:
            progressCanvas.addNormalPortion(50, "Stopped Main Runnable")
        self.logUtil.putF(self.commonStrings.END, self, self.gameStrings.STOP_GAME_CANVAS_RUNNABLE_INTERFACE)
    

    def getGameCanvasRunnableInterface(self) -> GameCanvasRunnableInterface:
        return self.allbinaryGameCanvasRunnableInterface
    

    def setGameCanvasRunnableInterface(self, gameCanvasRunnableInterface: GameCanvasRunnableInterface) -> None:
        self.allbinaryGameCanvasRunnableInterface = gameCanvasRunnableInterface
    

    def createGameLayerManager(self) -> AllBinaryGameLayerManager:
        gameInfo: GameInfo = GameInfo(GameTypeFactory.getInstance().SINGLE_PLAYER, GameMode.SERVER, PlayerTypesFactory.getInstance().PLAYER_TYPE_ONE, 1, 1)
        return AllBinaryGameLayerManager(self.basicColorFactory.BLACK, self.basicColorFactory.WHITE, gameInfo)
    

    def getGameOptionsForm(self) -> CommandForm:
        layerManager: AllBinaryGameLayerManager = self.createGameLayerManager()
        return GameOptionsFormFactory.getInstance().init(self, "Game Options", layerManager.getBackgroundBasicColor(), layerManager.getForegroundBasicColor())
    

    # throws Exception
    def save(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.SAVE)
        hashtable: ABHashtable[object, object] = self.getCurrentStateHashtable()
        GamePersistanceSingleton.getInstance().save(self.abeClientInformation, hashtable)
    

    # throws Exception
    def getCurrentStateHashtable(self) -> ABHashtable[object, object]:
        self.logUtil.putF(self.commonStrings.START, self, "getCurrentStateHashtable")
        hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        if self.allbinaryGameCanvasRunnableInterface != NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE:
            currentHashtable: ABHashtable[object, object] = self.allbinaryGameCanvasRunnableInterface.getCurrentStateHashtable()
            enumeration: Enumeration = currentHashtable.keys()
            key: object = None
            while self.enumerationUtil.hasMoreElements(enumeration):
                key = self.enumerationUtil.nextElement(enumeration)
                hashtable.put(key, currentHashtable.get(key))
        return hashtable
    

    def setLoadGameForm(self, loadGameForm: LoadGameForm) -> None:
        self.loadGameForm = loadGameForm
    

    def getLoadGameForm(self) -> CommandForm:
        return self.loadGameForm
    

    def setResized(self, resized: bool) -> None:
        self.resized = resized
    

    def isResized(self) -> bool:
        return self.resized
    

    def isDemoLoading(self) -> bool:
        if self.startedBefore:
            return False
        displayable: Displayable = self.getDisplay().getCurrent()
        if isinstance(displayable, DemoCanvas):
            demoCanvas: DemoCanvas = displayable
            if demoCanvas.isDemoLoading():
                return True
        return False
# from java.util.Enumeration import Enumeration
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.lcdui.NullCanvas import NullCanvas
# from javax.microedition.midlet.MIDletStateChangeException import MIDletStateChangeException
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.TsUtil import TsUtil
from org.allbinary.business.advertisement.GameAdStateFactory import GameAdStateFactory
from org.allbinary.canvas.FullScreenUtil import FullScreenUtil
from org.allbinary.canvas.GameStatisticsFactory import GameStatisticsFactory
from org.allbinary.debug.DebugFactory import DebugFactory
from org.allbinary.debug.DebugInterface import DebugInterface
from org.allbinary.game.GameAdState import GameAdState
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.GameMode import GameMode
from org.allbinary.game.GameStrings import GameStrings
from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.game.PlayerTypesFactory import PlayerTypesFactory
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.GameOptionsForm import GameOptionsForm
from org.allbinary.game.configuration.GameOptionsFormFactory import GameOptionsFormFactory
from org.allbinary.game.configuration.InGameFeatures import InGameFeatures
from org.allbinary.game.configuration.InGameOptionsForm import InGameOptionsForm
from org.allbinary.game.configuration.InGameOptionsFormFactory import InGameOptionsFormFactory
from org.allbinary.game.configuration.LoadGameForm import LoadGameForm
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.game.configuration.event.GameFeatureEventHandler import GameFeatureEventHandler
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFormUtil import GameFeatureFormUtil
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.game.configuration.persistance.GamePersistanceSingleton import GamePersistanceSingleton
from org.allbinary.game.configuration.persistance.KeyValuePersistance import KeyValuePersistance
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.displayable.canvas.BasicPaintablesCanvas import BasicPaintablesCanvas
from org.allbinary.game.displayable.canvas.DemoCanvas import DemoCanvas
from org.allbinary.game.displayable.canvas.GameCanvasRunnableInterface import GameCanvasRunnableInterface
from org.allbinary.game.displayable.canvas.GameEventHandlerUtil import GameEventHandlerUtil
from org.allbinary.game.displayable.canvas.GameInputMappingCanvas import GameInputMappingCanvas
from org.allbinary.game.displayable.canvas.GameInputMappingInstructionsCanvas import GameInputMappingInstructionsCanvas
from org.allbinary.game.displayable.canvas.MenuListener import MenuListener
from org.allbinary.game.displayable.canvas.NullGameCanvasRunnable import NullGameCanvasRunnable
from org.allbinary.game.input.TextNotificationUtil import TextNotificationUtil
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.paint.help.HelpPaintable import HelpPaintable
from org.allbinary.game.score.HighScoreCommands import HighScoreCommands
from org.allbinary.game.score.HighScoreCommandsFactory import HighScoreCommandsFactory
from org.allbinary.game.score.displayable.HighScoreTextBox import HighScoreTextBox
from org.allbinary.game.score.displayable.HighScoreUtil import HighScoreUtil
from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
from org.allbinary.game.state.GameStateFactory import GameStateFactory
from org.allbinary.graphics.ResizableListenerHandler import ResizableListenerHandler
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.ColorChangeEventHandler import ColorChangeEventHandler
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.graphics.displayable.screen.AboutCommandProcessor import AboutCommandProcessor
from org.allbinary.graphics.displayable.screen.AboutPaintableFactory import AboutPaintableFactory
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm
from org.allbinary.graphics.displayable.screen.WebCommandProcessor import WebCommandProcessor
from org.allbinary.input.AllBinarySensorManager import AllBinarySensorManager
from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.ClientInformationFactory import ClientInformationFactory
from org.allbinary.logic.system.security.licensing.InApplicationPurchaseFactory import InApplicationPurchaseFactory
from org.allbinary.logic.system.security.licensing.LockableFeature import LockableFeature
from org.allbinary.logic.system.security.licensing.LockableFeatureFactory import LockableFeatureFactory
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.audio.AllBinaryMediaManager import AllBinaryMediaManager
from org.allbinary.midlet.MidletStrings import MidletStrings
from org.allbinary.thread.NullThread import NullThread
from org.allbinary.thread.ThreadFactoryUtil import ThreadFactoryUtil
from org.allbinary.thread.ThreadUtil import ThreadUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.EnumerationUtil import EnumerationUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.game.midlet.GameMidletStateFactory import GameMidletStateFactory


