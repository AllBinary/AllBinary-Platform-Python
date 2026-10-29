# Generated Code Do Not Modify
# package org.allbinary.logic.communication.sql

from __future__ import annotations



class SqlTypeStrings:
    instance: SqlTypeStrings = None

    def _init_fields(self) -> None:
        self.CHAR_COLUMN: str = "VARCHAR"
        self.INT_COLUMN: str = "VARCHAR"
        self.MAX_SIZE: str = "(255)"
        self.SIXTY_SIZE: str = "(60)"
        self.NOT_NULL: str = "NOT NULL"
        self.ONE_SIZE: str = "(1)"
        self.TWO_SIZE: str = "(2)"
        self.THREE_SIZE: str = "(3)"
        self.SIX_SIZE: str = "(6)"
        self.ELEVEN_SIZE: str = "(11)"
        self.TWELVE_SIZE: str = "(12)"
        self.ONE_KB_CHAR_COLUMN: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append("(1024)").append(CommonSeps.getInstance().COMMA_SEP))
        self.MAX_CHAR_COLUMN: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append(self.MAX_SIZE).append(CommonSeps.getInstance().COMMA_SEP))
        self.MAX_CHAR_COLUMN_NOT_NULL: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append(self.MAX_SIZE).append(CommonSeps.getInstance().SPACE).append(self.NOT_NULL).append(CommonSeps.getInstance().COMMA_SEP))
        self.SIXTY_CHAR_COLUMN_NOT_NULL: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append(self.SIXTY_SIZE).append(self.NOT_NULL).append(CommonSeps.getInstance().COMMA_SEP))
        self.ONE_CHAR_COLUMN_NOT_NULL: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append(self.ONE_SIZE).append(self.NOT_NULL).append(CommonSeps.getInstance().COMMA_SEP))
        self.SIX_CHAR_COLUMN_NOT_NULL: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append(self.SIX_SIZE).append(self.NOT_NULL).append(CommonSeps.getInstance().COMMA_SEP))
        self.TWELVE_CHAR_COLUMN_NOT_NULL: str = str(StringMaker().append(CommonSeps.getInstance().SPACE).append(self.CHAR_COLUMN).append(self.TWELVE_SIZE).append(self.NOT_NULL).append(CommonSeps.getInstance().COMMA_SEP))
        self.TWO_INT_NOT_NULL: str = " INT(2) NOT NULL, "
        self.THREE_INT_NOT_NULL: str = " INT(3) NOT NULL, "
        self.FOUR_INT_NOT_NULL: str = " INT(4) NOT NULL, "
        self.MAX_INT_NOT_NULL: str = " INT(11) NOT NULL, "
        self.MAX_INT_UNSIGNED: str = " INT(11) UNSIGNED, "
        self.MAX_INT_UNSIGNED_NOT_NULL: str = " INT(11) UNSIGNED NOT NULL, "
        self.MAX_BIG_INT_NOT_NULL: str = " BIGINT(19) NOT NULL, "
        self.MAX_BIG_INT_UNSIGNED: str = " BIGINT(19) UNSIGNED, "
        self.MAX_BIG_INT_UNSIGNED_NOT_NULL: str = " BIGINT(19) UNSIGNED NOT NULL, "
        self.MAX_BIG_INT_UNSIGNED_AUTO_INCREMENT_NOT_NULL: str = " BIGINT(19) UNSIGNED AUTO_INCREMENT NOT NULL,"
        self.LONG_BLOB: str = " LONGBLOB, "
        self.BLOB: str = " BLOB, "
        self.BLOB_NOT_NULL: str = " BLOB NOT NULL, "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SqlTypeStrings:
        return SqlTypeStrings.instance
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


SqlTypeStrings.instance = SqlTypeStrings()

