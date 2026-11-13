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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class LastKeyAIVisitorFactory:
    instance: LastKeyAIVisitor = None
    

    @staticmethod
    def getInstance() -> LastKeyAIVisitor:
        return LastKeyAIVisitorFactory.instance


def _LastKeyAIVisitorFactory_instance() -> object:
    from org.allbinary.game.ag.ai.LastKeyAIVisitor import LastKeyAIVisitor
    return LastKeyAIVisitor()

lazy_static(LastKeyAIVisitorFactory, "instance", _LastKeyAIVisitorFactory_instance)

