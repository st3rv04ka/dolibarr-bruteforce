# Dolibarr Brute Force Tool
## Description
This repository contains a Python script designed to perform a brute force attack on a Dolibarr instance by trying various combinations of usernames and passwords. The script leverages multi-threading to speed up the process by attempting multiple login attempts in parallel.

## Usage
To run the script, you need to provide the URL of the Dolibarr instance, a file containing usernames, a file containing passwords, and the number of threads to use for parallel processing.

## Requirements
 - Python 3
 - requests library

## Installation
Clone the repository:

```sh
git clone [https://github.com/yourusername/dolibarr-bruteforce.git](https://github.com/st3rv04ka/dolibarr-bruteforce)
cd dolibarr-bruteforce
```
Install the required libraries:

```sh
pip install requests
```

## Running the Script
To execute the script, use the following command:

```sh
python3 dolibarr.py http://dolibarr.stf usernames_file passwords_file threads_count
```
 - URL: The URL of the Dolibarr instance you want to target.
 - usernames_file: Path to the file containing a list of usernames to try.
 - passwords_file: Path to the file containing a list of passwords to try.
 - threads_count: Number of threads to use for parallel processing.

## Example
```sh
python3 dolibarr.py http://dolibarr.stf usernames.txt passwords.txt 10
```
