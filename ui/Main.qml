import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

import "components"

ApplicationWindow {
    id: window
    visible: true

    width: 640
    height: 480

    title: "My Application"

    Material.theme: Material.Dark
    Material.accent: Material.Purple

    property string key_pressed: "Waiting for keypress..."

    flags: Qt.Window | Qt.FramelessWindowHint

    Rectangle {
        id: title_bar
        height: 50
        color: "#222024"
        
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top

        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0

        MouseArea {
            anchors.fill: parent

            property variant click_pos: "1,1"

            onPressed: {
                click_pos  = Qt.point(mouseX, mouseY)
            }

            onPositionChanged: {
                window.x = cursor_handler.cursor_position().x - click_pos.x
                window.y = cursor_handler.cursor_position().y - click_pos.y
            }
        }


        Rectangle {
            id: title_bar_icon
            width: 50
            height: 50
            color: "#00000000"
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            clip: true
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0

            PropertyAnimation {
                id: title_bar_icon_animation
                target: title_bar_icon

                property: "width"
                to: if (title_bar_icon.width == 50) return 300; else return 50;

                duration: 500
                easing.type: Easing.InOutQuint
            }

            Image {
                id: image
                x: 5
                y: 5
                width: 42
                height: 42
                source: "qrc:/icons/icon_32x32.png"
                fillMode: Image.PreserveAspectFit
            }

            Label {
                id: label
                width: 300
                color: "#ffffff"
                text: qsTr("ClickerX")

                anchors.left: image.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 0
                anchors.bottomMargin: 0
                anchors.rightMargin: 5
                anchors.leftMargin: 5

                verticalAlignment: Text.AlignVCenter
                font.pointSize: 25
            }
        }

        RowLayout {
            spacing: 10
            layoutDirection: Qt.RightToLeft
            anchors.right: parent.right
            anchors.rightMargin: 10
            anchors.verticalCenter: parent.verticalCenter

            TitleBarButton {
                id: close_button
                icon_source: "qrc:/icons/close.png"
                onClicked: window.close()
            }

            TitleBarButton {
                id: minimize_button
                icon_source: "qrc:/icons/minimize.png"

                onClicked: {
                    window.showMinimized()
                }
            }

            TitleBarButton {
                id: setting_button
                icon_source: "qrc:/icons/settings.png"
            }
        }

        Label {
            id: title

            text: qsTr("ClickerX - A simple auto clicker")

            anchors.verticalCenter: parent.verticalCenter
            anchors.left: title_bar_icon.right
            anchors.leftMargin: 15

            verticalAlignment: Text.AlignVCenter
            font.pointSize: 15
        }
    }

    // Connections {
    //     target: key_listener
        
    //     function onKey_pressed(key) {
    //         window.key_pressed = "Key Pressed: " + key;
    //     }
    // }

    // Rectangle {
    //     anchors.fill: parent
    //     color: Material.background

    //     ColumnLayout {
    //         anchors.centerIn: parent
    //         spacing: 10

    //         Text {
    //             text: window.key_pressed
    //             font.pixelSize: 24
    //             color: "white"
    //         }
    //     }
    // }
}
