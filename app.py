from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

# Eventbrite Private API Key
EVENTBRITE_API_KEY = "VR5VP5FPGLFY54LECM7P"

def fetch_eventbrite_events(organization_id):
    url = f"https://www.eventbriteapi.com/v3/organizations/{organization_id}/events/"
    headers = {"Authorization": f"Bearer {EVENTBRITE_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    return response.json()

@app.route('/get-events', methods=['GET'])
def get_events():
    organization_id = request.args.get('organization_id')
    if not organization_id:
        return jsonify({"error": "Organization ID is required"}), 400
    
    events = fetch_eventbrite_events(organization_id)
    return jsonify(events)

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=10000)
