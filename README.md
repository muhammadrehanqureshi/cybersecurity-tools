## About Me
My name is Muhammad Rehan Qureshi, a cybersecurity professional who has completed my bachelor of cyber security (honours) and master of cyber security from Deakin university, Melbourne. I am passionate about securing digital ecosystems. Please check out my portfolio. Regards.

# cybersecurity-tools
A collection of scripts and tools for penetration testing, vulnerability management, and more

## Tools Included
- **Penetration Testing Scripts**: Automating vulnerability scans.
- **Incident Response Toolkit**: Scripts to manage security incidents.
- **Encryption Demos**: Examples of AES/RSA encryption.

## Port Scanner
**File:** `port_scanner.py`  
This script scans a range of ports on a given IP address and identifies open ports.

### Usage
1. Run the script: `python port_scanner.py`.
2. Enter the target IP address and port range when prompted.
3. View the results showing open ports.

## Password Generator
**File:** `password_generator.py`  
This script generates secure passwords based on user preferences, including length and character types.

### Features
- Specify password length.
- Include/exclude uppercase letters, numbers, and special characters.
- Ensures at least one character of each selected type is included.

### Usage
Run the script and follow the prompts:

## Log Analyzer
**File:** `log_analyzer.py`  
This script analyzes log files to identify specific patterns or events and provides a summary of findings.

### Features
- Parse log files line by line.
- Search for user-defined patterns (e.g., 'ERROR', 'WARNING').
- Report matching lines with line numbers.

### Usage
Run the script and provide:
1. Path to the log file.
2. Pattern to search for.

## Password Generator
**File:** `password_generator.py`  
This script generates secure passwords based on user-defined length and character preferences.

### Features
- Specify password length (minimum 4 characters).
- Include/exclude uppercase letters, numbers, and special characters.
- Ensures at least one character of each selected type is included.

### Usage
Run the script and follow the prompts:

### New Features
- Password strength analysis (Weak, Medium, Strong).
- Option to save passwords to a file with timestamps.

# File Integrity Checker

## Overview
The **File Integrity Checker** is a Python-based script designed to monitor and verify the integrity of files. By calculating and storing file hashes, it ensures that any unauthorized modifications or tampering are quickly identified.

This tool is ideal for maintaining file security and ensuring data consistency in sensitive environments.

## Features
- **Hash Calculation**: Uses algorithms like SHA-256 to calculate file hashes.
- **Integrity Monitoring**: Detects unauthorized changes by comparing current and saved hashes.
- **Tampering Detection**: Identifies missing, modified, or tampered files.
- **JSON Storage**: Saves file hashes in a JSON file for easy management.

## How It Works
1. **Save Hashes**: Generate and store hashes for files in a directory.
2. **Check Integrity**: Compare stored hashes with current file hashes to detect changes.

## Malware Scanner

### Overview
The **Malware Scanner** is a Python tool designed to detect potentially malicious files in a directory by comparing their hashes against known malware signatures. It provides a simple solution for malware detection and is ideal for improving cybersecurity skills.

### Features
- Recursively scans directories for files.
- Compares file hashes to known malware signatures.
- Generates a report of potentially infected files.

### How It Works
1. **Input Directory**: Prompts the user to specify the directory to scan.
2. **Hash Comparison**: Matches file hashes with known malware signatures.
3. **Generate Report**: Outputs a list of suspicious files in the console.

---

## Vulnerability Scanner

### Overview
The **Vulnerability Scanner** is a Python tool designed to identify open ports on a target machine, which can indicate potential vulnerabilities. It scans a specified range of ports and provides insights to secure exposed services.

### Features
- Scans a specified IP address for open ports.
- Allows users to define custom port ranges.
- Identifies potential entry points for attackers.

### How It Works
1. **Input Target IP**: Users provide the IP address of the target machine.
2. **Specify Port Range**: Users define the range of ports to scan.
3. **Detect Open Ports**: The script identifies ports that are open and may need further investigation.

## Phishing Email Detector

### Overview
The **Phishing Email Detector** is a Python tool designed to identify potential phishing attempts in email content by analyzing keywords, links, and suspicious patterns.

### Features
- Detects phishing keywords (e.g., "password", "urgent").
- Analyzes URLs for suspicious domains and shortened links.
- Provides a summary of red flags detected in the email.

### How It Works
1. Save the email content as a `.txt` file.
2. Run the script and provide the file path when prompted.
3. Review the analysis results for any red flags.

### Usage
```bash
python phishing_email_detector.py


### Usage

#### 1. Clone the Repository
```bash
git clone https://github.com/muhammadrehanqureshi/cybersecurity_tools.git
cd cybersecurity_tools









