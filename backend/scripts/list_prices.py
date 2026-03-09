import json, os
d = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'data', 'seed_data.json')))
for cat in d['components']:
    print(f"\n=== {cat} ===")
    for c in d['components'][cat]:
        print(f"  {c['id']:15s} Rs.{c['price']:>7d}  {c['name']}")
