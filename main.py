import os
import json
from ui_part import ui_validate_event

def main():
    # Get event name from environment variable (set in GitHub Actions workflow)
    event_name = os.getenv("EVENT_NAME", "Hybrid Automation Test Event")

    # Run UI automation
    ui_validate_event(event_name)

    # Generate artifact for CI reporting
    artifact_data = {
        "event": event_name,
        "status": "completed"
    }

    with open("last_event.json", "w") as f:
        json.dump(artifact_data, f)

    print("✅ Artifact last_event.json created successfully.")

if __name__ == "__main__":
    main()
