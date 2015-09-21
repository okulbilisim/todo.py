# -*- coding: utf-8 -*-

__version__ = "0.0.2@alpha"


import sys
import sqlite3
import argparse

def main():
  check_create_todo_table()
  parser = argparse.ArgumentParser(description='Todo.py')
  parser.add_argument('-n','--new', help='new todo item', required=False)
  parser.add_argument('-p','--priority', help='set priority of a new item', required=False)
  parser.add_argument('-d','--delete', help='delete a todo item with id', required=False)

  args = vars(parser.parse_args())
  if args['new'] != None:
    print bcolors.BLUE+"adding new todo"+bcolors.ENDC
    if args['priority'] != None:
        new_item(args["new"], args['priority'])
    else:
        new_item(args["new"], 0)
  elif args['delete'] != None:
    print bcolors.WARNING+"deleting a todo item"+bcolors.ENDC
    delete_item(args["delete"])
  else:
    print bcolors.GREEN+"YOUR TODO LIST"+ bcolors.ENDC
    list_items()

def new_item(todostr, priority):
  conn = connect_todo_db()
  conn.execute("INSERT INTO TODOPY (TITLE,PRIORITY) \
      VALUES ('"+todostr+"',"+priority+")");
  conn.commit()
  conn.close()

def delete_item(todo_id):
  conn = connect_todo_db()
  conn.execute("DELETE FROM TODOPY WHERE ID = "+todo_id+"");
  conn.commit()
  conn.close()

def list_items():
  conn = connect_todo_db()
  cursor = conn.execute("SELECT TITLE,PRIORITY FROM TODOPY ORDER BY PRIORITY DESC")
  for row in cursor:
   print bcolors.WARNING,"--- ",row[1],"\t:",bcolors.ENDC,row[0]
  cursor.close()
  conn.close()

def check_create_todo_table():
  conn = connect_todo_db()
  conn.execute('''CREATE TABLE IF NOT EXISTS TODOPY
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    TITLE           TEXT    NOT NULL,
    PRIORITY        TINYINT NOT NULL);''')
  conn.close()

def connect_todo_db():
  return sqlite3.connect('todo.db')

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
