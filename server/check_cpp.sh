#!/bin/bash

g++ $1 -w > /dev/null 2>&1
echo $?
