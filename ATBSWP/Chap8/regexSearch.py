#! python3

# regexSearch.py - Uses Regex to search through all .txt files in a given path
# Usage:	python3 regexSearch.py <path> <regex> - Searchs the given path using regex
#			python3 regexSearch.py <regex> - Searchs the current path using regex

import os, sys, re

def dir_search(path_to_search, regex_to_search):
	# Open file and search for Regex string
	for txtFile in os.listdir(path_to_search):
		if txtFile.endswith(".txt"):
			searchFile = open(txtFile, 'r')
			searchStrs = searchFile.readlines()
			for line in searchStrs:
				searchResults = regex_to_search.search(line)
				if searchResults != None:
					print('Found:', searchResults.group(), 'in', searchFile.name, '\n')
				searchFile.close()


# If 2 inputs, validate path and get regex string
if len(sys.argv) == 3:
	searchPath = sys.argv[1]
	if os.path.exists(searchPath) and os.path.isdir(searchPath):
		os.chdir(searchPath)
		rexStr = re.compile(sys.argv[2])				
		dir_search(searchPath, rexStr)
	else:
		print('No valid path specified, please retry.')

# If 1 input, assume current path and get regex string		
elif len(sys.argv) == 2:
	searchPath = os.getcwd()
	rexStr = re.compile(sys.argv[1])				
	dir_search(searchPath, rexStr)
