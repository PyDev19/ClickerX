import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0

TextField {
    font.family: "Helvetica"
    font.pixelSize: 20
    horizontalAlignment: Text.AlignRight
    verticalAlignment: Text.AlignVCenter

    onTextChanged: {
        text = text.replace(/[^0-9]/g, "");
    }
}