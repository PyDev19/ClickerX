cmake_minimum_required(VERSION 3.16)

project(ClickerX VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    message(STATUS "Configuring for Debug mode")
    add_compile_definitions(DEBUG)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
    message(STATUS "Configuring for Release mode")
    add_compile_definitions(NDEBUG)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
endif()

if(WIN32)
    set(CMAKE_PREFIX_PATH "C:/Qt/6.8.3/msvc2022_64")
endif()

set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Core Gui Qml Quick)
qt_standard_project_setup()

qt_add_executable(ClickerX
    src/main.cpp
    resources.qrc
)

target_link_libraries(ClickerX PRIVATE Qt6::Core Qt6::Gui Qt6::Qml Qt6::Quick)
target_include_directories(ClickerX PRIVATE include)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_definitions(ClickerX PRIVATE DEBUG_MODE)
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_definitions(ClickerX PRIVATE RELEASE_MODE)
endif()