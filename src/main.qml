import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0
import "components/"

ApplicationWindow {
    visible: true
    width: 500
    height: 250
    title: "ClickerX"

    Material.theme: Material.Dark
    Material.accent: Material.Cyan

    Rectangle{
        id: main

        color: "transparent"
        anchors.fill: parent
        
        NumberField {
            id: hours

            placeholderText: "Hours"

            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 10

            height: 50
        }
    }
}