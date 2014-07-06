# -*- coding: utf-8 -*-

__version__ = "0.0.1@alpha"


import sys
import sqlite3


def main():
  print("Executing todocli version %s." % __version__)
  print("List of argument strings: %s" % sys.argv[1:])


def create_todo_db():
  conn = sqlite3.connect('todo.db')
  print "Created todo.db on home dir.";
  conn.execute('''CREATE TABLE TODOPY
  (ID INT PRIMARY KEY     NOT NULL,
  TITLE           TEXT    NOT NULL,
  DEADLINE        INT     NOT NULL,
  PRIORITY        INT     NOT NULL);''')
