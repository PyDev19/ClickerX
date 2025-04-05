import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow {
    id: window
    visible: true

    width: 640
    height: 480

    title: "My Application"

    Material.theme: Material.Dark
    Material.accent: Material.Purple

    property string key_pressed: "Waiting for keypress..."

    Connections {
        target: key_listener
        
        function onKey_pressed(key) {
            window.key_pressed = "Key Pressed: " + key;
        }
    }

    Rectangle {
        anchors.fill: parent
        color: Material.background

        ColumnLayout {
            anchors.centerIn: parent
            spacing: 10

            Text {
                text: window.key_pressed
                font.pixelSize: 24
                color: "white"
            }
        }
    }
}
