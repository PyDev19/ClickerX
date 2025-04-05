import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

RoundButton {
    property url icon_source: "qrc:/menu_icons/menu_icons/close.png"
    property var anchor_right: parent.right

    radius: 10

    // anchors.verticalCenter: parent.verticalCenter
    // anchors.right: anchor_right
    // anchors.rightMargin: 10

    flat: true

    Image {
        source: parent.icon_source

        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
