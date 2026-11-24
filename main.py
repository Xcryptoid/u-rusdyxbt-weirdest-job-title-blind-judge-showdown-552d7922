import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
    os.path.join(OUTPUT_DIR, "entry.txt"),
)
