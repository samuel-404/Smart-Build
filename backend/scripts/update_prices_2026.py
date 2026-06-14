"""
Update ALL component prices to accurate 2026 Indian market values.
Sources: Amazon India, MD Computers, PCStudio, Vedant Computers, EliteHubs (March 2026)
"""
import json, os

data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'seed_data.json')

# ═══════════════════════════════════════════════════════════════════════════════
#  2026 INDIAN MARKET PRICES (₹)
# ═══════════════════════════════════════════════════════════════════════════════
PRICES_2026 = {
    # ─── CPUs ─────────────────────────────────────────────────────────────
    "cpu_001":  7499,    # i3-12100F — older gen, price dropped
    "cpu_002": 14999,    # i5-13400F — price dropping with 14th gen out
    "cpu_003": 32999,    # i7-13700KF
    "cpu_004":  9999,    # Ryzen 5 5600 — budget king, prices dropped
    "cpu_005": 23999,    # Ryzen 7 7700X — price settled
    "cpu_006": 44999,    # Ryzen 9 7950X — superseded by 9950X
    "cpu_007": 11999,    # i5-12400F — older, discounted
    "cpu_008": 28999,    # Ryzen 9 5950X — end of life AM4
    "cpu_009": 49999,    # i9-13900K
    "cpu_010": 54999,    # i9-14900K
    "cpu_011": 64999,    # i9-14900KS
    "cpu_012": 14999,    # Ryzen 5 7600
    "cpu_013": 21999,    # Ryzen 7 7700
    "cpu_014": 34999,    # Ryzen 7 7800X3D — still in demand for gaming
    "cpu_015": 54999,    # Ryzen 9 7950X3D
    "cpu_016": 39999,    # i7-14700K
    "cpu_017": 23499,    # i5-14600K
    "cpu_018": 11999,    # Ryzen 5 5600X — mature pricing
    "cpu_019": 28999,    # Ryzen 9 5950X (dup)
    "cpu_020": 46999,    # Ryzen 7 9800X3D — newest gaming king
    "cpu_021": 20999,    # Ryzen 5 9600X
    "cpu_022": 28999,    # Ryzen 7 9700X
    "cpu_023": 42999,    # Ryzen 9 9900X
    "cpu_024": 56999,    # Ryzen 9 9950X
    "cpu_025":  9999,    # i3-12100
    "cpu_026": 11499,    # i3-13100
    "cpu_027": 13999,    # i5-12400
    "cpu_028": 17499,    # i5-13400
    "cpu_040":  6999,    # i5-10400F — very old, heavily discounted
    "cpu_041":  8499,    # i5-11400F — old gen
    "cpu_042":  8999,    # Ryzen 5 3600 — legacy, still available
    "cpu_043": 13499,    # Ryzen 7 3700X — legacy
    "cpu_044": 18999,    # Ryzen 9 3900X — legacy
    "cpu_045":  7499,    # Ryzen 5 5500 — cheapest AM4 option
    "cpu_046": 16999,    # Ryzen 7 5800X — mature pricing
    "cpu_047": 21999,    # Ryzen 9 5900X — EOL discounts
    "cpu_048": 15999,    # i5-14400F — current budget champ
    "cpu_049": 36999,    # i7-14700KF

    # ─── APUs ─────────────────────────────────────────────────────────────
    "apu_001":  5999,    # Ryzen 3 3200G — very old
    "apu_002":  7999,    # Ryzen 5 3400G — old
    "apu_003": 10999,    # Ryzen 5 5600G — good budget APU
    "apu_004": 15499,    # Ryzen 7 5700G
    "apu_005":  3499,    # Athlon 3000G — entry level
    "apu_006":  8999,    # Ryzen 5 4600G
    "apu_007": 19999,    # Ryzen 5 8600G — new gen APU
    "apu_008": 25999,    # Ryzen 7 8700G

    # ─── Motherboards ────────────────────────────────────────────────────
    "mb_001":   9999,    # B660M-A D4
    "mb_002":  22999,    # Z790-A WiFi DDR5
    "mb_003":  11999,    # B550 AORUS Elite V2 — discount with AM5 out
    "mb_004":  26499,    # B650E-F Gaming WiFi
    "mb_005":   7499,    # B660M Pro RS
    "mb_006":  29999,    # X670E TOMAHAWK
    "mb_007":   8499,    # B660M-C D4
    "mb_008":  36999,    # X670E AORUS Master
    "mb_009":  38999,    # X870E Phantom Gaming
    "mb_010":  35999,    # Z790-E Gaming WiFi
    "mb_011":  48999,    # Z690 Godlike — old, discounted
    "mb_012":  21999,    # B650 AORUS Elite AX
    "mb_013":  13499,    # B850M Pro RS
    "mb_014":  10999,    # H770-PLUS D4
    "mb_015":  10999,    # B550 Tomahawk — AM4 discount
    "mb_016":  32999,    # Z690 Dark K3
    "mb_am4_001": 4499,  # B450M DS3H V2 — budget AM4
    "mb_am4_002": 3999,  # A520M-A PRO — cheapest
    "mb_am4_003": 5499,  # B450M Pro4-F
    "mb_am4_004": 6499,  # B550M DS3H
    "mb_am4_005": 3499,  # A320M-K — bottom tier
    "mb_020":   8999,    # B560M-PLUS WiFi
    "mb_021":  10999,    # B560 Tomahawk
    "mb_022":   8499,    # B760M-A WiFi DDR4
    "mb_023":  21499,    # B650 AORUS Elite AX
    "mb_024":  20499,    # B650 Carbon WiFi

    # ─── GPUs ─────────────────────────────────────────────────────────────
    "gpu_001": 259999,   # RTX 5090 — flagship 2025
    "gpu_002": 149999,   # RTX 5080
    "gpu_003":  84999,   # RTX 5070 Ti
    "gpu_004":  59999,   # RTX 5070
    "gpu_005":  37999,   # RTX 5060 Ti
    "gpu_006":  27999,   # RTX 5060
    "gpu_007":  74999,   # RTX 4080 Super — discounted with 5080 out
    "gpu_008":  44999,   # RTX 4070 Super — discounted
    "gpu_009":  37999,   # RTX 4070 — discounted
    "gpu_010":  29999,   # RTX 4060 Ti — still popular
    "gpu_011":  69999,   # RX 7900 XTX — discounted with 9000 out
    "gpu_012":  56999,   # RX 7900 XT
    "gpu_013":  39999,   # RX 7800 XT — great value in 2026
    "gpu_014":  31999,   # RX 7700 XT
    "gpu_015":  19999,   # RX 7600 — budget champ
    "gpu_016":  11999,   # GTX 1650 Super — old but still sold
    "gpu_017":  24999,   # Arc A770 16GB — discounted
    "gpu_018":  17999,   # Arc A750 — budget
    "gpu_040":  24999,   # RTX 4060 — price dropped
    "gpu_041": 159999,   # RTX 4090 — still expensive
    "gpu_042":  64999,   # RTX 4070 Ti SUPER — discounted
    "gpu_030":  19999,   # RTX 3060 — old gen clearance
    "gpu_031":  24999,   # RTX 3060 Ti — clearance
    "gpu_032":  29999,   # RTX 3070 — clearance
    "gpu_033":  34999,   # RTX 3070 Ti
    "gpu_034":  42999,   # RTX 3080 — used/clearance
    "gpu_035":  49999,   # RTX 3080 Ti
    "gpu_036":  74999,   # RTX 3090 — collector/workstation
    "gpu_050":  13999,   # GTX 1660 Super — very old
    "gpu_051":  15999,   # GTX 1660 Ti
    "gpu_052":  17999,   # RTX 2060 — legacy
    "gpu_053":  27999,   # RTX 2070 Super — legacy
    "gpu_060":  15999,   # RX 6600 — cheap
    "gpu_061":  18999,   # RX 6600 XT
    "gpu_062":  22999,   # RX 6700 XT
    "gpu_063":  36999,   # RX 6800 XT — clearance
    "gpu_064":  44999,   # RX 6900 XT — clearance
    "gpu_070":  54999,   # RX 9070 XT — new RDNA 4
    "gpu_071":  46999,   # RX 9070
    "gpu_072":  28999,   # RX 9060 XT

    # ─── RAM ──────────────────────────────────────────────────────────────
    "ram_001":  2799,    # 16GB DDR4-3200 — dirt cheap in 2026
    "ram_002":  7999,    # 32GB DDR5-6000
    "ram_003":  4999,    # 32GB DDR4-3600
    "ram_004":  5999,    # 32GB DDR5-5600
    "ram_005": 14999,    # 64GB DDR5-6400
    "ram_006": 10499,    # 32GB DDR5-7200
    "ram_007":  1999,    # 16GB DDR4-3200 single
    "ram_008": 29999,    # 128GB DDR5-6000
    "ram_009":  6999,    # 32GB DDR5-5600 Dominator
    "ram_010":  2299,    # 16GB DDR4-3200
    "ram_011": 11499,    # 32GB DDR5-7200 RGB
    "ram_012":  2499,    # 16GB DDR4-3600
    "ram_013":  9999,    # 32GB DDR5-6400
    "ram_014": 16999,    # 64GB DDR5-5600
    "ram_015":  2699,    # 16GB DDR4-3600
    "ram_016": 13999,    # 64GB DDR5-6000

    # ─── PSUs ─────────────────────────────────────────────────────────────
    "psu_001":  3499,    # CV550 550W Bronze
    "psu_002":  5499,    # MWE Gold 650W
    "psu_003":  9999,    # RM850x 850W Gold
    "psu_004": 12999,    # Seasonic Focus GX-1000
    "psu_005":  7499,    # EVGA SuperNOVA 750W
    "psu_006": 16499,    # HX1200i 1200W Platinum
    "psu_007":  5999,    # be quiet! 600W Gold
    "psu_008":  8999,    # Toughpower GF1 850W
    "psu_009": 19999,    # ROG Strix 1200W Platinum
    "psu_010":  8499,    # P850GM 850W
    "psu_011":  6999,    # Prime Ultra 750W
    "psu_012": 10999,    # RM1000x 1000W Gold
    "psu_013":  8499,    # MPG A850G 850W
    "psu_014":  3999,    # Antec 650W Bronze
    "psu_015":  8999,    # ION Gold 850W

    # ─── Cases ────────────────────────────────────────────────────────────
    "case_001":  2299,   # Ant Esports ICE-112
    "case_002":  7499,   # Corsair 4000D Airflow
    "case_003":  6499,   # NZXT H510 Flow
    "case_004": 12999,   # Lian Li O11 Dynamic EVO
    "case_005": 10999,   # Phanteks P500A D-RGB
    "case_006":  7999,   # Fractal Design North
    "case_007":  9999,   # Lian Li A4-H2O
    "case_008": 16999,   # HAF 700 EVO
    "case_009": 28999,   # Corsair 5000T RGB
    "case_010": 14999,   # Lian Li O11 Dynamic XL
    "case_011": 19999,   # The Tower 900
    "case_012":  6999,   # Obsidian 500D
    "case_013": 24999,   # NZXT Kraken Elite 360
    "case_014": 21999,   # Fractal Torrent RGB

    # ─── Storage ──────────────────────────────────────────────────────────
    "storage_001":  2999,  # Samsung 980 500GB — cheap in 2026
    "storage_002":  7999,  # Samsung 990 Pro 1TB
    "storage_003":  4499,  # WD Blue SN580 1TB
    "storage_004":  7499,  # Crucial P3 Plus 2TB
    "storage_005":  6999,  # SK Hynix P41 1TB
    "storage_006":  5999,  # Seagate Barracuda 4TB HDD
    "storage_007": 10499,  # Sabrent Rocket 4 Plus 2TB
    "storage_008":  3999,  # Samsung 870 QVO 1TB
    "storage_009":  3999,  # Kingston A3000 1TB
    "storage_010":  9999,  # WD Black SN850X 2TB
    "storage_011": 15999,  # Corsair MP600 4TB
    "storage_012":  6999,  # Crucial BX500 2TB SSD
    "storage_013": 10999,  # Seagate BarraCuda Pro 8TB HDD
    "storage_014": 11999,  # Samsung 980 Pro 2TB
    "storage_015": 18999,  # Intel Optane 905P 480GB
    "storage_016":  7999,  # ADATA SX8200 Pro 2TB
    "storage_017":  6499,  # Sabrent XTRM-Q 1TB
    "storage_018": 12999,  # WD Blue 3D 4TB SSD
    "storage_019":  8999,  # Samsung 990 EVO 2TB
}


def main():
    with open(data_path, 'r') as f:
        data = json.load(f)

    updated = 0
    for cat in data['components']:
        for comp in data['components'][cat]:
            cid = comp['id']
            if cid in PRICES_2026:
                old = comp['price']
                new = PRICES_2026[cid]
                if old != new:
                    comp['price'] = new
                    updated += 1
                    diff = new - old
                    symbol = "+" if diff >= 0 else ""
                    print(f"  {comp['name']:45s} Rs.{old:>7,d} -> Rs.{new:>7,d} ({symbol}{diff:,d})")

    with open(data_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nUpdated {updated} prices in seed_data.json")


if __name__ == "__main__":
    main()
