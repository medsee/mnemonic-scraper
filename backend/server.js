const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: "*" } });

app.use(express.static("frontend"));

io.on("connection", socket => {
    console.log("Client connected");
});

server.listen(3000, () => console.log("SERVER RUNNING ON 3000"));
