# Shell Scripting Notes

### Libraries

- https://docs.python.org/3/library/os.html
  - `os.environ`: mapping object containing string environment, e.g., os.environ["HOME"] is pathname of your home directory
  - `os.getenv(key, default=None)`: similar to above, but provide default
  - `os.chdir(path), os.getcwd()`: change directory, get working directory
  - `os.mkdir(path)`: creates directory named path
  - `os.chmod(path, mode)`: change the mode of path
  - `os.chown(path, uid, gid)`: change owner and group id of path
  - `os.getpid()`: returns the current process ID
  - `os.getppid()`: return the parent's process ID
  - `os.uname()`: returns information identifying the current operating system
  - `os.listdir(path='.')`: returns list containing names of entries in the given directory
  - `os.readlink(path)`: returns path to which the symbolic link points
  - `os.remove(path)`: delete file path
  - `os.rmdir(path)`: delete directory path
  - `os.removedirs(name)`: remove directories recursively
  - `os.rename(old, new)`: directory or file renaming function
  - `os.symlink(src, dst)`: creates symbolic link pointing from src to named dst
  - `os.sync()`: force write of everything to disk
  - `os.walk(top, topdown=True, onerror=None, followlinks=False)`: yields 3-tuple (dirpath, dirnames, filenames)
  - `os.system`: execture command (string) in a subshell, returns exit status

- https://docs.python.org/3/library/sys.html
  - `sys.argv`: list of command line arguments, argv[0] is the script name
  - `sys.exit`: exit from python
  - `sys.stdin, sys.stderr, sys.stdout`: file objects for standard input, output, and errors


### Fork in Python

- `os.fork()`: fork a child process
- `os.kill(pgid, sig)`
- `os.wait()`: wait for completion of child process
- `os.waitpid()`: wait for completion of a child process given by process id pid, return tuple containing its process id and exit status

~~~~python
import os

def child():
  print("child process {}\n".format(os.getpid()))
  os._exit(0)

def parent():
  count = 0

  while True:
    newpid = os.fork()
    # both parent and child process continue ...
    if newpid == 0: # child process will have newpid == 0
      child()
    else: # parent process will have correct newpid
      pids = (os.getpid(), newpid)
      count += 1
      if count == 10: break

parent()
~~~~

... there has to be a better way?
