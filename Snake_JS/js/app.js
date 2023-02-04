const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

// screen 608x608
const ground = new Image();
ground.src = "img/green_squares.webp";

const foodImg = new Image();

let rand_food = Math.round(Math.random() * 4)
images = new Array();
images[0]="img/1.png"
images[1]="img/2.png"
images[2]="img/3.png"
images[3]="img/4.png"
images[4]="img/5.png"

foodImg.src = images[rand_food];


let box = 32;
let score = 0;
let food = {
	x: Math.floor((Math.random() * 17 + 1)) * box,
	y: Math.floor((Math.random() * 14 + 2)) * box,
};

let snake = [];
snake[0] = {
	x: 9 * box,
	y: 9 * box
};

document.addEventListener("keydown", direction);

let dir;

function direction(event) {
	if(event.keyCode == 37 && dir != "right")
		dir = "left";
	else if(event.keyCode == 38 && dir != "down")
		dir = "up";
	else if(event.keyCode == 39 && dir != "left")
		dir = "right";
	else if(event.keyCode == 40 && dir != "up")
		dir = "down";
}

function eatTail(head, body) {
	for(let i = 0; i < body.length; i++) {
		if(head.x == body[i].x && head.y == body[i].y)
			clearInterval(game);
	}
}
/*var ctx = c.getContext("2d");
ctx.moveTo(0, 0);
ctx.lineTo(200, 100);
ctx.stroke();*/
function drawGame() {
	ctx.drawImage(ground, 0, 0);
	ctx.moveTo(0,65);
	ctx.lineTo(608, 65);
	ctx.stroke();
	ctx.drawImage(foodImg, food.x, food.y);
	for(let i = 0; i < snake.length; i++) {
		ctx.fillStyle = i == 0 ? "navy" : "blue";
		ctx.fillRect(snake[i].x, snake[i].y, box, box);
	}
	ctx.fillStyle = "white";
	ctx.font = "50px Arial";
	ctx.fillText(score, box * 2.5, box * 1.7);

	let snakeX = snake[0].x;
	let snakeY = snake[0].y;

	// if snake eat food - score +1
	if(snakeX == food.x && snakeY == food.y) {
		score++;
		food = {
			x: Math.floor((Math.random() * 17 + 1)) * box,
			y: Math.floor((Math.random() * 14 + 2)) * box,
		};
	} else {
		snake.pop();
	}

	// board frame
	if(snakeX < box || snakeX > box * 17 || snakeY < 2 * box || snakeY > box * 18)
		clearInterval(game);

	if(dir == "left") snakeX -= box;
	if(dir == "right") snakeX += box;
	if(dir == "up") snakeY -= box;
	if(dir == "down") snakeY += box;

	let new_head = {
		x: snakeX,
		y: snakeY
	};

	eatTail(new_head, snake);
	snake.unshift(new_head);
}
let game = setInterval(drawGame, 150);