const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = '';

rl.on('line', function (line) {
    input = line;
    rl.close();
}).on('close',function(){
    
    let result = [];
    for(i of input){
        if(i == i.toUpperCase()){
            result.push(i.toLowerCase());
        }else{
            result.push(i.toUpperCase());
        }
        
    }
    console.log(result.join(''));
    process.exit();
});