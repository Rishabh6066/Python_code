'''
File handling in Python is a crucial feature that allows 
developers to create, read, write, and manipulate files 
stored on a file system. Python provides built-in functions 
and modules for handling various file operations efficiently.

Opening a File

To work with files, Python provides the open() function. 
It has the following syntax:
open(file, mode, buffering)

- file: The name of the file you want to open.
- mode: Specifies the mode in which the file is opened. Default is 'r' (read mode).
- buffering: Optional. If set to 0, buffering is disabled; if set to 1, line 
  buffering is performed.

Common Modes:

- 'r': Read (default).
- 'w': Write (overwrites the file if it exists or creates a new one).
- 'x': Exclusive creation (fails if the file exists).
- 'a': Append (writes data to the end of the file).
- 'b': Binary mode.
- 't': Text mode (default).
- '+': Read and write.

'''
f=open('abc.txt','w')
