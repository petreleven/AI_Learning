class DrawingCanvas{
    constructor(canvas){
        this.canvas = canvas;
        this.mode = this.canvas.getContext("2d");// we want to use the 2d option
        this.isdrawing = false;
        this.height = this.canvas.height;
        this.width = this.canvas.width;
        this.onmousedown = this.onmousedown.bind(this);
        this.onmouseup = this.onmouseup.bind(this);
        this.onmousedrag = this.onmousedrag.bind(this);
        this.onmouseleave = this.onmouseleave.bind(this);
        this.canvas.addEventListener("mousedown", this.onmousedown);
        this.canvas.addEventListener("mouseup", this.onmouseup);
        this.canvas.addEventListener("mousemove", this.onmousedrag);
        this.canvas.addEventListener("mouseleave", this.onmouseleave);
        this.mode.fillStyle = "black";
        this.mode.fillRect(0, 0, this.width, this.height);
    }

    onmousedown(message) {
        // todo start drawing on the canvas
        this.isdrawing = true;
        let mousePos = [message.clientX, message.clientY] // get the mouse position(X,Y)
        allPositions.push(this.calcRelativePos(mousePos))
    }

    onmouseup() {
        // todo stop drawing on the canvas
        this.isdrawing = false;
    }

    onmousedrag(message) {
        // todo - remember the user's mouse/finger position
        // only draw if we clicked
        if(this.isdrawing == true) {
            let mousePos = [message.clientX, message.clientY] // get the mouse position(X,Y)
            allPositions.push(this.calcRelativePos(mousePos))
            this.draw()
        }
    }

    onmouseleave() {
        // stop drawing
        this.isdrawing = false;
    }

    draw() {
        this.mode.strokeStyle = "white";
        this.mode.lineWidth = 5;
        for(let index = 0; index < allPositions.length-1; index++) {
            let startPos = allPositions[index];
            let endPos = allPositions[index+1];
            this.mode.beginPath();
            this.mode.moveTo(startPos[0], startPos[1]);
            this.mode.lineTo(endPos[0], endPos[1]);
            this.mode.stroke();
        }
    }

    calcRelativePos(mousePos) {
        let rect = this.canvas.getBoundingClientRect();
        let x = mousePos[0] - rect.left;
        let y = mousePos[1] - rect.top;
        return [x, y];
    }

}

let allPositions = []

let canvas = document.getElementById("drawingCanvas");
let dm = new DrawingCanvas(canvas);

let predButton = document.getElementById("predictionButton");
predButton.addEventListener("click", sendData);



function sendData() {
    console.log("***")
    console.log(allPositions)
    fetch("/mnist_playground", {
        method : "POST",
        body : JSON.stringify(allPositions),
        headers : {"Content-type":"application/json; charset=UTF-8"}
    }).then((response) => response.json())
} 

function mousedown(message){
    console.log("clicked");
    console.log(message);
}
function mouseup(message){
    console.log("Mouse released");
    console.log(message);
}
// eventlisteners - its like an ear to listen to what the user does
canvas.addEventListener("mousedown", mousedown);
canvas.addEventListener("mouseup", mouseup);
