#!/bin/bash

echo -e "\033[32mStarting app building process\033[0m"
echo -e "\n"

echo -e "\033[36mCompiling py files to pyc files\033[0m"
echo -e "\n"

py -m build_app.compile

echo -e "\033[36mDone compiling py files to pyc files\033[0m"
echo -e "\n"

echo -e "\033[36mFreezing app with cx_Freeze\033[0m"
echo -e "\n"

py -m build_app.setup build

echo -e "\033[36mDone freezing app with cx_Freeze\033[0m"
echo -e "\n"

echo -e "\033[36mStarting clean up process to delete all unecessary 'api-ms-win' dll files from 'build/app' directory\033[0m"

cd build/app

# Find the files starting with "api-ms-win" and delete them
find . -name "api-ms-win*.dll" -type f -delete

echo -e "\033[36mDone clean up process to delete all unecessary 'api-ms-win' dll files from 'build/app' directory\033[0m"
echo -e "\n"

echo -e "\033[32mDone app building process, final build is located in 'build/app' directory\033[0m"
echo -e "\n"
