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
        this.ontouchstart = this.ontouchstart.bind(this);
        this.ontouchmove = this.ontouchmove.bind(this);
        this.canvas.addEventListener("mousedown", this.onmousedown);
        this.canvas.addEventListener("mouseup", this.onmouseup);
        this.canvas.addEventListener("mousemove", this.onmousedrag);
        this.canvas.addEventListener("mouseleave", this.onmouseleave);
        this.canvas.addEventListener("touchstart", this.ontouchstart);
        this.canvas.addEventListener("touchmove", this.ontouchmove);
        this.mode.fillStyle = "black";
        this.mode.fillRect(0, 0, this.width, this.height);
    }

    ontouchstart(event) {
        event.preventDefault(); // Prevent scrolling
        this.isdrawing = true;
        let touch = event.touches[0];
        let touchposition = this.calcRelativePos([touch.clientX, touch.clientY]);
        allPositions.push([touchposition]);
    }
    
    ontouchmove(event) {
        event.preventDefault(); // Prevent scrolling
        if (this.isdrawing) {
          let touch = event.touches[0];
          let touchposition = this.calcRelativePos([touch.clientX, touch.clientY]);
          allPositions[allPositions.length - 1].push(touchposition);
          this.draw();
        }
      }

    onmousedown(message) {
        // todo start drawing on the canvas
        this.isdrawing = true;
        let mousePos = [message.clientX, message.clientY] // get the mouse position(X,Y)
        allPositions.push([this.calcRelativePos(mousePos)])
        console.log(allPositions)
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
            allPositions[allPositions.length-1].push(this.calcRelativePos(mousePos))
            console.log(allPositions)
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
        for(let lineNo = 0; lineNo < allPositions.length; lineNo++) {
            for(let index = 0; index < allPositions[lineNo].length-1; index++) {
                let startPos = allPositions[lineNo][index];
                let endPos = allPositions[lineNo][index+1];
                this.mode.beginPath();
                this.mode.moveTo(startPos[0], startPos[1]);
                this.mode.lineTo(endPos[0], endPos[1]);
                this.mode.stroke();
            }
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

let clearButton = document.getElementById("clearButton");
clearButton.addEventListener("click", clearCanvas);

function sendData() {
    console.log("***")
    console.log(allPositions)
    fetch("https://web-production-8cbdf.up.railway.app/mnist_playground", {
        method : "POST",
        body : JSON.stringify(allPositions),
        headers : {"Content-type":"application/json; charset=UTF-8"}
    }).then((response) => response.json()).then((data) => showResultAsHtml(data));
} 

function clearCanvas(){
    let clearCanvas = document.getElementById("drawingCanvas")
    clearCanvas.getContext('2d').clearRect(0, 0, 280, 280)
    allPositions = []
}

function showResultAsHtml(data) {
    const div = document.getElementById("results");
    const maxValue = Math.max(...data);
    const resultHtml = Array.from(data).map((value, index) => {
        const percentage = Math.round(value);
        const isHighest = value === maxValue;
        return `
            <div class="prediction-row d-flex flex-row align-items-center p-2 ${isHighest ? 'highlight-prediction' : ''}"
                 style="opacity: 0; transform: translateX(-20px); animation: slideIn 0.3s ease forwards ${index * 0.05}s;">
                <div class="digit-label me-3" style="min-width: 30px;">
                    <span class="fw-bold ${isHighest ? 'text-accent' : ''}">${index}</span>
                </div>
                <div class="progress flex-grow-1 me-3" style="height: 12px; background: rgba(255, 255, 255, 0.1); border-radius: 6px; overflow: hidden;">
                    <div class="progress-bar" 
                         style="width: ${percentage}%; 
                                height: 100%; 
                                background: ${isHighest ? 'linear-gradient(to right, var(--gradient-start), var(--gradient-end))' : 'rgba(255, 255, 255, 0.2)'};
                                transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);">
                    </div>
                </div>
                <div class="percentage-label" style="min-width: 60px;">
                    <span class="${isHighest ? 'fw-bold text-accent' : ''}">${percentage}%</span>
                </div>
            </div>
        `;
    }).join('');

    // Add styles
    const styles = `
        <style>
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(-20px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            .text-accent {
                color: var(--accent-color);
            }

            .prediction-row {
                transition: all 0.3s ease;
                border-radius: 8px;
                margin-bottom: 4px;
            }

            .prediction-row:hover {
                background: rgba(255, 255, 255, 0.05);
            }

            .highlight-prediction {
                background: rgba(99, 102, 241, 0.1);
            }

            .highlight-prediction:hover {
                background: rgba(99, 102, 241, 0.15);
            }

            .progress-bar {
                transform-origin: left;
                animation: growBar 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            }

            @keyframes growBar {
                from {
                    transform: scaleX(0);
                }
                to {
                    transform: scaleX(1);
                }
            }
        </style>
    `;

    div.innerHTML = styles + `
        <div class="results-container p-3">
            ${resultHtml}
        </div>
    `;

    // Update the accuracy meter in the main UI
    const accuracyFill = document.querySelector('.accuracy-fill');
    if (accuracyFill) {
        accuracyFill.style.width = `${maxValue}%`;
    }
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
