#!/usr/bin/node
class Rectangle {constructor (width, height){
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)){
        this.width = w;
        this.height = h;
        } else {
            this.width = undefined;
            this.height = undefined;
        }
    }
    print() {
        for (let i = 0; i < this.width; i++) {
            let row = "";
            for (let j = 0; j < this.height; j++) {
                row += "x";
            }
            console.log(row)
        }
    }
    rotate(){
        [this.width,this.height] = [this.height, this.width];
        for (let i = 0; i < this.width; i++) {
            let row = "";
            for (let j = 0; j < this.height; j++) {
                row += "x";
            }
            console.log(row)
        }
    }
    double(){
        this.width *= 2;
        this.height *= 2;
        for (let i = 0; i < this.width; i++) {
            let row = "";
            for (let j = 0; j < this.height; j++) {
                row += "x";
            }
            console.log(row)
        }
    }
}

