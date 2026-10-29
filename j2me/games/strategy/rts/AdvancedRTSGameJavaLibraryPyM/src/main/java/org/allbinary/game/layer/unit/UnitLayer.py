# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.unit

from __future__ import annotations

import math
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.building.event.BuildingEventListenerInterface import BuildingEventListenerInterface
from org.allbinary.game.tracking.TrackingEventListenerInterface import TrackingEventListenerInterface
from org.allbinary.util.BasicArrayListS import BasicArrayListS


class UnitLayer(AdvancedRTSGameLayer, BuildingEventListenerInterface, TrackingEventListenerInterface):
    partialPositionList: BasicArrayList = BasicArrayListS(4)
    SENSOR_RANGE_MULTIPLIER: int = 6
    MOVE: str = "Moving"

    def _init_fields(self) -> None:
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.groupCommonFactory: GroupCommonFactory = GroupCommonFactory.getInstance()
        self.layerPartialCellPositionsUtil: LayerPartialCellPositionsUtil = LayerPartialCellPositionsUtil.getInstance()
        self.layerDistanceUtil: LayerDistanceUtil = LayerDistanceUtil.getInstance()
        self.angleFactory: AngleFactory = AngleFactory.getInstance()
        self.cellPositionFactory: CellPositionFactory = CellPositionFactory.getInstance()
        self.maxResourceLoad: int = None
        self.vehicleProperties: VehicleProperties = None
        self.accelerationBasicDecimal: BasicDecimal = BasicDecimal(1600)
        self.decelerationBasicDecimal: BasicDecimal = BasicDecimal(-1000)
        self.trackingEvent: TrackingEvent = None
        self.damageFloaters: DamageFloaters = None
        self.damageFloatersPaintableInterface: Paintable = None
        self.healthBar: Paintable = None
        self.moveSoundInterface: Sound = None
        self.initResourceAnimation: RotationAnimation = None
        self.resourceAnimation: IndexedAnimation = NullIndexedAnimationFactory.getFactoryInstance().getInstance(0)
        self.initPathAnimation: PathAnimation = None
        self.pathAnimation: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.captionAnimationHelper: CaptionAnimationHelperBase = CaptionAnimationHelper(FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(CaptionResources.getInstance().RESOURCE).getInstance(0), -23, -25, 6, 0)
        self.decalAnimation: RotationAnimation = None
        self.waypointLayerInterfaceFactoryInterface: LayerInterfaceFactoryInterface = None
        self.resourceLoad: int = 0
        self.weaponRange: int = 0
        self.rtsLogHelper: RTSLayerLogHelper = RTSLayerLogHelper.getInstance()
        self.rotationAnimationInterfaceP: RotationAnimation = None
        self.movementAngle: NamedAngle = self.angleFactory.NOT_ANGLE
        self.steeringInsideGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.sensorGeographicMapCellPositionList: BasicArrayList = BasicArrayListD()
        self.CAPITAL_EVENT: CapitalEvent = CapitalEvent(self)
    

    def __init__(self, remoteInfo: RemoteInfo, parentLayer: PathFindingLayerInterface, advancedRTSProperties: AdvancedRTSProperties, groupInterface: list[Group], rootName: str, name: str, vehicleProperties: VehicleProperties, healthInterface: Health, maxResourceLoad: int, moveSoundInterface: Sound, waypointLayerInterfaceFactoryInterface: LayerInterfaceFactoryInterface, animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, decalAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, resourceAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface: ProceduralAnimationInterfaceFactoryInterface, rectangle: Rectangle, direction: Direction, x: int, y: int, z: int, viewPosition: ViewPositionBase) -> None:
        from org.allbinary.game.layer.unit.CollidableUnitBehavior import CollidableUnitBehavior
        super().__init__(remoteInfo, parentLayer, advancedRTSProperties, groupInterface, rootName, name, healthInterface, WaypointRTSFormInput(groupInterface, True), animationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface, rectangle, x, y, viewPosition)
        self._init_fields()
        self.setCollidableInferface(CollidableUnitBehavior(True))
        self.waypointLayerInterfaceFactoryInterface = waypointLayerInterfaceFactoryInterface
        self.maxResourceLoad = int(maxResourceLoad)
        self.moveSoundInterface = moveSoundInterface
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().DAMAGE_FLOATERS):
            self.damageFloaters = PtsDamageFloaters(self)
            self.damageFloatersPaintableInterface = self.damageFloaters
        else:
            self.damageFloatersPaintableInterface = NullPaintable.getInstance()
            self.damageFloaters = DamageFloaters()
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().HEALTH_BARS):
            self.healthBar = HealthBar(self, self.getHealthInterface(), HealthBarTwodAnimation(self, BasicHudFactory.getInstance().BOTTOMLEFT), -1)
        else:
            self.healthBar = NullPaintable.getInstance()
        self.decalAnimation = decalAnimationInterfaceFactoryInterface.getInstance(0)
        self.initResourceAnimation = resourceAnimationInterfaceFactoryInterface.getInstance(0)
        self.initResourceAnimation.setFrameByDirection(direction)
        self.decalAnimation.setFrameByDirection(direction)
        self.rotationAnimationInterfaceP = self.indexedButShouldBeRotationAnimationInterface
        self.rotationAnimationInterfaceP.setFrameByDirection(direction)
        self.setMaxLevel(12)
        self.vehicleProperties = vehicleProperties
        self.trackingEvent = TrackingEvent(self)
        self.initPathAnimation = PathAnimation(self, LinePathRelativeAnimation.getInstance())
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        self.initPathAnimation.setAllBinaryGameLayerManager(allBinaryGameLayerManager)
    

    # throws Exception
    def updateWaypointBehavior(self, geographicMapInterface: BasicGeographicMap) -> None:
        from org.allbinary.game.layer.unit.UnitWaypointBehavior2 import UnitWaypointBehavior2
        hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        hashtable.put(self.groupCommonFactory.ID, self.getGroupInterface())
        hashtable.put(Layer.ID, self)
        hashtable.put(AllBinaryGameLayerManager.ID, self.allBinaryGameLayerManagerP)
        self.setWaypointBehavior(UnitWaypointBehavior2(self, self.waypointLayerInterfaceFactoryInterface.getNextInstance(hashtable, self.x, self.y, self.z)))
        features: Features = Features.getInstance()
        waypoint: WaypointBase = (MultipassNoCacheWaypoint(self, AttackSound.getInstance()) if J2MEUtil.isHTML() else NoCacheWaypoint(self, AttackSound.getInstance()))
        self.getWaypointBehavior().setWaypoint(waypoint)
        super().updateWaypointBehavior(geographicMapInterface)
        self.initRangeHack()
    

    # throws Exception
    def construct(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        super().construct(rtsPlayerLayerInterface)
        TrackingEventHandler.getInstance().addListenerInterface(self)
        WaypointEventHandlerFactory.getInstance(self.getGroupInterface()[0]).addListenerInterface(self.getUnitWaypointBehavior())
        BuildingEventHandler.getInstance().addListenerInterface(self)
        self.getUnitWaypointBehavior().setCurrentPathGeographicMapCellPosition(self.getCurrentGeographicMapCellPosition())
        self.updateSensorGeographicMapCellPositionList()
        self.getUnitWaypointBehavior().setLastPathGeographicMapCellPosition(self.getUnitWaypointBehavior().getCurrentPathGeographicMapCellPosition())
    

    # throws Exception
    def updateSensorGeographicMapCellPositionList(self) -> None:
        if VisibleCellPositionsSingleton.getInstance().shouldProcess():
            currentGeographicMapCellPosition: GeographicMapCellPosition = self.getCurrentGeographicMapCellPosition()
            self.sensorGeographicMapCellPositionList.clear()
            self.sensorGeographicMapCellPositionList.add(currentGeographicMapCellPosition)
            sensorRange: int = self.weaponRange * UnitLayer.SENSOR_RANGE_MULTIPLIER
            geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
            totalCells: int = (sensorRange / tiledLayer.getCellHeight()) / 2
            geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
            column: int = currentGeographicMapCellPosition.getColumn()
            row: int = currentGeographicMapCellPosition.getRow()
            lastColumn: int = column + totalCells
            lastRow: int = row + totalCells
            if lastColumn > tiledLayer.getColumns():
                lastColumn = tiledLayer.getColumns()
            if lastRow > tiledLayer.getRows():
                lastRow = tiledLayer.getRows()
            firstColumn: int = column - totalCells
            firstRow: int = row - totalCells
            if firstColumn < 0:
                firstColumn = 0
            if firstRow < 0:
                firstRow = 0
            for index in range(lastColumn - 1, firstColumn - 1, -1):
                for index2 in range(lastRow - 1, firstRow - 1, -1):
                    geographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(index, index2)
                    if not self.sensorGeographicMapCellPositionList.contains(geographicMapCellPosition):
                        self.sensorGeographicMapCellPositionList.add(geographicMapCellPosition)
    

    def getSensorGeographicMapCellPositionList(self) -> BasicArrayList:
        return self.sensorGeographicMapCellPositionList
    

    def select(self) -> None:
        self.pathAnimation = self.initPathAnimation
        super().select()
    

    def deselect(self) -> None:
        self.pathAnimation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        super().deselect()
    

    def setSelected(self, selected: bool) -> None:
        super().setSelected(selected)
        if selected:
            if self.debug:
                self.rtsLogHelper = RTSLayerSelectedLogHelper.getInstance()
            self.rtsLayer2LogHelper = RTSLayer2SelectedLogHelper.getInstance()
        else:
            if self.debug:
                self.rtsLogHelper = RTSLayerLogHelper.getInstance()
            self.rtsLayer2LogHelper = RTSLayer2LogHelper.getInstance()
    

    # throws Exception
    def setClosestGeographicMapCellHistory(self, pathsList: BasicArrayList) -> None:
        self.rtsLogHelper.setClosestGeographicMapCellHistory(self, pathsList)
        closestIndex: int = -1
        shortestDistance: int = 2147483647
        currentDistance: int = 2147483647
        for index in range(pathsList.size() - 1, 0 - 1, -1):
            geographicMapCellPositionBasicArrayList: BasicArrayList = pathsList.get(index)
            geographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionBasicArrayList.get(geographicMapCellPositionBasicArrayList.size() - 1)
            currentDistance = self.layerDistanceUtil.getDistanceAt(self, geographicMapCellPosition.getMidPoint())
            if currentDistance < shortestDistance:
                shortestDistance = currentDistance
                closestIndex = index
        if closestIndex >= 0:
            geographicMapCellPositionBasicArrayList: BasicArrayList = pathsList.get(closestIndex)
            geographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionBasicArrayList.get(0)
            self.teleportTo(geographicMapCellPosition)
    

    # throws Exception
    def init(self, geographicMapCellHistory: GeographicMapCellHistory, geographicMapCellPositionBasicArrayList: BasicArrayList) -> None:
        geographicMapCellHistory.trackAll(geographicMapCellPositionBasicArrayList)
    

    def onMovement(self, trackingEvent: TrackingEvent) -> None:
        try:
            layerInterface: AdvancedRTSGameLayer = trackingEvent.getLayerInterface()
            if layerInterface.getGroupInterface()[0] != self.getGroupInterface()[0]:
                self.getUnitWaypointBehavior().getPossibleTargetList().add(layerInterface)
                layerInterface.onMovementFound(self.getTrackingEvent())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onMovement", e)
    

    # throws Exception
    def onMovementFound(self, trackingEvent: TrackingEvent) -> None:
        layerInterface: AdvancedRTSGameLayer = trackingEvent.getLayerInterface()
        if layerInterface.getGroupInterface()[0] != self.getGroupInterface()[0]:
            self.getUnitWaypointBehavior().getPossibleTargetList().add(layerInterface)
    

    def initRangeHack(self) -> None:
        basicWeaponPart: BasicWeaponPart = self.getPartInterfaceArray()[0]
        weaponProperties: WeaponProperties = basicWeaponPart.getWeaponProperties()
        self.weaponRange = weaponProperties.getRange()
        self.initRangeAnimation = AdjustedCircleAnimation.createW(self.weaponRange, self.weaponRange, self.getWidth(), self.basicColorFactory.GREEN)
        sensorRange: int = self.weaponRange * UnitLayer.SENSOR_RANGE_MULTIPLIER
        self.initSensorRangeAnimation = AdjustedCircleAnimation.createW(sensorRange, sensorRange, self.getWidth(), self.basicColorFactory.RED)
        self.getUnitWaypointBehavior().initRange(self.weaponRange)
        self.fireTimeHelper.delay = (int(weaponProperties.getReloadTime()))
    

    # throws Exception
    def processBuiltTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if not self.getHealthInterface().isAlive():
            if self.isReadyForExplosion():
                currentFrame: int = self.destroyAnimationInterface.getFrame()
                size: int = self.destroyAnimationInterface.getSize() - 1
                if currentFrame == size:
                    if not self.getHealthInterface().isAlive():
                        self.setDestroyed(True)
                else:
                    self.destroyAnimationInterface.nextFrame()
            else:
                self.setAnimationInterface(self.destroyAnimationInterface)
                SecondaryPlayerQueueFactory.getInstance().add(ExplosionBasicSound.getInstance())
                self.shakeListener.onSmallShakeEvent()
                self.vibration.vibrate(self.duration, 0, 0)
                self.setReadyForExplosion(True)
        else:
            super().processBuiltTick(allBinaryLayerManager)
        self.captionAnimationHelper.tick()
        self.getUnitWaypointBehavior().processTick(allBinaryLayerManager)
    

    def teleportTo(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        point: GPoint = geographicMapCellPosition.getMidPoint()
        self.setPosition(point.getX() - self.getHalfWidth(), point.getY() - self.getHalfHeight(), self.z)
    

    # throws Exception
    def getCurrentGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        geographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXY(self.x + self.getHalfWidth(), self.y + self.getHalfHeight())
        raceTrackGeographicMap: RaceTrackGeographicMap = geographicMapInterface
        if not raceTrackGeographicMap.isValid(geographicMapCellPosition):
            raise Exception("Position is not really on the map: " + str(geographicMapCellPosition))
        return geographicMapCellPosition
    

    # throws Exception
    def fire(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        if self.fireTimeHelper.isTimeTNT():
            self.fireAll(layerManager)
        else:
            self.reload()
    

    # throws Exception
    def left(self) -> None:
        self.initResourceAnimation.previousRotation()
        self.decalAnimation.previousRotation()
        self.rotationAnimationInterfaceP.previousRotation()
    

    # throws Exception
    def right(self) -> None:
        self.initResourceAnimation.nextRotation()
        self.decalAnimation.nextRotation()
        self.rotationAnimationInterfaceP.nextRotation()
    

    def down(self) -> None:
        velocityProperties: VelocityProperties = self.getVehicleProperties().getVelocityProperties()
        if not velocityProperties.isOverXYMaxForwardVelocity():
            self.accelerate(self.decelerationBasicDecimal)
    

    def up(self) -> None:
        velocityProperties: VelocityProperties = self.getVehicleProperties().getVelocityProperties()
        if not velocityProperties.isOverXYMaxForwardVelocity():
            self.accelerate(self.accelerationBasicDecimal)
    

    def initInputProcessors(self) -> None:
        self.inputProcessorArray[Canvas.RIGHT] = SpecialRightGameInputProcessor(self)
        self.inputProcessorArray[Canvas.LEFT] = SpecialLeftGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_NUM0] = SpecialFireGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_POUND] = self.inputProcessorArray[Canvas.KEY_NUM0]
        self.inputProcessorArray[Canvas.DOWN] = SpecialDownGameInputProcessor(self)
        self.inputProcessorArray[Canvas.UP] = SpecialUpGameInputProcessor(self)
        super().initInputProcessors()
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        list_: BasicArrayList = self.getGameKeyEventList()
        size: int = list_.size()
        for index in range(0, size):
            anyType: object = list_.get(index)
            key: int = GameKeyEventUtil.getKey(anyType)
            self.inputProcessorArray[key].processEvent(layerManager, GameKeyEvent.NONE)
        list_.clear()
        self.groundFriction()
        self.move()
    

    def accelerate(self, accelerate: BasicDecimal) -> None:
        self.getVehicleProperties().getVelocityProperties().addVelocityi(accelerate.getUnscaled(), int(self.rotationAnimationInterfaceP.getAngleInfoP().getAngle()), 90)
    

    # throws Exception
    def fireAll(self, layerManager: AllBinaryLayerManager) -> None:
        angleInfo: AngleInfo = self.rotationAnimationInterfaceP.getAngleInfoP()
        angle: int = int((angleInfo.getAngle() + self.slightAngle))
        self.hashtable.put(SmallIntegerSingletonFactory.getInstance().getAt(1), SmallIntegerSingletonFactory.getInstance().getAt(int(AngleFactory.getInstance().getAt(angle).getValue())))
        salvoInterface: SalvoInterface = self.getPartInterfaceArray()[0]
        salvoInterface.process(layerManager, ((int(angle) + 32768) % 65536 - 32768), ((int(90) + 32768) % 65536 - 32768))
    

    def downgrade(self) -> None:
        if self.getLevel() > 1:
            super().downgrade()
    

    def upgrade(self) -> None:
        super().upgrade()
        self.initRangeHack()
    

    def groundFriction(self) -> None:
        vehicleFrictionProperties: VehicleFrictionProperties = self.getVehicleProperties().getVehicleFrictionProperties()
        self.getVehicleProperties().getVehicleFrictionProperties().friction(self.getVehicleProperties().getVelocityProperties(), vehicleFrictionProperties.getTireFrictionNominator())
    

    # throws Exception
    def trackTo(self, reason: str) -> None:
        waypointBehaviorBase: WaypointBehaviorBase = self.waypointBehaviorBase
        nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition = waypointBehaviorBase.getNextUnvisitedPathGeographicMapCellPosition()
        point: GPoint = nextUnvisitedPathGeographicMapCellPosition.getMidPoint()
        dx: int = (self.getXP() + self.getHalfWidth()) - point.getX()
        dy: int = (self.getYP() + self.getHalfHeight()) - point.getY()
        self.rtsLogHelper.trackTo(self, nextUnvisitedPathGeographicMapCellPosition, dx, dy, reason)
        self.trackToDXY(dx, dy)
    

    # throws Exception
    def trackToDXY(self, dx: int, dy: int) -> None:
        angleOfTarget: int = 0
        self.trackToDXYTargetAngle(dx, dy, angleOfTarget)
    

    # throws Exception
    def turnTo(self, dx: int, dy: int, targetAngle: int) -> bool:
        waypointBehaviorBase: WaypointBehaviorBase = self.waypointBehaviorBase
        nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition = waypointBehaviorBase.getNextUnvisitedPathGeographicMapCellPosition()
        evading: bool = False
        if self.getUnitWaypointBehavior().getSensorAction() == SensorActionFactory.getInstance().EVADE:
            self.rtsLogHelper.evade(self)
            evading = True
            targetAngle += 180
        angleInfo: AngleInfo = self.rotationAnimationInterfaceP.getAngleInfoP()
        angle: int = FrameUtil.getInstance().adjustAngleToFrameAngle(angleInfo.getAngle() - 270)
        self.rtsLogHelper.turnTo(self, dx, dy, angleInfo, angle, self.movementAngle, evading, targetAngle)
        gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        if dx == 0 and dy == 0:
            self.rtsLogHelper.doneMoving(self)
            return True
        elif (int(self.movementAngle.getValue())) == angle:
            if dx > 0 and self.movementAngle == self.angleFactory.LEFT:
                self.rtsLogHelper.movingLeft(self)
                return False
            if dx < 0 and self.movementAngle == self.angleFactory.RIGHT:
                self.rtsLogHelper.movingRight(self)
                return False
            if dy > 0 and self.movementAngle == self.angleFactory.UP:
                self.rtsLogHelper.movingUp(self)
                return False
            if dy < 0 and self.movementAngle == self.angleFactory.DOWN:
                self.rtsLogHelper.movingDown(self)
                return False
            self.rtsLogHelper.currentMoveEnded(self)
            if self.movementAngle == self.angleFactory.LEFT or self.movementAngle == self.angleFactory.RIGHT:
                self.handleDeltalY(dx, dy)
            elif self.movementAngle == self.angleFactory.UP or self.movementAngle == self.angleFactory.DOWN:
                self.handleDeltalX(dx, dy)
            return True
        else:
            if nextUnvisitedPathGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
                if self.steeringInsideGeographicMapCellPosition != nextUnvisitedPathGeographicMapCellPosition:
                    if abs(dx) > abs(dy) and dy != 0:
                        self.handleDeltalY(dx, dy)
                    elif dx != 0:
                        self.handleDeltalX(dx, dy)
                    else:
                        self.handleDeltalY(dx, dy)
                deltaAngle2: int = self.movementAngle.getValue() - angle
                if deltaAngle2 > 0:
                    self.rtsLogHelper.rotateRight(self)
                    self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.RIGHT))
                else:
                    self.rtsLogHelper.rotateLeft(self)
                    self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.LEFT))
                return True
            else:
                self.rtsLogHelper.noRotation(self)
            return False
    

    def handleDeltalX(self, dx: int, dy: int) -> None:
        waypointBehaviorBase: WaypointBehaviorBase = self.waypointBehaviorBase
        nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition = waypointBehaviorBase.getNextUnvisitedPathGeographicMapCellPosition()
        if dx > 0:
            self.movementAngle = self.angleFactory.LEFT
            self.steeringInsideGeographicMapCellPosition = nextUnvisitedPathGeographicMapCellPosition
        else:
            self.movementAngle = self.angleFactory.RIGHT
            self.steeringInsideGeographicMapCellPosition = nextUnvisitedPathGeographicMapCellPosition
        self.rtsLogHelper.handle(self, self.movementAngle)
    

    def handleDeltalY(self, dx: int, dy: int) -> None:
        waypointBehaviorBase: WaypointBehaviorBase = self.waypointBehaviorBase
        nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition = waypointBehaviorBase.getNextUnvisitedPathGeographicMapCellPosition()
        if dy > 0:
            self.movementAngle = self.angleFactory.UP
            self.steeringInsideGeographicMapCellPosition = nextUnvisitedPathGeographicMapCellPosition
        else:
            self.movementAngle = self.angleFactory.DOWN
            self.steeringInsideGeographicMapCellPosition = nextUnvisitedPathGeographicMapCellPosition
        self.rtsLogHelper.handle(self, self.movementAngle)
    

    # throws Exception
    def trackToDXYTargetAngle(self, dx: int, dy: int, targetAngle: int) -> None:
        list_: BasicArrayList = self.getUnitWaypointBehavior().getSteeringVisitorList()
        if list_.size() > 0:
            for index in range(list_.size() - 1, 0 - 1, -1):
                steeringVisitor: SteeringVisitor = list_.get(index)
                anyType: object = steeringVisitor.visit(self)
                if anyType is None:
                    list_.removeAt(index)
            self.fireOrMove()
        elif not self.turnTo(dx, dy, targetAngle):
            self.fireOrMove()
    

    # throws Exception
    def fireOrMove(self) -> None:
        gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        if self.getUnitWaypointBehavior().needToMove():
            self.rtsLayer2LogHelper.steeringUp(self)
            if self.showMoreCaptionStates and not self.captionAnimationHelper.isShowing():
                self.captionAnimationHelper.update(UnitLayer.MOVE, self.basicColorFactory.GREEN)
            self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.UP))
        else:
            self.captionAnimationHelper.update(CommonPhoneStrings.getInstance().FIRE, self.basicColorFactory.RED)
            self.rtsLayer2LogHelper.steeringFireOrStop(self)
            self.allStop()
            self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.KEY_NUM0))
            TrackingEventHandler.getInstance().fireEvent(self.getTrackingEvent())
    

    def move(self) -> None:
        try:
            velocityProperties: VelocityProperties = self.getVehicleProperties().getVelocityProperties()
            velocityXScaled: int = int(velocityProperties.getVelocityXBasicDecimalP().getScaled())
            velocityYScaled: int = int(velocityProperties.getVelocityYBasicDecimalP().getScaled())
            self.getUnitWaypointBehavior().move()
            if velocityXScaled != 0 or velocityYScaled != 0:
                self.getUnitWaypointBehavior().setMoving(True)
                geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
                geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
                self.layerPartialCellPositionsUtil.getAllDXY(geographicMapInterface, self, velocityXScaled, velocityYScaled, UnitLayer.getPartialpositionlist())
                cellPosition: GeographicMapCellPosition = DropCellPositionHistory.getInstance().getCellPositionWithDrop(UnitLayer.getPartialpositionlist())
                if cellPosition == self.cellPositionFactory.NONE:
                    tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
                    tiledLayerUtil: TiledLayerUtil = TiledLayerUtil.getInstance()
                    x: int = self.x + velocityXScaled
                    y: int = self.y + velocityYScaled
                    x = tiledLayerUtil.keepOnMapX(tiledLayer, x, self.getWidth())
                    y = tiledLayerUtil.keepOnMapY(tiledLayer, y, self.getHeight())
                    self.setPosition(x, y, self.z)
                else:
                    allbinaryLayer: AllBinaryLayer = DropCellPositionHistory.getInstance().getLayerInterface(cellPosition)
                    self.getUnitWaypointBehavior().setMovingFromStopped(False)
                    self.getUnitWaypointBehavior().addBuildingChase(allbinaryLayer, cellPosition)
            if self.getUnitWaypointBehavior().isMoving():
                TrackingEventHandler.getInstance().fireEvent(self.getTrackingEvent())
            else:
                self.getUnitWaypointBehavior().setMovingFromStopped(False)
            if self.getUnitWaypointBehavior().isMovingFromStopped() and self.isVisible():
                SecondaryPlayerQueueFactory.getInstance().add(self.moveSoundInterface)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "move", e)
    

    def allStop(self) -> None:
        velocityProperties: VelocityProperties = self.getVehicleProperties().getVelocityProperties()
        velocityProperties.getVelocityXBasicDecimalP().setint(0)
        velocityProperties.getVelocityYBasicDecimalP().setint(0)
    

    def paint(self, graphics: Graphics) -> None:
        if self.isVisible():
            super().paint(graphics)
            viewPosition: ViewPositionBase = self.getViewPosition()
            viewX: int = viewPosition.getX()
            viewY: int = viewPosition.getY()
            self.decalAnimation.paintXY(graphics, viewX, viewY)
            self.rangeAnimation.paintXY(graphics, viewX, viewY)
            self.sensorRangeAnimation.paintXY(graphics, viewX, viewY)
            self.damageFloatersPaintableInterface.paint(graphics)
            self.healthBar.paint(graphics)
            self.captionAnimationHelper.paintXY(graphics, viewX, viewY)
            self.pathAnimation.paintXY(graphics, viewX, viewY)
            self.resourceAnimation.paintXY(graphics, viewX, viewY)
    

    # throws Exception
    def onBuildingEvent(self, event: RTSLayerEvent) -> None:
        buildingLayer: BuildingLayer = event.getRtsLayer()
        self.getUnitWaypointBehavior().moveAwayFromBuilding(buildingLayer)
    

    def getVehicleProperties(self) -> VehicleProperties:
        return self.vehicleProperties
    

    # throws Exception
    def damage(self, damage: int, damageType: int) -> None:
        super().damage(damage, damageType)
        self.damageFloaters.add(damage)
        if damage > 0:
            self.getHealthInterface().damage(damage)
    

    # throws Exception
    def getDamage(self, damageType: int) -> int:
        return 0
    

    # throws Exception
    def setDestroyed(self, destroyed: bool) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "setDestroyed")
        super().setDestroyed(destroyed)
        if self.isDestroyed():
            WaypointEventHandlerFactory.getInstance(self.getGroupInterface()[0]).removeListener(self.getUnitWaypointBehavior())
            TrackingEventHandler.getInstance().removeListener(self)
            BuildingEventHandler.getInstance().removeListener(self)
            if not self.getHealthInterface().isAlive():
                damage: int = self.getHealthInterface().getMaxHealth()
                if damage > 10:
                    SecondaryPlayerQueueFactory.getInstance().add(ExplosionBasicSound.getInstance())
                    if damage < 100:
                        self.shakeListener.onSmallShakeEvent()
                        self.vibration.vibrate(self.duration, 0, 0)
                    elif damage < 1000:
                        self.shakeListener.onMediumShakeEvent()
                        self.vibration.vibrate(self.duration * 2, 0, 0)
                    elif damage < 3000:
                        self.shakeListener.onLargeShakeEvent()
                        self.vibration.vibrate(self.duration * 4, 0, 0)
    

    def getLoad(self) -> int:
        return self.resourceLoad
    

    # throws Exception
    def clearResourceAnimation(self) -> None:
        self.resourceAnimation = NullIndexedAnimationFactory.getFactoryInstance().getInstance(0)
    

    # throws Exception
    def setLoad(self, resource: int) -> None:
        if resource > 0:
            self.resourceAnimation = self.initResourceAnimation
        else:
            self.clearResourceAnimation()
        self.resourceLoad = resource
    

    def addLoad(self, resource: int) -> None:
        self.resourceLoad += resource
    

    # throws Exception
    def handleCost(self, ownerLayer: PathFindingLayerInterface) -> None:
        if self.getLoad() > 0:
            self.CAPITAL_EVENT.setValue(self.getLoad())
            CapitalEventHandlerFactory.getInstance(ownerLayer.getGroupInterface()[0]).fireEvent(self.CAPITAL_EVENT)
            self.setLoad(0)
    

    def createHudPaintable(self) -> SelectionHudPaintable:
        rtsLayerHudPaintable: RTSLayerHudPaintable = RTSLayerHudPaintable.getInstance()
        rtsLayerHudPaintable.setBasicColorP(self.allBinaryGameLayerManagerP.getForegroundBasicColor())
        rtsLayerHudPaintable.setRtsLayer(self)
        return rtsLayerHudPaintable
    

    def getHudPaintable(self) -> SelectionHudPaintable:
        rtsLayerHudPaintable: RTSLayerHudPaintable = RTSLayerHudPaintable.getInstance()
        return rtsLayerHudPaintable
    

    def getType(self) -> int:
        return UnitLayer.getStaticType()
    

    @staticmethod
    def getStaticType() -> int:
        return 1
    

    def getUnitWaypointBehavior(self) -> UnitWaypointBehavior:
        return self.getWaypointBehavior()
    

    def getTrackingEvent(self) -> TrackingEvent:
        return self.trackingEvent
    

    def getCaptionAnimationHelper(self) -> CaptionAnimationHelperBase:
        return self.captionAnimationHelper
    

    def isSelfUpgradeable(self) -> bool:
        return False
    

    def getMaxResourceLoad(self) -> int:
        return self.maxResourceLoad
    

    @staticmethod
    def getPartialpositionlist() -> BasicArrayList:
        return UnitLayer.partialPositionList
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.ag.weapon.media.audio.ExplosionBasicSound import ExplosionBasicSound
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.NullIndexedAnimationFactory import NullIndexedAnimationFactory
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.animation.RotationAnimation import RotationAnimation
from org.allbinary.animation.caption.CaptionAnimationHelper import CaptionAnimationHelper
from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase
from org.allbinary.animation.vector.AdjustedCircleAnimation import AdjustedCircleAnimation
from org.allbinary.direction.Direction import Direction
from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters
from org.allbinary.game.combat.damage.PtsDamageFloaters import PtsDamageFloaters
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.game.health.Health import Health
from org.allbinary.game.health.HealthBar import HealthBar
from org.allbinary.game.health.HealthBarTwodAnimation import HealthBarTwodAnimation
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.identification.GroupCommonFactory import GroupCommonFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.event.GameKeyEventUtil import GameKeyEventUtil
from org.allbinary.game.input.form.VisibleCellPositionsSingleton import VisibleCellPositionsSingleton
from org.allbinary.game.input.form.WaypointRTSFormInput import WaypointRTSFormInput
from org.allbinary.game.layer.AdvancedRTSProperties import AdvancedRTSProperties
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.layer.CaptionResources import CaptionResources
from org.allbinary.game.layer.LinePathRelativeAnimation import LinePathRelativeAnimation
from org.allbinary.game.layer.PathAnimation import PathAnimation
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.RTSLayer2LogHelper import RTSLayer2LogHelper
from org.allbinary.game.layer.RTSLayer2SelectedLogHelper import RTSLayer2SelectedLogHelper
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.RTSLayerHudPaintable import RTSLayerHudPaintable
from org.allbinary.game.layer.RTSLayerLogHelper import RTSLayerLogHelper
from org.allbinary.game.layer.RTSLayerSelectedLogHelper import RTSLayerSelectedLogHelper
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable
from org.allbinary.game.layer.SensorActionFactory import SensorActionFactory
from org.allbinary.game.layer.SteeringVisitor import SteeringVisitor
from org.allbinary.game.layer.TiledLayerUtil import TiledLayerUtil
from org.allbinary.game.layer.VehicleFrictionProperties import VehicleFrictionProperties
from org.allbinary.game.layer.VehicleProperties import VehicleProperties
from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
from org.allbinary.game.layer.building.BuildingLayer import BuildingLayer
from org.allbinary.game.layer.building.event.BuildingEventHandler import BuildingEventHandler
from org.allbinary.game.layer.capital.event.CapitalEvent import CapitalEvent
from org.allbinary.game.layer.capital.event.CapitalEventHandlerFactory import CapitalEventHandlerFactory
from org.allbinary.game.layer.geographic.map.LayerPartialCellPositionsUtil import LayerPartialCellPositionsUtil
from org.allbinary.game.layer.special.SpecialDownGameInputProcessor import SpecialDownGameInputProcessor
from org.allbinary.game.layer.special.SpecialFireGameInputProcessor import SpecialFireGameInputProcessor
from org.allbinary.game.layer.special.SpecialLeftGameInputProcessor import SpecialLeftGameInputProcessor
from org.allbinary.game.layer.special.SpecialRightGameInputProcessor import SpecialRightGameInputProcessor
from org.allbinary.game.layer.special.SpecialUpGameInputProcessor import SpecialUpGameInputProcessor
from org.allbinary.game.layer.waypoint.MultipassNoCacheWaypoint import MultipassNoCacheWaypoint
from org.allbinary.game.layer.waypoint.NoCacheWaypoint import NoCacheWaypoint
from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
from org.allbinary.game.layer.waypoint.event.WaypointEventHandlerFactory import WaypointEventHandlerFactory
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.game.part.weapon.BasicWeaponPart import BasicWeaponPart
from org.allbinary.game.part.weapon.SalvoInterface import SalvoInterface
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.graphics.CellPositionFactory import CellPositionFactory
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.Layer import Layer
from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.math.FrameUtil import FrameUtil
from org.allbinary.math.LayerDistanceUtil import LayerDistanceUtil
from org.allbinary.math.NamedAngle import NamedAngle
from org.allbinary.media.audio.AttackSound import AttackSound
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMap import RaceTrackGeographicMap
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.view.ViewPositionBase import ViewPositionBase


