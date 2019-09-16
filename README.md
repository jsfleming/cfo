# cfo 
*C*TF *F*older *O*rganizer. Used to help quickly generate folder structures
for challenges while participating in a CTF.

## Motivation
Often during CTFs, it can be hard to keep track of files downloaded throughout
the event, and even saving them to work on writeups afterwards. I created this
script to help me automate the setup for these directories to create a neat
working environment. The structure of these directories is as follows:

```
ctf/ - a root directory that holds all CTF folders
|- csaw-quals-2019/ - an example CTF
   |- pwn/ - example category
   |- reversing/ - example category
      |- beleaf/ - example challenge
         |- original/ - clean copy of the original file(s) distributed
	    |- ...
	 |- working/ - dirty copy of the distributed file(s) and associated scripts/file
	    |- ...
	 |- submit/ - final copies of solution scripts/files as well as eventual writeups
|- umdctf-2019/ - another example CTF
   |- ...
```

I structured my environment like this with inspiration from coursework that I've
worked on during my university, and liked it a lot for organizing original
copies, works in progress, and final submissions. This is the default organizational
schema, but feel free to fork this project and adopt a custom schema that works for
you. Custom schemas may be worked in if I end up re-writing this script.

## Setup

### Requirements
`cfo` is written in Python3, and requires [`click`](https://palletsprojects.com/p/click/).

### Installation
`cfo` can quickly be installed via [`setuptools`](https://setuptools.readthedocs.io/en/latest/).

To install:

```
git clone https://github.com/jsfleming/cfo
cd cfo
python3 setup.py install
```

`cfo` will then be accessible from the terminal.

## Usage
```
Usage: cfo [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add   Adds a challenge to the current working CTF folder.
  init  Initializes cfo with root directory for CTF folders.
  new   Instantiate a new CTF folder structure
  set   Sets given CTF as the current working CTF folder.
```

## Examples

To initialize the root directory for all CTF folders:
```
cfo init ~/ctf
```

To add a new CTF and set up preliminary folders (reversing, web, forensics):
```
cfo new csaw-quals-2019 -rwf
```

To add a new CTF with less common challenge categories:
```
cfo new umdctf-2019 -o steganography -o blast-from-the-past
```

To set a given CTF as the current working CTF:
```
cfo set umdctf-2019
```
This can be done by passing the `-x` flag to the `new` command. This will also
create an alias `cfod` that switches directories to the current working CTF
folder by adding `source ~/.config/cfo/cfod-alias` to your `.bashrc` file.

To add challenges to the current working CTF:
```
cfo add r babys-first-re ~/Downloads/706a2299cc3df42580ac990a1bfca583
```
This will add a folder for `babys-first-re` to the `reversing` folder of the
current CTF, as well as move our downloaded binary to that folder. You can
also pass in multiple files or directories to be moved over.
