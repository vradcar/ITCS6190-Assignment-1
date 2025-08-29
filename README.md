# ITCS6190-Assignment-1

## What This Project Does

This project analyzes taxi trip data using Docker containers. It consists of a PostgreSQL database and a Python app that runs queries on the data and saves the results as JSON. The setup is simple and requires minimal configuration.

## Project Structure

```
├── app/                    # Python application files
│   ├── Dockerfile          # Container definition for the Python app
│   ├── main.py             # Python script that analyzes trip data
│   └── requirements.txt    # Python dependencies
├── db/                     # Database files and setup
│   ├── Dockerfile.db       # Container definition for PostgreSQL 
│   └── init.sql            # Database initialization script with sample data
├── out/                    # Output directory for results
│   └── summary.json        # Generated JSON output file
├── compose.yml             # Docker Compose configuration
├── run.sh                  # Helper script for common commands
├── LICENSE                 # Project license file
└── README.md               # This file
```

## Prerequisites

- Docker and Docker Compose

## How to Run

You can use the helper script `run.sh` for all operations:

```bash
# Start the application
./run.sh up

# Stop the application
./run.sh down

# Build just the app container
./run.sh build

# Clean up (stop containers and remove output files)
./run.sh clean

# Show help
./run.sh help
```

### Note for Windows Users

Windows users can run the script using Git Bash, WSL (Windows Subsystem for Linux), or a similar bash-compatible shell.

## Output

The application produces two outputs:

1. Summary statistics in the terminal console
2. A JSON file at `out/summary.json`

## Example Output

This is what you'll see in the console:

```
=== Summary ===
{
  "total_trips": 6,
  "avg_fare_by_city": [
    {"city": "Charlotte", "avg_fare": 16.25},
    {"city": "New York", "avg_fare": 19.0},
    {"city": "San Francisco", "avg_fare": 20.25}
  ],
  "top_by_minutes": [
    {"id": 6, "city": "San Francisco", "minutes": 28, "fare": 29.3},
    ...
  ]
}
```

The same data is saved in the `out/summary.json` file.

## Database Information

The database stores taxi trip information:
- City name
- Trip duration in minutes
- Fare amount

## Troubleshooting

If you have problems:

1. **Database connection errors**: 
   - Wait a few seconds and try again; the database might still be starting
   - Run `docker compose down -v` to reset the data and try again

2. **File output errors**:
   - Make sure the `out` directory exists
   - Check that Docker has permission to write to it

For any other issues, check the Docker logs with `docker compose logs`.