# File Extractor

## Installation
Perform the following steps
- Run the following on the terminal 
			
		git clone git@github.com:ShaderOX/file-extractor.git
- Run `file_extractor.py` and using the `Python3` interpreter.

## Usage
To run it use the following command
		
	python file_extractor.py <dir>
	
**dir*** is going to be your search directory

## Brief

### Working
This software does the following
- Given the path, goes through all the available directories in that path
- If it finds a file then it copies it back to the path provided else if it finds another directory then calls itself recursively till it finds a dead end.

### Technologies
It uses `Python3` and can be used with any major operating system

