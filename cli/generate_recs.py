import json, sys
from PackVote.pipelines.generate_and_persist import run

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m packvote.cli.generate_recs <GROUP_ID>")
        sys.exit(1)
    gid = int(sys.argv[1])
    result = run(gid, include_amadeus=True)
    print(json.dumps(result, default=str, indent=2))

if __name__ == "__main__":
    main()
