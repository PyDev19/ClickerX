import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "My Application"

    Rectangle {
        anchors.fill: parent
        color: "lightgray"

        Button {
            text: "Click Me"
            anchors.centerIn: parent
            onClicked: {
                console.log("Button clicked!");
            }
        }
    }
}
