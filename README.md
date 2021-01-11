# SQxxx test <br>

### Language: Python <br>
### Version compatibility: 3.7+
---  

## Important points:
- No *3rd party libs/packages* used <br>
- You can run the program as soon as you have an appropriate version of **Python** installed <br>
- I haven't used a **database** first approach, because:
	- I wanted to try this with an in-memory based **DS** approach
		- Used Heaps to maintain the ***next nearest slot available*** in the parking lot
	- I wanted to keep this program 100% 3rd party lib free (database drivers, etc)

## Installation
1. Install Python 3.7+ version
2. Use the default environment (as no deps required), or create a new virtual environment
3. Highly recommend [Pyenv](https://github.com/pyenv/pyenv) for installing, managing, and maintaining virtual envs
 - If you're using MacOS, use [this](https://github.com/pyenv/pyenv#homebrew-on-macos) link
 - If you're using Linux, use [this](https://github.com/pyenv/pyenv#basic-github-checkout) link
 - If you're using Windows, you can still use Pyenv with [this](https://github.com/pyenv-win/pyenv-win) link

## Usage
All inputs are file based. Hence, you will need to input the filename/path as input to the program.

eg: if your file is `fileA.txt`,
```sh
python main.py -i fileA.txt
```

To run the test files located in this repo, use
```sh
python main.py -i input_files/input1.txt
python main.py -i input_files/input2.txt
```

To run the tests,  use
```sh
python tests.py
```
