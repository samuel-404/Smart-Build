import os
import json
import httpx
from dotenv import load_dotenv

# Run setup
load_dotenv()

# We expect you've saved these into backend/.env
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://hisxrqiuytehbunhsyql.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhpc3hycWl1eXRlaGJ1bmhzeXFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzIzNzgwNjcsImV4cCI6MjA4Nzk1NDA2N30.ue87Yhg31SC8iAqL0xc5gyMo8E0xIVMUWQU3vxGJB5E")

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'seed_data.json')

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates" # Acts like upsert
}

def load_data():
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def run_upsert(table_name, payload):
    url = f"{SUPABASE_URL}/rest/v1/{table_name}"
    response = httpx.post(url, headers=headers, json=payload)
    if response.status_code not in (200, 201):
        print(f"Error inserting into {table_name}: {response.text}")
    else:
        print(f"Successfully inserted {len(payload)} rows into {table_name}!")

def seed_database():
    print("Loading local JSON data...")
    data = load_data()
    
    components_data = data.get('components', {})
    usage_profiles = data.get('usage_profiles', {})
    budget_tiers = data.get('budget_tiers', {})

    print("=========================")
    print("Preparing to seed Supabase via REST API...")
    
    # 1. Seed standard Components
    print("Seeding Components...")
    all_inserted_components = []
    
    for category, items in components_data.items():
        print(f" -> Mapping category: {category} ({len(items)} items)")
        for item in items:
            row = {
                "id": item.get('id'),
                "type": category,
                "name": item.get('name'),
                "brand": item.get('brand'),
                "price": item.get('price'),
                "performance_score": item.get('performance_score'),
                "specs": item
            }
            all_inserted_components.append(row)
            
    if all_inserted_components:
        run_upsert('components', all_inserted_components)

    # 2. Seed Usage Profiles
    print("\nSeeding Usage Profiles...")
    profiles_list = []
    for key, profile in usage_profiles.items():
        profiles_list.append({
            "id": key,
            "name": profile.get('name'),
            "min_requirements": profile.get('min_requirements', {})
        })
    if profiles_list:
        run_upsert('usage_profiles', profiles_list)

    # 3. Seed Budget Tiers
    print("\nSeeding Budget Tiers...")
    budget_list = []
    for key, tier in budget_tiers.items():
        budget_list.append({
            "id": key,
            "name": tier.get('name'),
            "min_price": tier.get('min', 0),
            "max_price": tier.get('max', 0),
            "description": tier.get('description', '')
        })
    if budget_list:
        run_upsert('budget_tiers', budget_list)

if __name__ == "__main__":
    seed_database()
