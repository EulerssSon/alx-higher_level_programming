#!/usr/bin/node
const fs = require('fs');
const [,, file1, file2, outputFile] = process.argv;

function concatenateFiles (file1Path, file2Path, outputPath) {
  fs.readFile(file1Path, 'utf8', (err, data1) => {
    if (err) {
      return;
    }
    fs.readFile(file2Path, 'utf8', (err, data2) => {
      if (err) {
        return;
      }
      const combinedContent = data1 + data2;
      fs.writeFile(outputPath, combinedContent, (err) => {
        if (err) {
          throw err;
        }
      });
    });
  });
}
concatenateFiles(file1, file2, outputFile);
