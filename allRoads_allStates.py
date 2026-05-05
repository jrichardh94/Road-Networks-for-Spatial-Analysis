import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

BASE_URL = "https://www2.census.gov/geo/tiger/TIGER2025/ROADS/"
OUT_DIR = Path(r"C:\path\to\your\data")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_RETRIES = 5
WAIT_BETWEEN_FILES = 0.75
CHUNK_SIZE = 1024 * 1024

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "*/*",
})

html = session.get(BASE_URL, timeout=60).text

zip_urls = sorted(set(
    urljoin(BASE_URL, match)
    for match in re.findall(r'href="([^"]+\.zip)"', html, flags=re.I)
))

print(f"Found {len(zip_urls)} zip files.")

failed_files = []

for i, url in enumerate(zip_urls, start=1):
    filename = url.split("/")[-1]
    out_path = OUT_DIR / filename
    temp_path = OUT_DIR / f"{filename}.part"

    if out_path.exists():
        print(f"[{i}/{len(zip_urls)}] Skipping existing {filename}")
        continue

    print(f"[{i}/{len(zip_urls)}] Downloading {filename}")

    success = False

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if temp_path.exists():
                temp_path.unlink()  # delete partial failed download

            with session.get(url, stream=True, timeout=(30, 300)) as r:
                if r.status_code == 403:
                    print(f"  403 Forbidden on attempt {attempt}; waiting...")
                    time.sleep(10 * attempt)
                    continue

                r.raise_for_status()

                with open(temp_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)

            temp_path.rename(out_path)
            success = True
            break

        except requests.exceptions.RequestException as e:
            print(f"  Attempt {attempt} failed: {e}")
            time.sleep(10 * attempt)

    if not success:
        print(f"  FAILED after {MAX_RETRIES} attempts: {filename}")
        failed_files.append(filename)

    time.sleep(WAIT_BETWEEN_FILES)

print("Done.")

if failed_files:
    print("\nFailed files:")
    for f in failed_files:
        print(f)
