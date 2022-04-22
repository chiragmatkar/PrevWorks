// TODO: Account for floor plans
// TODO: account for walls
// TODO: account for ventilation
// CDC has statistics that you can use

function make2DArray(cols, rows) {
    let arr = new Array(cols);
    for(let i = 0; i < arr.length; i++) {
        arr[i] = new Array(rows);
    }
    return arr;
}

let grid;
let nextGrid;
let posGrid;
let cols;
let rows;
let res = 25;
let day;
let infected_count;
let unvaxxed_count;
let vaxxed_count;
let run_flag;
let draw_mode;

function setup() {

    let canv = createCanvas(500, 500);
    canv.parent("canvas-container");
    canv.elt.style.border = "2px solid black";

    frameRate(1);

    cols = 500 / res;
    rows = 500 / res;

    draw_mode = 0;

    initSimulation();
    
    noLoop();
}

function initSimulation() {

    run_flag = 0;

    day = 0;
    document.querySelector("#day-count").innerHTML = day;
    // set the intial values of everything too 0
    grid = make2DArray(cols, rows); 
    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            grid[i][j] = 0;
        }
    }
    nextGrid = make2DArray(cols, rows); 
    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            nextGrid[i][j] = 0;
        }
    }

    let population = document.querySelector("#population").value;
    if(population > 400) {
        population = 400;
    }
    else if(population < 0) {
        population = 0;
    }

    let percentVaxxed = document.querySelector("#per-vaxxed").value;
    if(percentVaxxed > 100) {
        percentVaxxed = 100;
    }
    else if(percentVaxxed < 0) {
        percentVaxxed = 0;
    }

    let infected = document.querySelector("#init-infected").value;
    if(infected > 400) {
        infected = 400;
    }
    else if(infected < 0) {
        infected = 0;
    }

    infected_count = infected;
    document.querySelector("#infected-count").innerHTML = infected_count;



    let vaxxedPop = Math.round(population * (percentVaxxed/100.0));
    let genPop = population - vaxxedPop;
    
    for(let i = 0; i < genPop; i++) {
        while(true) {
            let x = Math.floor(Math.random()*cols);
            let y = Math.floor(Math.random()*rows);
            if(grid[x][y] == 0) {
                grid[x][y] = 1;
                break;
            }
        }
    }

    for(let i = 0; i < vaxxedPop; i++) {
        while(true) {
            let x = Math.floor(Math.random()*cols);
            let y = Math.floor(Math.random()*rows);
            if(grid[x][y] == 0) {
                grid[x][y] = 3;
                break;
            }
        }
    }

    for(let i = 0; i < infected; i++) {
        while(true) {
            let x = Math.floor(Math.random()*cols);
            let y = Math.floor(Math.random()*rows);
            if(grid[x][y] == 1 || grid[x][y] == 3) {
                grid[x][y] = 2;
                break;
            }
        }
    }

}

function draw() {
    
    // render current day
    document.querySelector("#day-count").innerHTML = day;
    if(run_flag) {
        day++;
    }
    infected_count = 0;
    unvaxxed_count = 0; 
    vaxxed_count = 0;

    background(255);
    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            let x = (i * res)+(res/2);
            let y = (j * res)+(res/2);
            if(grid[i][j] == 1) {
                fill('tan');
                circle(x,y,res);
                unvaxxed_count++;
            }
            else if(grid[i][j] == 2) {
                fill('lightgreen');
                circle(x,y,res);
                infected_count++;
            }
            else if(grid[i][j] == 3) {
                fill('lightblue');
                circle(x,y,res);
                vaxxed_count++;
            }
            else if(grid[i][j] == 4) {
                fill('grey');
                square(x- (res/2), y - (res/2), res);
            }
        }
    }

    document.querySelector("#infected-count").innerHTML = infected_count;
    document.querySelector("#unvaxxed-count").innerHTML = unvaxxed_count;
    document.querySelector("#vaxxed-count").innerHTML = vaxxed_count;


    
    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            if(grid[i][j] != 2 && run_flag == 1){
                infectionCheck(i,j);
            }
            else {
                nextGrid[i][j] = grid[i][j];
            }
        }
    }

    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            grid[i][j] = nextGrid[i][j];
        }
    }

    if(run_flag == 0) {
        for(let i = 0; i < cols; i++) {
            for(let j = 0; j < rows; j++) {
                let x = (i * res)+(res/2);
                let y = (j * res)+(res/2);
            
                let distance = Math.sqrt( Math.pow((x-mouseX),2) + Math.pow((y-mouseY),2) );
            
                if(distance < res/2) {
                    grid[i][j] = draw_mode;
                    //noLoop();
                    //redraw();
                    break;
                }
            
            } 
        }
    }

}

function mousePressed() {
    console.log("mouse pressed");
    run_flag = 0;
    frameRate(30);

    loop();
}

function mouseReleased() {

    console.log("mouse released");
    noLoop();

    frameRate(1);
}


function infectionCheck(x, y) {

    let infectedNeighbors = 0;

    for(let i = 0; i < 5; i++) {
        for(let j = 0; j < 5; j++) {
            
            let neighborX = x - 2 + i;
            let neighborY = y - 2 + j;

            if(neighborX < 0 || neighborX >= cols || neighborY < 0 || neighborY >= rows || (neighborX == x && neighborY == y)) {
                continue;
            }
            else if(grid[neighborX][neighborY] == 2) {
                infectedNeighbors++;
            }

        }

        if(infectedNeighbors > 0) {
            let rand = random(8);
            if((grid[x][y] == 1 && rand < 4) || (grid[x][y] == 3 && rand < 2)) {
                nextGrid[x][y] = 2;
            }
            else {
                nextGrid[x][y] = grid[x][y];
            }
        }
        else {
            nextGrid[x][y] = grid[x][y];
        }
    }

}

document.querySelector("#run-btn").onclick = function() {
    run_flag = 1;
    loop();
}

document.querySelector("#stop-btn").onclick = function() {
    run_flag = 0;
    noLoop();
}

document.querySelector("#reset-btn").onclick = function() {
    loop();
    initSimulation();
    noLoop();
}

document.querySelector("#reset-btn").onclick = function() {
    loop();
    initSimulation();
    noLoop();
}

document.querySelector("#wall-btn").onclick = function() {
    draw_mode = 4;
}
document.querySelector("#infected-btn").onclick = function() {
    draw_mode = 2;
}
document.querySelector("#unvaxxed-btn").onclick = function() {
    draw_mode = 1;
}
document.querySelector("#vaxxed-btn").onclick = function() {
    draw_mode = 3;
}
document.querySelector("#erase-btn").onclick = function() {
    draw_mode = 0;
}
