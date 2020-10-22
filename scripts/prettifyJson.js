let fs = require('fs');

console.log('Step 5: Prettifying our friend, Jason...')

fs.readFile(process.argv[2], 'utf8', (err, content) => {
    if(err){
        console.error(err);
    }

    let json = JSON.parse(content);

    fs.writeFileSync(process.argv[2], JSON.stringify(json, null, 2))
})

console.log('DONE: prettifyJson.js\n')