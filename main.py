import json
from ui_validate_event import ui_validate_event

def main():
    # You can make this dynamic, e.g., from workflow input or environment variable
    event_name = "Hybrid Automation Test Event"

    # Run UI validation
    ui_validate_event(event_name)

    # Generate artifact for CI reporting
    artifact_data = {
        "event": event_name,
        "status": "completed"
    }

    # Save artifact
    with open("last_event.json", "w") as f:
        json.dump(artifact_data, f)

    print("✅ Artifact last_event.json created successfully.")

if __name__ == "__main__":
    main()
