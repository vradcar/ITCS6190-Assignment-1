import os, sys, time, json
import psycopg

# Environment variables with defaults
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")
TOP_N = int(os.getenv("APP_TOP_N", "10"))


def connect_with_retry(retries=5, delay=2):
    """Connect to database with retry logic"""
    for attempt in range(retries):
        try:
            conn = psycopg.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASS,
                dbname=DB_NAME,
                connect_timeout=3,
            )
            return conn
        except Exception as e:
            print(f"Database connection attempt {attempt+1}/{retries} failed, retrying...", file=sys.stderr)
            time.sleep(delay)
    
    print("Failed to connect to database after multiple attempts", file=sys.stderr)
    sys.exit(1)


def main():
    conn = connect_with_retry()
    with conn, conn.cursor() as cur:
        # Total number of trips
        cur.execute("SELECT COUNT(*) FROM trips")
        total_trips = cur.fetchone()[0]

        # Average fare by city
        cur.execute("""
            SELECT city, AVG(fare) AS avg_fare
            FROM trips
            GROUP BY city
            ORDER BY city
        """)
        by_city = [{"city": c, "avg_fare": float(a)} for (c, a) in cur.fetchall()]

        # Top N trips by minutes (longest duration trips)
        cur.execute("""
            SELECT id, city, minutes, fare
            FROM trips
            ORDER BY minutes DESC
            LIMIT %s
        """, (TOP_N,))
        top = [{"id": id, "city": city, "minutes": minutes, "fare": float(fare)} 
               for (id, city, minutes, fare) in cur.fetchall()]

        summary = {
            "total_trips": int(total_trips),
            "avg_fare_by_city": by_city,
            "top_by_minutes": top
        }

        # Write to /out/summary.json
        os.makedirs("/out", exist_ok=True)
        with open("/out/summary.json", "w") as f:
            json.dump(summary, f, indent=2)
            
        # Print to stdout
        print("=== Summary ===")
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
