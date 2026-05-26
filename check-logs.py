#!/usr/bin/env python3
import subprocess
import json

# Get the latest workflow runs
result = subprocess.run(
    ["curl", "-s", "-H", "Authorization: Bearer *** 'https://api.github.com/repos/Aivan-bot/xalt_web/actions/runs?per_page=3"],
    capture_output=True, text=True
)

if result.returncode == 0 and result.stdout:
    runs = json.loads(result.stdout).get("workflow_runs", [])
    if runs:
        latest = runs[0]
        print(f"Latest run: #{latest['id']} - {latest['status']} ({latest['conclusion']})")
        
        # Now get the logs for that run
        logs_result = subprocess.run(
            ["curl", "-s", "-H", f"Authorization: Bearer *** https://api.github.com/repos/Aivan-bot/xalt_web/actions/runs/{latest['id']}/logs"],
            capture_output=True, text=True
        )
        
        if logs_result.stdout:
            print("\n=== LAST 40 LINES OF BUILD LOG ===")
            for line in logs_result.stdout.strip().split('\n')[-40:]:
                print(line)
        
        if logs_result.stderr:
            print(f"\n=== STDERR ===")
            print(logs_result.stderr[-2000:])
    else:
        print("No workflow runs found")
else:
    print("Error fetching runs:", result.stderr[-500:] if result.stderr else "unknown error")
