const https = require('https');
const fs = require('fs');

const url = "https://raw.githubusercontent.com/crskycode/GARbro/master/SchemeTool/Program.cs";
const path = "tools/SchemeTool_Program.cs";

console.log("Fetching " + url + "...");
https.get(url, (res) => {
    let data = [];
    res.on('data', (chunk) => {
        data.push(chunk);
    });
    res.on('end', () => {
        const buffer = Buffer.concat(data);
        fs.writeFileSync(path, buffer);
        console.log("Saved successfully! Size: " + buffer.length + " bytes");
        const lines = buffer.toString('utf8').split('\n');
        console.log("Total lines: " + lines.length);
    });
}).on('error', (err) => {
    console.error("Error: " + err.message);
});
