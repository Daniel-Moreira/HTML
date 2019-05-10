const http = require('http')
const fs = require('fs')
const { parse } = require('querystring')
const { spawn } = require('child_process');

const server = http.createServer((request, res) => {
    if (request.method === 'POST') {
        // Parse the data
        collectData(request, result => {
            // Print ok and log the data as a object
            console.log(result)
            res.end(result)
        })
    }
    else
    {
        // Read the web page and print
        fs.readFile('./pagina.html', function(err, data) {
            if(err) {
                res.statusCode = 500
                res.end(`Error getting the file: ${err}.`)
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' })
                res.end(data)
            }
        })
    }
});

function collectData(request, callback) {
    let body = ''
    
    request.on('data', chunk => body += chunk.toString())
    request.on('end', () => {
        let parsedData = parse(body)
        // callback(parsedData)
        const pythonProcess = spawn('python', ['./python/MHP.py', JSON.stringify(parsedData)])
        pythonProcess.stdout.on('data', data => callback(data.toString()))
    })
}

server.listen(3000);

console.log("listening 3000")

