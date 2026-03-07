"""
Standalone script to scrape live prices from EliteHubs
and update them directly in the Supabase database.

Run this whenever you want to refresh all component prices:
  python backend/scripts/update_prices_db.py
"""

import httpx
import urllib.parse
import os
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://hisxrqiuytehbunhsyql.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhpc3hycWl1eXRlaGJ1bmhzeXFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzIzNzgwNjcsImV4cCI6MjA4Nzk1NDA2N30.ue87Yhg31SC8iAqL0xc5gyMo8E0xIVMUWQU3vxGJB5E")

supabase_headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

scrape_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}


def scrape_price(component_name):
    """Scrape the price for a single component from EliteHubs."""
    encoded = urllib.parse.quote(component_name)
    url = f"https://elitehubs.com/search?type=product&options%5Bprefix%5D=last&q={encoded}"
    
    try:
        response = httpx.get(url, headers=scrape_headers, follow_redirects=True, timeout=10.0)
        response.raise_for_status()
    except Exception as e:
        print(f"  ✗ Network error: {e}")
        return None
        
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.select('.grid__item .card-wrapper')
    
    if not products:
        return None
        
    first_product = products[0]
    price_elem = first_product.select_one('.price-item--sale') or first_product.select_one('.price-item--regular')
    
    if not price_elem:
        return None
        
    raw_price = price_elem.text.strip()
    clean_price = "".join(c for c in raw_price if c.isdigit() or c == '.')
    
    try:
        return float(clean_price)
    except ValueError:
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
    failed = 0
    skipped = 0
    
    for i, comp in enumerate(components):
        comp_id = comp['id']
        comp_name = comp['name']
        old_price = comp.get('price', 0)
        
        print(f"[{i+1}/{len(components)}] {comp_name}...")
        
        live_price = scrape_price(comp_name)
        
        if live_price and live_price > 0:
            update_price_in_db(comp_id, live_price)
            change = live_price - old_price
            symbol = "+" if change >= 0 else ""
            print(f"  ✓ ₹{old_price:,.0f} → ₹{live_price:,.0f} ({symbol}{change:,.0f})")
            updated += 1
        else:
            print(f"  – Skipped (no price found on EliteHubs)")
            skipped += 1
        
        # Be nice to the server — wait 1 second between requests
        time.sleep(1)
    
    print(f"\n{'='*50}")
    print(f"Done! Updated: {updated}  |  Skipped: {skipped}  |  Failed: {failed}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
