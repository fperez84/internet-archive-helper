"""
This script is done literally for education purpose and also fun. I knew old
Club Nintendo Chile magazines are available at archive.org, but there are so
many to do click-ops so I thought of automating this using python(Plus, I'm
looking to refine my python skills so this seems like the perfect opportunity).

The script will perform a search on archive.org for 'Club Nintendo' and filter
the results for Chilean issues only. Then it will download them in a given
directory.

For the above, the script is using internetarchive library and to prevent ban
is taking a two seconds delay between downloads.
"""
import time

from pathlib import Path
from internetarchive import search_items, get_item

# Variables init
filtered_results = []
output_dir = Path("/tmp/Club Nintendo")  # Download Directory
DELAY = 2  # Delay in seconds between downloads

# Search for Club Nintendo, key item here is do a title search.
for item in search_items('title:Club Nintendo'):
    # From all identifier returned, filter Chilean issues.
    identifier = item.get('identifier')
    if "chile" in identifier.lower():
        filtered_results.append(identifier)

# Download
# Create direcroty if it doesn't exists. With all parent folders
try:
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Directory created at: {output_dir}")
except Exception as e:
    print(f"Error on directory creation: {e}")

# In order to provide progresion to the user we enumerate the filtered_results
for index, item_id in enumerate(filtered_results, start=1):
    print(f"[{index}/{len(filtered_results)}] Downloading item: {item_id}")
    try:
        item = get_item(item_id)
        # internetarchive from each identifier returns an item that could have
        # more than one file, in our case there are 2 versions of each magazine
        # the one that ends with _text seems to be for mobile view, which I'm
        # not looking for, that's why Im filtering those out.
        files = item.files
        for file in files:
            if file['name'].endswith('.pdf') and '_text' not in file['name']:
                item.download(glob_pattern=file['name'], destdir=output_dir, verbose=True)
                print(f"✔ Download completed for: {file['name']}")
    except Exception as e:
        print(f"❌ Download error at: {item_id}: {e}")
    # Delay between each download.
    time.sleep(DELAY)

print("🎉 All downloads finished!.")
