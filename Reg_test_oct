
#!/usr/bin/env python3

import argparse
import subprocess
import sys
import re

def check_disk(sid):
    # Validate SID: SAP SIDs are typically 3 alphanumeric characters
    if not re.fullmatch(r"[A-Za-z0-9]{3}", sid):
        print("Error: Please provide a valid 3-character SID.")
        sys.exit(1)

    print(f"Checking disk space for SAP SID: {sid}")
    print("-" * 50)

    try:
        result = subprocess.run(
            ["df", "-h"],
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)

    except FileNotFoundError:
        print("Error: df command not found.")
        sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"Error executing df command: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check Linux disk space for an SAP SID"
    )
    parser.add_argument("SID", help="SAP System ID (e.g., TS4)")

    args = parser.parse_args()
    check_disk(args.SID.upper())
