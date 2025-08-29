# ITCS6190-Assignment-1

## What This Does

This project analyzes taxi trip data using Docker. It has a PostgreSQL database with sample trip data and a Python script that runs queries to calculate statistics. The results are displayed in your terminal and saved as a JSON file.

## Setup and Run

You need Docker installed on your computer. That's it.

To run everything:

```bash
./run.sh
```

On Windows, use Git Bash or run:
```bash
bash run.sh
```

This single command will:
- Build the containers
- Start the database 
- Run the analysis
- Show you the results
- Save results to `out/summary.json`

To stop everything, press Ctrl+C in the terminal.

## What You'll See

The script analyzes 6 taxi trips from Charlotte, New York, and San Francisco. It calculates:
- Total number of trips
- Average fare by city  
- Longest trips by duration

Results appear in your terminal and are saved to `out/summary.json`.

## Files

```
├── app/                    # Python application
├── db/                     # Database setup
├── out/                    # Results go here
├── compose.yml             # Docker configuration
├── run.sh                  # Run this to start everything
└── README.md               # This file
```

For any other issues, check the Docker logs with `docker compose logs`.