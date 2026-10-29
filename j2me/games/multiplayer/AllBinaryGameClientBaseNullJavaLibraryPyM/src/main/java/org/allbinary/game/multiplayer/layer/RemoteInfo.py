# 
# To change this license header, choose License Headers in Project Properties. 
# To change this template file, choose Tools | Templates 
# and open the template in the editor.  
# Generated Code Do Not Modify
# package org.allbinary.game.multiplayer.layer

from __future__ import annotations

from org.allbinary.logic.string.StringUtil import StringUtil


class RemoteInfo:
    NEW_PLAYER_ID: int = 0
    REMOTE_INFO: RemoteInfo = None
    

    def __init__(self, username: str, actorSessionId: int, playerInputId: int, id: int) -> None:
        pass


RemoteInfo.REMOTE_INFO = RemoteInfo(StringUtil.getInstance().EMPTY_STRING, -1, -1, RemoteInfo.NEW_PLAYER_ID)

