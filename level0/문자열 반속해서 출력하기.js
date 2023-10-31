const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
    rl.close();
}).on('close', function () {
    str = input[0];
    n = Number(input[1]);
    str1 = '';
    for(i = 1; i <= n; i++){
        str1 += str
    }
    console.log(str1);
    process.exit();
});