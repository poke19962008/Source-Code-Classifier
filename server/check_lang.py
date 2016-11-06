import subprocess
import os
import sys


def check_py(filename):
    print subprocess.check_output(["check_py.sh", str(filename)])
    return subprocess.check_output(["check_py.sh", str(filename)])

def check_rb(filename):
    print subprocess.check_output(["check_rb.sh", str(filename)])
    return subprocess.check_output(["check_rb.sh", str(filename)])

def check_j(filename):
    original = str(filename)
    filename = str(filename)+'.java'
    os.system('mv '+original+' '+filename)
    a = subprocess.check_output(["check_j.sh", str(filename)])
    os.system('mv '+filename+' '+original)
    print a
    return 1

def check_c(filename):
    original = str(filename)
    filename = str(filename)+'.c'
    os.system('mv '+original+' '+filename)

    a = subprocess.check_output(["check_c.sh", str(filename)])
    # just to set the name as it was
    os.system('mv '+filename+' '+original)
    print a
    return a


def check_cpp(filename):
    original = str(filename)
    filename = str(filename)+'.cpp'
    os.system('mv '+original+' '+filename)

    a = subprocess.check_output(["check_cpp.sh", str(filename)])
    # just to set the name as it was
    os.system('mv '+filename+' '+original)
    print a
    return a




# check_py(sys.argv[1])
# check_rb(sys.argv[1])
# check_c(sys.argv[1])
# check_cpp(sys.argv[1])
# check_j(sys.argv[1])
