import re
import argparse

def load_spelling_pairs(filepath):
    uk_to_us = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line and not line.startswith('#'):
                uk, us = line.strip().split(',', 1)
                uk_to_us[uk.strip()] = us.strip()
    us_to_uk = {us: uk for uk, us in uk_to_us.items()}
    return uk_to_us, us_to_uk

def find_spellings(text, uk_to_us, us_to_uk):
    found_uk = {}
    found_us = {}

    for uk, us in uk_to_us.items():
        if re.search(r'\b' + re.escape(uk) + r'\b', text, re.IGNORECASE):
            found_uk[uk] = us
    for us, uk in us_to_uk.items():
        if re.search(r'\b' + re.escape(us) + r'\b', text, re.IGNORECASE):
            found_us[us] = uk
    return found_uk, found_us

def display_results(uk_found, us_found):
    if uk_found:
        print("📘 UK spellings found:")
        for uk, us in sorted(uk_found.items()):
            print(f" - {uk} (US: {us})")
    else:
        print("📘 No UK spellings found.")

    print()

    if us_found:
        print("📙 US spellings found:")
        for us, uk in sorted(us_found.items()):
            print(f" - {us} (UK: {uk})")
    else:
        print("📙 No US spellings found.")

    print()
    if uk_found and us_found:
        print("⚠️ Mixed UK/US spelling detected — consider standardising.")
    elif uk_found:
        print("✅ Text appears to be in UK English.")
    elif us_found:
        print("✅ Text appears to be in US English.")
    else:
        print("ℹ️ No UK/US spelling variants detected from the dictionary.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect and display UK/US spelling usage.")
    parser.add_argument('file', nargs='?', help='Optional path to a .txt file to scan.')

    args = parser.parse_args()

    uk_to_us, us_to_uk = load_spelling_pairs('spelling_pairs.txt')

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        print("📋 Paste your text below. Press Enter twice to finish:\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        text = "\n".join(lines)

    uk_found, us_found = find_spellings(text, uk_to_us, us_to_uk)
    display_results(uk_found, us_found)
