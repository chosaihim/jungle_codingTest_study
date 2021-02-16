var progresses = [95, 90, 99, 99, 80, 99];
var speeds = [1, 1, 1, 1, 1, 1];
var day = 1;


function help(progresses, speeds, answer) {
	var progress = progresses.shift();
	var speed = speeds.shift();
	var cnt = 1;	
	while ((progress + day * speed) < 100) {
		day++;
	}
	while (progresses && (progresses[0] + day * speeds[0] >= 100)) {
		progresses.shift();
		speeds.shift();
		cnt++;
	}
	answer.push(cnt);
}

function solution(progresses, speeds) {
	var answer = [];
	
	while (progresses.length) {
		help(progresses, speeds, answer);
	}
    return answer;
}

console.log(solution(progresses, speeds));