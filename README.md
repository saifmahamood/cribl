# Log Monitoring Service

A REST API service that provides access to log files in `/var/log` without logging into each server.

### Requirements
- Python 3.8+
- Flask (install with `pip install -r requirements.txt`)

### Running the Service
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python app.py`

### Usage
Use the following endpoint to retrieve logs:

**GET** `/logs`

| Query Parameter | Description |
| --------------- | ----------- |
| `filename`      | Specify the log filename (default: `syslog`) |
| `keyword`       | Filter log lines containing this keyword |
| `n`             | Number of matching log lines to retrieve (default: 10) |

Example:
```bash
curl "http://localhost:5000/logs?filename=syslog&keyword=error&n=5"
