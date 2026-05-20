# Log Parser

A simple Python log parser that reads server log files, extracts useful information, and flags suspicious activity such as 404 errors.

## Features

- Reads log files line by line
- Extracts:
  - IP addresses
  - Request methods
  - Request paths
  - Status codes
- Detects 404 errors
- Lightweight and beginner-friendly
- Easy to expand with additional detection rules

## Example Log Format

```txt
192.168.1.10 GET /index 200
10.0.0.5 GET /admin 404
172.16.0.3 POST /login 500
```

## Example Output

```txt
404 detected from 10.0.0.5
Request: GET /admin
```

## How to Run

```bash
python log_parser.py
```

## Technologies Used

- Python
- File handling
- String parsing

## Future Improvements

- Suspicious IP detection
- Failed login tracking
- Regex-based parsing
- Apache/Nginx log support
- Export flagged logs to a file
- Request frequency analysis

## Educational Purpose

This project was built for learning:

- Python file I/O
- Parsing structured text
- Basic cybersecurity monitoring
- Log analysis fundamentals
- Networking and HTTP status codes

## Disclaimer

This project is intended for educational purposes only.
