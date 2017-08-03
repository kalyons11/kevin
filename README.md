# kevin

[![Build Status](https://travis-ci.org/kalyons11/kevin.svg?branch=master)](https://travis-ci.org/kalyons11/kevin)

Personal repository for development and experimentation.

[About](#about) | [Installation](#installation) | [Structure](#structure)

## About

I have created this repository for some personal coding development and experimentation. Feel free to use whatever code is available here for your own personal use. Do [cite properly](https://integrity.mit.edu/handbook/writing-code), though!

## Installation

1.	Clone `master`.

	```
	git clone https://github.com/kalyons11/kevin.git
	```

2. Install it.

	```
	make install
	```

3. **[Optional]** Run some tests to make sure everything is okay.

	```
	make test
	```

## Structure

- `kevin` Python package

	This is a package I am working on for several purposes. I would like to experiment with the latest Python technologies (potential those in [Python 3.6](https://www.python.org/downloads/)).
	
	This package is by no means production ready. Use at your own risk.

- `scripts` directory

	This is a set of useful bash scripts I have written that streamline my normal dev process. Feel free to add them to your path.
	
	```
	$ export PATH="$PATH:kevin/scripts"
	$ encrypt test.txt
	...
	```