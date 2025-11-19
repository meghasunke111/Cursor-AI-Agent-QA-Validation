from api_part import api_create_event
from ui_part import ui_validate_event

if __name__ == "__main__":
    print("\n=== HYBRID AUTOMATION STARTED ===")

    # Step 1: Mock API login + event creation
    event_id, token = api_create_event()

    # Step 2: Validate event in UI
    ui_validate_event(event_id)

    print("\n=== HYBRID AUTOMATION COMPLETED ===")
