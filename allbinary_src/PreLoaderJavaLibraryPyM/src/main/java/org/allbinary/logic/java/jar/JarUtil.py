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
# package org.allbinary.logic.java.jar

from __future__ import annotations

import traceback


class JarUtil:

    def _init_fields(self) -> None:
        self.jarURL: URL = None
    

    def __init__(self, jarURL: URL) -> None:
        self._init_fields()
        self.jarURL = jarURL
    

    def show(self) -> None:
        cache: list[int] = [0] * (1024)
        try:
            conn: URLConnection = self.jarURL.openConnection()
            jis: JarInputStream = JarInputStream(conn.getInputStream())
            while True:
                entry: JarEntry = jis.getNextJarEntry()
                if entry is not None:
                    if not entry.isDirectory():
                        offset: int = 0
                        i: int = 0
                        while ((i := jis.read(cache, offset, len(cache) - offset))) != -1:
                            offset += i
                            if offset >= len(cache):
                                newcache: list[int] = [0] * (len(cache) + 1024)
                                newcache[0:0 + len(cache)] = cache[0:0 + len(cache)]
                                cache = newcache
                        tmp: list[int] = [0] * (offset)
                        tmp[0:0 + offset] = cache[0:0 + offset]
                        print(entry.getName())
                else:
                    break
        except OSError as ex:
            print(ex)
            traceback.print_exception(ex)
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        JarUtil(URL("file:///G:/mnt/bc/mydev/working/j2me/MiniSpaceWars/MiniSpaceWars/dist/MiniSpaceWars.jar")).show()
# from java.io.IOException import IOException
# from java.net.URL import URL
# from java.net.URLConnection import URLConnection
# from java.util.jar.JarEntry import JarEntry
# from java.util.jar.JarInputStream import JarInputStream


