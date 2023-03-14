#!/bin/bash

# Define variables
VENV_DIR=env

# Activate virtual environment
source "./$VENV_DIR/Scripts/activate"

# Define variables
BUILD_DIR=build/app

# Define functions
function compile_py_files {
    echo -e "\033[36mCompiling py files to pyc files\033[0m"
    echo -e "\n"

    py -m build_app.compile

    echo -e "\033[36mDone compiling py files to pyc files\033[0m"
    echo -e "\n"
}

function delete_unecessary_dll {
    # Clean up process to delete all unnecessary 'api-ms-win' dll files from 'build/app' directory
    echo -e "\033[36mStarting clean up process to delete all unecessary 'api-ms-win' dll files from 'build/app' directory\033[0m"

    cd $1

    # Find the files starting with "api-ms-win" and delete them
    find . -name "api-ms-win*.dll" -type f -delete

    echo -e "\033[36mDone clean up process to delete all unecessary 'api-ms-win' dll files from 'build/app' directory\033[0m"
    echo -e "\n"
}

# Exit script if any command fails
set -e

# Start app building process
echo -e "\033[32mStarting app building process\033[0m"
echo -e "\n"

compile_py_files

# Freeze app with cx_Freeze
echo -e "\033[36mFreezing app with cx_Freeze\033[0m"
echo -e "\n"

py -m build_app.setup build

echo -e "\033[36mDone freezing app with cx_Freeze\033[0m"
echo -e "\n"

delete_unecessary_dll $BUILD_DIR

# Finish app building process
echo -e "\033[32mDone app building process, final build is located in '$BUILD_DIR' directory\033[0m"
echo -e "\n"

sleep 2
