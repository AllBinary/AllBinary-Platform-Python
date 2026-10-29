# Generated Code Do Not Modify
# package org.allbinary.logic.communication.sql

from __future__ import annotations



class SqlStrings:
    instance: SqlStrings = None

    def _init_fields(self) -> None:
        self.CREATE_DATABASE: str = "CREATE DATABASE "
        self.DROP_TABLE: str = "DROP TABLE "
        self.CREATE_TABLE: str = "CREATE TABLE "
        self.START: str = " ("
        self.SELECT: str = "SELECT "
        self.FROM: str = " FROM "
        self.SELECT_ALL: str = "SELECT *"
        self.WHERE: str = " WHERE "
        self.AND: str = " AND "
        self.UPDATE: str = "UPDATE "
        self.SET: str = " SET "
        self.SELECT_ALL_FROM: str = self.SELECT_ALL + self.FROM
        self.DELETE: str = "DELETE"
        self.LIKE_QUOTE: str = " LIKE \""
        self.INSERT_INTO: str = "INSERT INTO "
        self.VALUES: str = " VALUES ('"
        self.ORDER_BY: str = "ORDER BY"
        self.COUNT: str = "COUNT("
        self.ASC: str = "ASC"
        self.DESC: str = "DESC"
        self.PRIMARY_KEY: str = "PRIMARY KEY("
        self.END: str = ") )"
        self.EQUAL_QUOTE: str = " = \""
        self.CLOSE_QUOTE: str = CommonSeps.getInstance().QUOTE
        self.EQUAL_QUOTE_NO_SPACE: str = "=\""
        self.ESCAPE: str = "\\"
        self.DOUBLE_ESCAPE: str = "\\\\"
        self.MORE_THAN_QUOTE: str = " > \""
        self.LESS_THAN_QUOTE: str = " < \""
        self.SINGLE_QUOTE_COMMA_SEP: str = "','"
        self.ID: str = "ID"
        self.SQL_STATEMENT_LABEL: str = "SQL Statement: "
        self.COLUMN_VALUE: str = "\nColumn Value: "
        self.CREATE_RETURN: str = " Created Successfully"
        self.FIELD_VALUE: str = "\nField Value: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SqlStrings:
        return SqlStrings.instance
from org.allbinary.string.CommonSeps import CommonSeps


SqlStrings.instance = SqlStrings()

