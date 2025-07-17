#CRM PRODUCER
from confluent_kafka import Producer
import json
import time

P = Producer({'bootstrap.servers': 'localhost:9092'})

#MOCK DATA 
crm_events = [
    {"event": "lead_created", "lead_id": 101, "agent": "Mona", "timestamp": "2025-06-22T10:00:00"},
    {"event": "call_logged", "lead_id": 101, "agent": "Mona", "timestamp": "2025-06-22T12:00:00"}]

'''
###TO ENABLE API 
headers = {
    'Authorization': 'your_api_token_here',
    'Content-Type': 'json'
}

try:
    response = requests.get(
        "",
        headers=headers,
        params={'limit': 100, 'offset': 0} 
    )
    response.raise_for_status() 
    crm_events = response.json()
    
 '''

for event in crm_events:
    P.produce("crm_events", json.dumps(event).encode("utf-8"))
    P.flush()
    print('sent')
    time.sleep(2)




#ERP PRODUCER
from confluent_kafka import Producer
import json
import time

P = Producer({'bootstrap.servers': 'localhost:9092'})

#MOCK DATA 
erp_events = [
    # Property Listing Events
    {
        "event_type": "property_listing_created",
        "property_id": "RE-2025-1001",
        "address": "123 Palm Boulevard, Dubai Marina",
        "listing_price": 4500000,
        "currency": "AED",
        "agent": "Ahmed Al-Farsi",
        "timestamp": "2025-06-01T09:15:00Z",
        "sap_transaction_id": "SAP-RE-847392"
    },
    
    # Buyer Interaction Events
    {
        "event_type": "buyer_interest_registered",
        "property_id": "RE-2025-1001",
        "buyer_id": "VIP-7892",
        "buyer_name": "Li Wei Investments LLC",
        "agent": "Mona Khalid",
        "timestamp": "2025-06-10T14:30:00Z",
        "sap_transaction_id": "SAP-RE-849573"
    },
    
    # Contract Events
    {
        "event_type": "sales_contract_initiated",
        "property_id": "RE-2025-1001",
        "contract_value": 4350000,
        "status": "under_review",
        "legal_team": "Smith & Partners",
        "timestamp": "2025-06-18T11:45:00Z",
        "sap_transaction_id": "SAP-RE-850294"
    },
    
    # Payment Events
    {
        "event_type": "deposit_received",
        "property_id": "RE-2025-1001",
        "amount": 1000000,
        "payment_method": "bank_transfer",
        "transaction_ref": "UAE-RE-2025-789234",
        "timestamp": "2025-06-20T16:20:00Z",
        "sap_transaction_id": "SAP-RE-851023"
    }
]

'''
###TO ENABLE API 
headers = {
    'Authorization': 'your_api_token_here',
    'Content-Type': 'json'
}

try:
    response = requests.get(
        "",
        headers=headers,
        params={'limit': 100, 'offset': 0} 
    )
    response.raise_for_status() 
    erp_events = response.json()
    
 '''

for event in erp_events:
    P.produce("erp_events", json.dumps(event).encode("utf-8"))
    P.flush()
    print('sent')
    time.sleep(2)





#WEBSITE PRODUCER
from confluent_kafka import Producer
import json
import time

P = Producer({'bootstrap.servers': 'localhost:9092'})

#MOCK DATA 
website_events = [
    # User Account Activity
    {
        "log_id": "WEB-20250625-001",
        "event_type": "user_registration",
        "user_id": "user_4821",
        "user_type": "buyer",
        "email": "investor@example.com",
        "ip_address": "185.143.223.12",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X)",
        "timestamp": "2025-06-25T08:12:45Z"
    },
    
    # Property Views
    {
        "log_id": "WEB-20250625-002",
        "event_type": "property_view",
        "user_id": "user_4821",
        "property_id": "DXB-PALM-7890",
        "session_duration": 148,
        "saved": True,
        "device": "mobile",
        "timestamp": "2025-06-25T08:15:33Z"
    },
    
    # Search Queries
    {
        "log_id": "WEB-20250625-003",
        "event_type": "search_query",
        "user_id": "user_4821",
        "search_params": {
            "location": "Palm Jumeirah",
            "min_price": 5000000,
            "max_price": 15000000,
            "bedrooms": 4,
            "type": "villa"
        },
        "results_returned": 12,
        "timestamp": "2025-06-25T08:14:02Z"
    },
    
    # Lead Generation
    {
        "log_id": "WEB-20250625-004",
        "event_type": "contact_agent",
        "user_id": "user_4821",
        "property_id": "DXB-PALM-7890",
        "agent_assigned": "agent_114",
        "contact_method": "whatsapp",
        "message": "Is this villa available for viewing next week?",
        "timestamp": "2025-06-25T08:18:21Z"
    },
    
    # Admin System Events
    {
        "log_id": "SYS-20250625-001",
        "event_type": "property_listing_update",
        "admin_id": "admin_03",
        "property_id": "DXB-PALM-7890",
        "changes": {
            "price": {"old": 12500000, "new": 11950000},
            "status": {"old": "available", "new": "under_offer"}
        },
        "timestamp": "2025-06-25T09:30:15Z"
    }
]

'''
###TO ENABLE API 
headers = {
    'Authorization': 'your_api_token_here',
    'Content-Type': 'json'
}

try:
    response = requests.get(
        "",
        headers=headers,
        params={'limit': 100, 'offset': 0} 
    )
    response.raise_for_status() 
    website_events = response.json()
    
 '''

for event in website_events:
    P.produce("website_events", json.dumps(event).encode("utf-8"))
    P.flush()
    print('sent')
    time.sleep(2)


#APP PRODCUER 
#WEBSITE PRODUCER
from confluent_kafka import Producer
import json
import time
import datetime
from uuid import uuid4


P = Producer({'bootstrap.servers': 'localhost:9092'})

#MOCK DATA 
app_events = {
    # Property Listings (Rent & Sale)
    "properties": [
        {
            "property_id": str(uuid4()),
            "type": "apartment",
            "transaction_type": "rent",  
            "title": "Luxury 2BR Apartment - Downtown Dubai",
            "price": 120000,  
            "location": {
                "latitude": 25.2048,
                "longitude": 55.2708,
                "address": "Burj Khalifa Tower, Downtown Dubai"
            },
            "details": {
                "bedrooms": 2,
                "bathrooms": 2,
                "size_sqft": 1450,
                "amenities": ["pool", "gym", "concierge"]
            },
            "views": 47,
            "saves": 8,
            "status": "available",
            "last_updated": "2025-06-22T10:12:33Z"
        },
        {
            "property_id": str(uuid4()),
            "type": "villa",
            "transaction_type": "sale",
            "title": "Beachfront Villa - Palm Jumeirah",
            "price": 8500000,  # AED for sale
            "location": {
                "latitude": 25.1123,
                "longitude": 55.1387,
                "address": "Palm Jumeirah, Frond A"
            },
            "details": {
                "bedrooms": 5,
                "bathrooms": 6,
                "size_sqft": 7800,
                "amenities": ["private beach", "maid's room", "smart home"]
            },
            "views": 112,
            "saves": 23,
            "status": "under_offer",
            "last_updated": "2025-06-22T10:07:45Z" 
        }
    ],
    
    # User Activity Logs
    "user_activity": [
        {
            "event_id": str(uuid4()),
            "user_id": "user_7892",
            "event_type": "property_view",
            "property_id": "properties[0].property_id",
            "duration_sec": 87,
            "device_info": {
                "os": "Android 14",
                "model": "Samsung Galaxy S24",
                "screen_res": "1440x3088"
            },
            "timestamp": "2025-06-22T10:05:12Z" 
        },
        {
            "event_id": str(uuid4()),
            "user_id": "user_7892",
            "event_type": "property_saved",
            "property_id": "properties[0].property_id",
            "timestamp": "2025-06-22T09:30:00Z"
        }
    ],
    
    # Payment Transactions
    "transactions": [
        {
            "transaction_id": str(uuid4()),
            "user_id": "user_7892",
            "property_id": "properties[0].property_id",
            "type": "reservation_deposit",
            "amount": 5000,  # AED
            "payment_method": "apple_pay",
            "status": "completed",
            "receipt_url": "https://payments.realestatecorp.com/r_789234",
            "timestamp": "2025-06-21T16:45:00Z" 
        }
    ],
    
    # User Profiles
    "users": [
        {
            "user_id": "user_7892",
            "name": "Ahmed Mohammed",
            "email": "ahmed.m@example.ae",
            "phone": "+971501234567",
            "preferences": {
                "locations": ["Downtown Dubai", "Palm Jumeirah"],
                "min_bedrooms": 2,
                "budget_rent": {"min": 80000, "max": 150000},
                "budget_buy": {"min": 3000000, "max": 10000000}
            },
            "account_status": "verified",
            "registration_date": "2025-01-15T11:20:34Z"
        }
    ]
}
 

'''
###TO ENABLE API 
headers = {
    'Authorization': 'your_api_token_here',
    'Content-Type': 'json'
}

try:
    response = requests.get(
        "",
        headers=headers,
        params={'limit': 100, 'offset': 0} 
    )
    response.raise_for_status() 
    website_events = response.json()
    
 '''

for event_type, event_list in app_events.items():
    for event in event_list:
        P.produce("app_events", json.dumps({
            "event_type": event_type,
            "data": event,
            "timestamp": event.get("timestamp") or datetime.datetime.utcnow().isoformat()
        }).encode("utf-8"))
        P.flush()
        print(f'sent {event_type}')
        time.sleep(1)