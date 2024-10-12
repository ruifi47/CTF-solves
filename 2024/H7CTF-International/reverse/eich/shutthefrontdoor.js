function A(D, length) {
    let key = '';
    for (let i = 0; i < length; i++) {
        key += D.charAt(i % D.length);
    }
    return key;
}

function B(F, D) {
    let key = A(D, F.length);
    let G = '';
    for (let i = 0; i < F.length; i++) {
        let charCode = F.charCodeAt(i);
        let keyCode = key.charCodeAt(i);
        let GChar = String.fromCharCode(charCode ^ keyCode);
        G += GChar;
    }
    return G;
}
const fs = require('fs');
let C = fs.readFileSync('C.txt', 'utf8');
let D = "6aef677b2c8b645384e713aece4322b045a79f48";
let E = B(C, D);
console.log("Reward: ", E); // b3BlbnlvdXJleWVzYW5kbG9va2F0dGhlbWtleXNwcm9wZXJseQ==
