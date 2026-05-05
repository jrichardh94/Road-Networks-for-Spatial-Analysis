import arcpy
from pathlib import Path
import re
import zipfile
import os

ZIP_DIR = r"C:\Users\jrich\OneDrive\Desktop\Rail Passengers Association\01_Received_Info\All Roads All States"
GDB_PATH = r"C:\Users\jrich\OneDrive\Desktop\Rail Passengers Association\01_Received_Info\All Roads All States\TIGER2025_STATE_ROADS.gdb"

# create GDB if it doesn't exist
if not arcpy.Exists(GDB_PATH):
    arcpy.management.CreateFileGDB(os.path.dirname(GDB_PATH), os.path.basename(GDB_PATH))

zip_files = list(Path(ZIP_DIR).glob("tl_2025_*_roads.zip"))

state_groups = {}

# group by state
for z in zip_files:
    m = re.search(r"tl_2025_(\d{5})_roads", z.name)
    if not m:
        continue

    county_fips = m.group(1)
    state_fips = county_fips[:2]

    state_groups.setdefault(state_fips, []).append(z)

print(f"Found {len(state_groups)} states")

# process each state
for state_fips, files in state_groups.items():
    print(f"\nProcessing state {state_fips}")

    out_fc = f"{GDB_PATH}\\roads_{state_fips}"
    first = True

    for i, z in enumerate(files, start=1):
        print(f"  [{i}/{len(files)}] {z.name}")

        try:
            # unzip to temp folder
            temp_dir = Path(ZIP_DIR) / "temp"
            temp_dir.mkdir(exist_ok=True)

            with zipfile.ZipFile(z, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            shp = list(temp_dir.glob("*.shp"))[0]

            if first:
                arcpy.management.CopyFeatures(str(shp), out_fc)
                first = False
            else:
                arcpy.management.Append(str(shp), out_fc, "NO_TEST")

            # clean temp
            for f in temp_dir.glob("*"):
                f.unlink()

        except Exception as e:
            print(f"    ERROR: {e}")

print("Done.")