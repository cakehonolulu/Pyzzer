# Pyzzer

<div align="center">
  <img src="pyzzerlogo.png" alt="Pyzzer" width="150" height="150">
  <h2>A simple yet effective Python 3 binary fuzzer</h2>
</div>
  
## Features

### String fuzzing:

```bash
User specified string length and format, completely random and generated at runtime

Format follows a 3 letter rule:

a = All Alphabetic ASCII (Lower and Upper case) characters
d = All digits (0-9)
p = All ASCII symbols

The default (Pressing ENTER) option uses all three modifiers.ç

To construct a 32 character length with digits and symbols it'd look like this:

 $ ./pyzzer.py program string
...
Fuzzing method: string
Input the string size:
32
Specify which string options you want (Press ENTER for default options):
ad
Random generated string: NOYpEAYLcFsr7PeudkzT9o9W0xsMbIXg
...
```

### Integer fuzzing

To be documented

## Requirements

* Python 3
* pip3
* pip3 modules (pip install -r modules.txt)
