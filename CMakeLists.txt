cmake_minimum_required(VERSION 3.16)

project(ClickerX VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Gui Core Qml)
qt_standard_project_setup()

qt_add_executable(ClickerX
    src/main.cpp
)

target_link_libraries(ClickerX PRIVATE Qt6::Gui Qt6::Core Qt6::Qml)

# set_target_properties(ClickerX PROPERTIES
#     WIN32_EXECUTABLE ON
# )