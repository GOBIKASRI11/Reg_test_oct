#!/usr/bin/env python3 nanthu
import sys
import subprocess
 
 
def check_disk_usage(sid):
    print("\nChecking disk usage for SID: {}".format(sid))
    print("=" * 60)
 
    try:
        result = subprocess.run(
            ["df", "-h"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=True
        )
 
        print(result.stdout)
 
    except subprocess.CalledProcessError as e:
        print("Error executing df -h:")
        print(e.stderr)
        sys.exit(1)
 
    except OSError as e:
        print("Error: {}".format(e))
        sys.exit(1)
 
 
if __name__ == "__main__":
 
    if len(sys.argv) != 2:
        print("Usage: {} <SID>".format(sys.argv[0]))
        print("Example: {} KSL".format(sys.argv[0]))
        sys.exit(1)
 
    sid = sys.argv[1].upper()
 
    check_disk_usage(sid)
