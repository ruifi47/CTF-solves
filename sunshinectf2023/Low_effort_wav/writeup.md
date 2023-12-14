## 1 - .wav has PNG file signature
```zsh
% xxd low_effort.wav | head -n 1
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

## 2 - change extension to .png - we have a cropped image vulnerable to CVE 2023-21036 (aCropalypse)
```zsh
% cp low_effort.wav low_effort.png
```

## 3 - get pixel model number used
```zsh
% exiftool low_effort.png
...
Unique Camera Model             : Google Pixel 7
...
```

## 4 - go to https://acropalypse.app/ select Device: Pixel 7 and upload the image to get the hidden part that contains the flag (flag.png)
`sun{well_that_was_low_effort}`
