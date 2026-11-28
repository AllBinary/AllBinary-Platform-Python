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
# package org.allbinary.game.ag.layer.weapon.mine

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.resources.BasicGameResources import BasicGameResources


@java_inherited_overloads
class MineWeaponResources(BasicGameResources):
    instance: object = None
    def _java_defaults(self):
        vars(self).setdefault("DROP_TEXT_RESOURCE", None)
        vars(self).setdefault("DROP_RESOURCE", None)
        vars(self).setdefault("DROP_ICON_RESOURCE", None)

    def _init_fields(self) -> None:
        self.DROP_TEXT_RESOURCE: str = "/mine_drop_text_20_by_20.png"
        self.DROP_RESOURCE: str = "/mine_drop_20_by_20.png"
        self.DROP_ICON_RESOURCE: str = "/mine_drop_icon_20_by_20.png"
    

    @staticmethod
    def getInstance() -> MineWeaponResources:
        from org.allbinary.logic.NullUtil import NullUtil
        if MineWeaponResources.instance == NullUtil.getInstance().NULL_OBJECT:
            MineWeaponResources.instance = MineWeaponResources()
        return MineWeaponResources.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        ROOT: str = "/mine"
        SMALL: str = "_20_by_20.png"
        MEDIUM: str = SMALL
        SIZE_FOUR: str = SMALL
        SIZE_FIVE: str = SMALL
        SIZE_SIX: str = SMALL
        SIZE: list[str] = [SMALL, MEDIUM, SIZE_FOUR, SIZE_FIVE, SIZE_SIX]
        java_super_call(super(), "init", ROOT, SIZE)
# from org.allbinary.logic.NullUtil import NullUtil


def _MineWeaponResources_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(MineWeaponResources, "instance", _MineWeaponResources_instance)

