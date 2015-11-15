from __future__ import print_function
# -*- coding: utf-8 -*-

__version__ = "0.0.1@alpha"

import sys
import sqlite3
import argparse

def main():
  check_create_todo_table()
  parser = argparse.ArgumentParser(description='Todo.py')
  parser.add_argument('-n','--new', help='new todo item', required=False)
  parser.add_argument('-d','--delete', help='delete a todo item with id', required=False)
  
  args = vars(parser.parse_args())
  if args['new'] != None:
    print (bcolors.BLUE+"adding new todo"+bcolors.ENDC)
    new_item(args["new"])
  elif args['delete'] != None:
    print (bcolors.WARNING+"deleting a todo item"+bcolors.ENDC)
    delete_item(args["delete"])
  else:
    print (bcolors.GREEN+"YOUR TODO LIST"+ bcolors.ENDC)
    list_items()

def new_item(todostr):
  conn = connect_todo_db()
  conn.execute("INSERT INTO TODOPY (TITLE) \
      VALUES ('"+todostr+"')");
  conn.commit()
  conn.close()

def delete_item(todo_id):
  conn = connect_todo_db()
  conn.execute("DELETE FROM TODOPY WHERE ID = "+todo_id+"");
  conn.commit()
  conn.close()

def list_items():
  conn = connect_todo_db()
  cursor = conn.execute("SELECT ID,TITLE FROM TODOPY")
  for row in cursor:
   print (bcolors.BLUE,"#",bcolors.ENDC,row[0],"\t",row[1])
  cursor.close()
  conn.close()

def check_create_todo_table():
  conn = connect_todo_db()
  conn.execute('''CREATE TABLE IF NOT EXISTS TODOPY
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    TITLE           TEXT    NOT NULL);''')
  conn.close()

def connect_todo_db():
  return sqlite3.connect('todo.db')

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
