const https = require('https');
const fs = require('fs');

const url = "https://raw.githubusercontent.com/crskycode/GARbro/master/ArcFormats/KiriKiri/ArcXP3.cs";
const path = "tools/ArcXP3_crskycode.cs";

console.log("Fetching " + url + "...");
https.get(url, (res) => {
    let data = [];
    res.on('data', (chunk) => {
        data.push(chunk);
    });
    res.on('end', () => {
        const buffer = Buffer.concat(data);
        fs.writeFileSync(path, buffer);
        console.log("Saved to " + path + " successfully! Size: " + buffer.length + " bytes");
        const lines = buffer.toString('utf8').split('\n');
        console.log("Total lines: " + lines.length);
    });
}).on('error', (err) => {
    console.error("Error: " + err.message);
});
