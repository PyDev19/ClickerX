import QtQuick 6.0
import QtQuick.Controls 6.0
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
        id: main

        color: "transparent"
        anchors.fill: parent

        GroupBox {
            id: click_interval
            title: qsTr("Click Delay")

            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 10

            RowLayout {
                NumberField {
                    id: hours

                    placeholderText: "Hours"
                }

                NumberField {
                    id: minutes

                    placeholderText: "Minutes"
                }

                NumberField {
                    id: seconds

                    placeholderText: "Seconds"
                }

                NumberField {
                    id: milliseconds

                    placeholderText: "Milli Seconds"
                }
            }
        }
    }
}
