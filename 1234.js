let canvas = document.getElementById("canvas");
console.log(canvas);
let ctx = canvas.getContext("2d");
let img = new Image(300, 150);
img.onload = drawImageActualSize;
img.src = "Cat.jpg";
function drawImageActualSize() {
    canvas.width = this.naturalWidth;
    canvas.height = this.naturalHeight;
    ctx.drawImage(img, 0, 0);
}
canvas.addEventListener("click", function(event){
    console.log(event);
    ctx.beginPath();
    ctx.ellipse(event.clientX - 6, event.clientY - 5, 10, 10, 0, 0, 2*Math.PI);
    ctx.fillStyle = "blue";
    ctx.fill();
});


