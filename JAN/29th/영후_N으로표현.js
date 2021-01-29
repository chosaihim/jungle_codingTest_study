function calcul(n1, n2) {
	var lst = [];
	lst.push(n1+n2);
	lst.push(n1*n2);
	if (n1 >= n2) {
		if (n2 != 0) {
			lst.push(Math.floor(n1/n2));
		}
		lst.push(n1-n2);
	}
	else {
		if (n1 != 0) {
			lst.push(Math.floor(n2/n1));
		}
		lst.push(n2-n1);
	}
	lst = Array.from(new Set(lst));
	return lst
}

function bingo(i, N) {
	if (i == 0) {
		return N;
	}
	return N * Math.pow(10, i) + bingo(i - 1, N);
}

function solution(N, number) {
	var arr = new Array(8);
	if (N == number) {
		return 1;
	}
	arr[0] = [N];
	arr[1] = calcul(N, N);
	arr[1].push(N * 10 + N);

	if (arr[1].indexOf(number) != -1) {
		return 2;
	}
	else {
		var i = 2;
		while (1) {
			var tmp = []
			var j = i;
			var pl = 0;
			var pr = j - 1;
			while (1) {
				for (var a = 0 ; a < arr[pl].length ; a++) {
					for (var b = 0 ; b < arr[pr].length ; b++) {
						tmp = tmp.concat(calcul(arr[pl][a], arr[pr][b]));
					}
				}
				pl++;
				pr--;
				if (pl > pr) {
					break;
				}	
			}
			arr[i] = Array.from(new Set(tmp));
			arr[i].push(bingo(i, N));

			if (arr[i].indexOf(number) != -1) {
				return (i + 1);
			}
			if (i == 7) {
				return -1;
			}
			i++;
		}
	}
}


var N = 5;
var number = 12;

console.log(solution(N, number));


