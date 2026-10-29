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
# package org.allbinary.android.input.motion.button

from __future__ import annotations

from org.allbinary.init.Init import Init


class TouchButtonAndroidResources(Init):

    def __init__(self) -> None:
        super().__init__()
    

    def init(self) -> None:
        from org.allbinary.android.input.motion.button.RESOURCE_STRING_ARRAY import RESOURCE_STRING_ARRAY
        from org.allbinary.android.input.motion.button.RESOURCE_ARRAY import RESOURCE_ARRAY
        resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        androidResources: AndroidResources = AndroidResources.getInstance()
        RESOURCE_STRING_ARRAY: list[TouchButtonResource] = [TouchButtonBlankResource.getInstance(), TouchButtonGenericActionResource.getInstance(), TouchButtonStartResource.getInstance(), TouchButtonUpResource.getInstance(), TouchButtonDownResource.getInstance(), TouchButtonTurnLeftResource.getInstance(), TouchButtonTurnRightResource.getInstance(), TouchButtonStrafeLeftResource.getInstance(), TouchButtonStrafeRightResource.getInstance()]
        RESOURCE_ARRAY: list[int] = [0] * (len(RESOURCE_STRING_ARRAY))
        if CommonButtons.getInstance().STANDARD_BUTTON_SIZE == 128:
            RESOURCE_ARRAY[0] = androidResources.raw.touch_button_128_by_128
            RESOURCE_ARRAY[1] = androidResources.raw.touch_button_generic_action_128_by_128
            RESOURCE_ARRAY[2] = androidResources.raw.touch_button_start_128_by_128
            RESOURCE_ARRAY[3] = androidResources.raw.touch_button_up_arrow_128_by_128
            RESOURCE_ARRAY[4] = androidResources.raw.touch_button_down_arrow_128_by_128
            RESOURCE_ARRAY[5] = androidResources.raw.touch_button_turn_left_arrow_128_by_128
            RESOURCE_ARRAY[6] = androidResources.raw.touch_button_turn_right_arrow_128_by_128
            RESOURCE_ARRAY[7] = androidResources.raw.touch_button_strafe_left_arrow_128_by_128
            RESOURCE_ARRAY[8] = androidResources.raw.touch_button_strafe_right_arrow_128_by_128
            if OperatingSystemFactory.getInstance().getOperatingSystemInstance().isOverScan():
                resourceUtil.addResource(RESOURCE_STRING_ARRAY[2].HINT, str(androidResources.raw.ouya_o))
        else:
            RESOURCE_ARRAY[0] = androidResources.raw.touch_button_64_by_64
            RESOURCE_ARRAY[1] = androidResources.raw.touch_button_generic_action_64_by_64
            RESOURCE_ARRAY[2] = androidResources.raw.touch_button_start_64_by_64
            RESOURCE_ARRAY[3] = androidResources.raw.touch_button_up_arrow_64_by_64
            RESOURCE_ARRAY[4] = androidResources.raw.touch_button_down_arrow_64_by_64
            RESOURCE_ARRAY[5] = androidResources.raw.touch_button_turn_left_arrow_64_by_64
            RESOURCE_ARRAY[6] = androidResources.raw.touch_button_turn_right_arrow_64_by_64
            RESOURCE_ARRAY[7] = androidResources.raw.touch_button_strafe_left_arrow_64_by_64
            RESOURCE_ARRAY[8] = androidResources.raw.touch_button_strafe_right_arrow_64_by_64
        for index in range(0, len(RESOURCE_ARRAY)):
            resourceUtil.addResource(RESOURCE_STRING_ARRAY[index].RESOURCE, str(RESOURCE_ARRAY[index]))
from org.allbinary.AndroidResources import AndroidResources
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.input.motion.button.CommonButtons import CommonButtons
from org.allbinary.input.motion.button.TouchButtonBlankResource import TouchButtonBlankResource
from org.allbinary.input.motion.button.TouchButtonDownResource import TouchButtonDownResource
from org.allbinary.input.motion.button.TouchButtonGenericActionResource import TouchButtonGenericActionResource
from org.allbinary.input.motion.button.TouchButtonResource import TouchButtonResource
from org.allbinary.input.motion.button.TouchButtonStartResource import TouchButtonStartResource
from org.allbinary.input.motion.button.TouchButtonStrafeLeftResource import TouchButtonStrafeLeftResource
from org.allbinary.input.motion.button.TouchButtonStrafeRightResource import TouchButtonStrafeRightResource
from org.allbinary.input.motion.button.TouchButtonTurnLeftResource import TouchButtonTurnLeftResource
from org.allbinary.input.motion.button.TouchButtonTurnRightResource import TouchButtonTurnRightResource
from org.allbinary.input.motion.button.TouchButtonUpResource import TouchButtonUpResource
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory


