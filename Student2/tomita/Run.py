import os 
myCmd = 'python3 db_export.py'
os.system (myCmd)
myCmd = './tomita-parser config.proto' 
os.system (myCmd)
myCmd = 'python3 parse.py'
os.system (myCmd)
myCmd = 'python3 db_import.py'
os.system (myCmd)
