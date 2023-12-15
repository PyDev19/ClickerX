import QtQuick 6.0
import QtQuick.Controls.Material 6.0

TextField {
    font.family: "Helvetica"
    font.pixelSize: 15
    horizontalAlignment: Text.AlignRight
    verticalAlignment: Text.AlignVCenter
    topPadding: 0
    bottomPadding: 0

    onTextChanged: {
        text = text.replace(/[^0-9]/g, "");
    }
}