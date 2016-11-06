#!/bin/bash

python -m py_compile $1 > /dev/null 2>&1
echo $?

#
