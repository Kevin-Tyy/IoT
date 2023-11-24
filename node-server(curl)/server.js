const http = require("http");
const fs = require("fs");
const path = require("path");
const multer = require("multer");

const PORT = 3000;
const UPLOAD_DIR = path.join(__dirname, "uploads");

// Create the uploads directory if it doesn't exist
if (!fs.existsSync(UPLOAD_DIR)) {
    fs.mkdirSync(UPLOAD_DIR);
}

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, UPLOAD_DIR);
    },
    filename: function (req, file, cb) {
        // Use the original file name for simplicity
        cb(null, file.originalname);
    },
});

const upload = multer({
    storage: storage,
    limits: {
        fileSize: 500000 * 1024 * 1024, // Set the maximum file size to 50MB (adjust as needed)
    },
    fileFilter: function (req, file, cb) {
        // Accept only video file types (you can extend this list)
        if (file.mimetype.startsWith("image/")) {
            cb(null, true);
        } else {
            cb(new Error("Invalid file type. Only images are allowed."), false);
        }
    },
});

const server = http.createServer((req, res) => {
    if (req.method === "POST" && req.url === "/upload") {
        handleVideoUpload(req, res);
    } else {
        // Serve HTML form for video upload
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Video Upload</title>
            </head>
            <body>
                <form action="/upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="file" accept="video/*" />
                    <input type="submit" value="Upload" />
                </form>
            </body>
            </html>
        `);
    }
});

function handleVideoUpload(req, res) {
    // Use multer to handle video upload
    upload.single("file")(req, res, (err) => {
        if (err) {
            console.error("Error processing video upload:", err.message);
            res.writeHead(500, { "Content-Type": "text/plain" });
            res.end("Internal Server Error");
        } else {
            res.writeHead(200, { "Content-Type": "text/plain" });
            res.end("Video uploaded successfully!");
        }
    });
}

server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
