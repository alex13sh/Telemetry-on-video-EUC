import QtQuick 2.0
//import QtMultimedia
import Dash 1.0

Rectangle {
    id: root
    width: 200
    height: 100
    color: "red"
//     property int speed: 10
    Dash {id: dash}

    Text {
        anchors.centerIn: parent
        text: "Speed: " + dash.speed
    }

    Timer {
        //interval: 1000/20; repeat: true; running: true
        property int i: 0
        onTriggered: {
           performScreenShot(root, "./test video/"+i+".png",
               function() {
                   i += 1;
               })
        }
    }

    function performScreenShot(item, name, callback) {
        if(typeof(item) === "undefined") {
            return;
        }
        else if(typeof(name) !== "string") {
            name = "screenshot.png"
        }

        item.grabToImage(function(result) {
            result.saveToFile(name);
            callback();
        });
    }
}
