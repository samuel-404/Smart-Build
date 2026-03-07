"""
Standalone script to scrape live prices from EliteHubs (Shopify JSON API)
and update them directly in the Supabase database.

Run this whenever you want to refresh all component prices:
  python backend/scripts/update_prices_db.py
"""

import httpx
import urllib.parse
import os
import time
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://hisxrqiuytehbunhsyql.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhpc3hycWl1eXRlaGJ1bmhzeXFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzIzNzgwNjcsImV4cCI6MjA4Nzk1NDA2N30.ue87Yhg31SC8iAqL0xc5gyMo8E0xIVMUWQU3vxGJB5E")

supabase_headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


def scrape_price(component_name):
    """Scrape price via EliteHubs Shopify Suggest JSON API (no JS rendering needed)."""
    encoded = urllib.parse.quote(component_name)
    url = f"https://elitehubs.com/search/suggest.json?q={encoded}&resources[type]=product&resources[limit]=1"
    
    try:
        response = httpx.get(url, headers={'User-Agent': 'Mozilla/5.0'}, follow_redirects=True, timeout=10.0)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"  ✗ Network error: {e}")
        return None
    
    products = data.get('resources', {}).get('results', {}).get('products', [])
    
    if not products:
        return None
    
    price_str = products[0].get('price', '')
    
    if not price_str:
        return None
    
    try:
        price = float(price_str)
        return price if price > 0 else None
    except (ValueError, TypeError):
        return None


def fetch_all_components():
    """Fetch all components from Supabase."""
    url = f"{SUPABASE_URL}/rest/v1/components?select=id,name,price"
    response = httpx.get(url, headers=supabase_headers, timeout=10.0)
    response.raise_for_status()
    return response.json()


def update_price_in_db(component_id, new_price):
    """Update a single component's price in Supabase."""
    url = f"{SUPABASE_URL}/rest/v1/components?id=eq.{component_id}"
    response = httpx.patch(url, headers=supabase_headers, json={"price": new_price}, timeout=5.0)
    response.raise_for_status()


def main():
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("ERROR: Missing SUPABASE_URL or SUPABASE_KEY in environment.")
        return
    
    print("Fetching all components from Supabase...")
    components = fetch_all_components()
    print(f"Found {len(components)} components.\n")
    
    updated = 0
    skipped = 0
    
    for i, comp in enumerate(components):
        comp_id = comp['id']
        comp_name = comp['name']
        old_price = comp.get('price', 0)
        
        print(f"[{i+1}/{len(components)}] {comp_name}...", end=" ")
        
        live_price = scrape_price(comp_name)
        
        if live_price and live_price > 0:
            update_price_in_db(comp_id, live_price)
            change = live_price - old_price
            symbol = "+" if change >= 0 else ""
            print(f"✓ ₹{old_price:,.0f} → ₹{live_price:,.0f} ({symbol}{change:,.0f})")
            updated += 1
        else:
            print(f"– Skipped (not found)")
            skipped += 1
        
        # Be nice to the server — small delay between requests
        time.sleep(0.5)
    
    print(f"\n{'='*50}")
    print(f"Done! Updated: {updated}  |  Skipped (not on EliteHubs): {skipped}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
