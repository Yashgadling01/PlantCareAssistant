import os

dirs = ["backend", "frontend", "Dataset"]
files = {
    "backend": ["plant_id_api.py", "trefle_api.py"],
    "frontend": ["app.py"]
}

for d in dirs:
    os.makedirs(d, exist_ok=True)
    for f in files.get(d, []):
        with open(os.path.join(d, f), "w") as file:
            file.write("# " + f)
