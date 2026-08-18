const https = require('https');

const options = {
    hostname: 'api.github.com',
    path: '/repos/crskycode/GARbro/git/trees/master?recursive=1',
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
};

console.log("Fetching repository tree...");
https.get(options, (res) => {
    let data = [];
    res.on('data', (chunk) => {
        data.push(chunk);
    });
    res.on('end', () => {
        const json = JSON.parse(Buffer.concat(data).toString('utf8'));
        if (!json.tree) {
            console.error("Error fetching tree:", json);
            return;
        }
        
        console.log("Total files in repository:", json.tree.length);
        const interestingFiles = json.tree.filter(f => {
            const path = f.path.toLowerCase();
            return path.includes("kirikiri") || path.includes("xp3") || path.endsWith(".dat") || path.endsWith(".cs") || path.includes("maitetsu");
        });
        
        console.log("Interesting files:");
        interestingFiles.forEach(f => {
            console.log(`  ${f.path}`);
        });
    });
}).on('error', (err) => {
    console.error("Error: " + err.message);
});
