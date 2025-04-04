import os
import re
import argparse
from pathlib import Path
import shutil
import tldextract

# TLDs to ignore when extracting domains (due to common method name collisions)
EXCLUDED_TLDS = {
    "py", "post", "tab", "read", "menu", "save", "place", "call", "run", "select", "open"
}

# --- Get absolute path to script directory ---
SCRIPT_DIR = Path(__file__).resolve().parent
suffix_list_path = SCRIPT_DIR / "public_suffix_list.dat"

# --- Create a temporary cache dir for tldextract ---
tld_cache_dir = SCRIPT_DIR / ".tld_cache"
tld_cache_dir.mkdir(exist_ok=True)

# --- Copy the suffix file there under expected name ---
shutil.copy(suffix_list_path, tld_cache_dir / "public_suffix_list.dat")

# --- Use tldextract with local cache only ---
ext = tldextract.TLDExtract(
    cache_dir=str(tld_cache_dir),
    suffix_list_urls=[]
)

# --- Regexes ---
url_regex = re.compile(
    r'\b(?:https?|ftp)://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})(?::\d{1,5})?(?:/[^\s"\'<>()]*)?',
    re.IGNORECASE
)

ip_regex = re.compile(
    r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
)


def extract_domains_from_text(text):
    # Grab domain-like patterns first
    raw_candidates = re.findall(r'\b[a-zA-Z0-9.-]+\.[a-z]{2,}\b', text)
    base_domains = set()
    for host in raw_candidates:
        parsed = ext(host)
        if parsed.domain and parsed.suffix:
            # Skip domains with ignored suffixes (TLDs)
            if parsed.suffix.lower() in EXCLUDED_TLDS:
                continue
            base_domains.add(f"{parsed.domain}.{parsed.suffix}")
    return sorted(base_domains)


def extract_iocs(text, extract_urls=False, extract_domains=False, extract_ips=False):
    results = {}
    if extract_urls:
        results['urls'] = sorted(set(url_regex.findall(text)))
    if extract_domains:
        results['domains'] = extract_domains_from_text(text)
    if extract_ips:
        results['ips'] = sorted(set(ip_regex.findall(text)))
    return results

def extract_from_file(file_path, args):
    try:
        content = Path(file_path).read_text(errors='ignore')
        iocs = extract_iocs(content, args.urls, args.domains, args.ips)
        return (file_path, iocs)
    except Exception as e:
        return (file_path, {"error": str(e)})

def main():
    parser = argparse.ArgumentParser(description="IOC Extractor")
    parser.add_argument("--file", help="Target file")
    parser.add_argument("--dir", help="Target directory")
    parser.add_argument("--urls", action="store_true", help="Extract URLs")
    parser.add_argument("--domains", action="store_true", help="Extract domains")
    parser.add_argument("--ips", action="store_true", help="Extract IP addresses")
    args = parser.parse_args()

    if not (args.file or args.dir):
        parser.error("You must specify either --file or --dir")

    if not any([args.urls, args.domains, args.ips]):
        parser.error("You must specify at least one of --urls, --domains, or --ips")

    targets = []
    if args.file:
        targets = [Path(args.file)]
    elif args.dir:
        targets = list(Path(args.dir).rglob("*"))

    for path in targets:
        if path.is_file():
            file_path, iocs = extract_from_file(path, args)
            print(f"=== {file_path} ===")
            if "error" in iocs:
                print(f"Error: {iocs['error']}")
                continue
            for ioc_type, values in iocs.items():
                print(f"[{ioc_type.upper()}]")
                for val in values:
                    print(val)
                print()

if __name__ == "__main__":
    main()
