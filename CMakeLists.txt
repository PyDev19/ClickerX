cmake_minimum_required(VERSION 3.16)

project(ClickerX VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_PREFIX_PATH "C:/Qt/6.6.1/msvc2019_64")
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Core Gui Qml Quick QuickControls2 QuickTemplates2)
qt_standard_project_setup()

qt_add_executable(ClickerX
    src/main.cpp
    src/ui.cpp
    include/ui.hpp
    resources.qrc
)

set_source_files_properties(src/main.qml PROPERTIES QT_RESOURCE_ALIAS main.qml)
set_source_files_properties(src/components/NumberField.qml PROPERTIES QT_RESOURCE_ALIAS components/NumberField.qml)

qt_add_qml_module(ClickerX
    URI qml
    RESOURCE_PREFIX /
    QML_FILES
        src/main.qml
        src/components/NumberField.qml
)

set_target_properties(ClickerX PROPERTIES QT_QMLCACHEGEN_DIRECT_CALL ON)

target_link_libraries(ClickerX PRIVATE Qt6::Core Qt6::Gui Qt6::QmlPrivate Qt6::QuickPrivate Qt6::QuickControls2Private Qt6::QuickTemplates2Private)
target_include_directories(ClickerX PRIVATE include)
# set_target_properties(ClickerX PROPERTIES
#     WIN32_EXECUTABLE ON
# )