#!/bin/bash

javac $1 > /dev/null 2>&1
echo $?
