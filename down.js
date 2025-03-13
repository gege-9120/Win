const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, "public")));

// Serve the index.html on the root path "/"
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Handle file download request
app.get('/download', (req, res) => {
  const filePath = 'encrypter.exe';

  console.log(`Attempting to download file from: ${filePath}`);

  res.download(filePath, 'encrypter.exe', (err) => {
    if (err) {
      console.error(`Error downloading file: ${err.message}`);
      res.status(500).send(`Error downloading file: ${err.message}`);
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
