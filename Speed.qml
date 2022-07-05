import QtQuick 2.0

Rectangle {
    id: root

    property int speed: 10

    ArcItem {
        x: - width/2
        y: 10
        strokeWidth: 5
        end: speed / 50 * 180
//        fillColor: "blue"
        strokeColor: "blue"
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
