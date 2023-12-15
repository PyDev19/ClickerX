import QtQuick 6.0
import QtQuick.Layouts 6.0
import QtQuick.Controls.Material 6.0
import "components/"

ApplicationWindow {
    visible: true
    width: 550
    height: 275
    title: "ClickerX"

    Material.theme: Material.Dark
    Material.accent: Material.Cyan

    Rectangle {
        objectName: "main_rect"
        id: main

        color: "transparent"
        anchors.fill: parent

        GroupBox {
            objectName: "click_interval_box"
            id: click_interval
            title: qsTr("Click Delay")

            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 10

            RowLayout {
                objectName: "click_interval_layout"
                anchors.fill: parent
            }
        }

        GroupBox {
            id: mouse_button
            title: qsTr("Mouse Button")

            anchors.top: click_interval.bottom
            anchors.topMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 10

            ColumnLayout {
                spacing: 0
                RadioButton {
                    id: left_buton
                    text: qsTr("Left")
                }

                RadioButton {
                    id: right_button
                    text: qsTr("Right")
                }
            }
        }
    }
}
