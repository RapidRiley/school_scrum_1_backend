// Author: Riley Warps

const express = require('express')
const fs = require('fs')
const { ServerResponse } = require('http')

// SSL Configuration
const https = require('https')
const private_key = fs.readFileSync('cert/school_scrum_1_back_end.key', 'utf8')
const certificate = fs.readFileSync('cert/school_scrum_1_back_end.crt', 'utf8')
const credentials = {
	key:  private_key,
	cert: certificate
}

const PORT = process.env.PORT
const data_dir = "/data/"

app = express()

app.get("/", (req, res) => {
    res_text = `
        <h1>You have sucessfully connected to the NodeJS API.</h1>
        <h2>/get-manifest</h2>
        <p>Retrieves a manifest containing metadata regarding 
        the currently available data, including time of last change and batch ID's.</p>
        <h2>/get-batch:\<batch_id\></h2>
        <p>Retrieves the data of the specified batch.</p>
        <h2>/get-hash:\<batch_id\></h2>
        <p>Retrieves the hash that corresponds to the specified batch.</p>
    `;
    res.send(res_text);
})

app.get("/get-batch/:batch_id", (req, res) =>{
    fs.readFile(data_dir + req.params.batch_id + ".csv", 'utf8' , (err, data) => 
    {
        if (err) {
            res.sendStatus(404)
            return
        }
        res.send(data)
        return
    })
})

app.get("/get-hash/:batch_id", (req, res) =>{
    fs.readFile(data_dir + req.params.batch_id + ".md5", 'utf8' , (err, data) => 
    {
        if (err) {
            res.sendStatus(404)
            return
        }
        res.send(data)
        return
    })
})

app.get("/get-manifest", (req, res) => {
    fs.readFile(data_dir + "manifest.json", 'utf8' , (err, data) => 
    {
        if (err) {
            res.sendStatus(404)
            return
        }
        res.send(JSON.parse(data))
        return
    })
})


https_server = https.createServer(credentials, app)
console.log("Starting server on port " + toString(PORT))
https_server.listen(PORT);