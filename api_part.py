import time

def api_create_event():
    print("\n🔵 MOCK API RUNNING…")

    # Simulate API login
    time.sleep(1)
    token = "dummy_token_12345"
    print("✅ Mock Login Successful")

    # Simulate event creation API
    time.sleep(1)
    event_id = f"EVT_{int(time.time())}"
    print(f"✅ Mock Event Created: {event_id}")

    return event_id, token





# import requests
# import json
# from config import LOGIN_API, CREATE_EVENT_API, EVENT_LIST_API, EMAIL, PASSWORD

# def api_create_event():
#     # LOGIN
#     login_payload = {
#         "email": EMAIL,
#         "password": PASSWORD
#     }
#     login_res = requests.post(LOGIN_API, json=login_payload)

#     if login_res.status_code != 200:
#         raise Exception("Login failed!")

#     token = login_res.json().get("token")

#     headers = {"Authorization": f"Bearer {token}"}

#     # CREATE EVENT
#     event_payload = {
#         "title": "Automation Event",
#         "description": "Hybrid test event",
#         "category": "Conference"
#     }

#     create_res = requests.post(CREATE_EVENT_API, json=event_payload, headers=headers)

#     if create_res.status_code != 200:
#         raise Exception("Event creation failed!")

#     event_id = create_res.json().get("_id")

#     print("Event Created ID:", event_id)

#     return event_id, token
