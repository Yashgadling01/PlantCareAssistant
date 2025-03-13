import os

# Define the project structure
project_structure = {
    "data": ["raw", "processed"],
    "models": [],
    "notebooks": [],
    "src": ["preprocessing.py", "train_model.py", "predict.py", "api_integration.py"],
    "web": ["app.py", "templates", "static"],
    "": ["requirements.txt", "README.md", ".gitignore"]
}

# Create folders and files
for folder, files in project_structure.items():
    path = os.path.join("PlantCareAssistant", folder)
    os.makedirs(path, exist_ok=True)  # Create folder if it doesn't exist
    for file in files:
        file_path = os.path.join(path, file)
        if "." in file:  # Create files only if they have an extension
            with open(file_path, "w") as f:
                pass  # Create an empty file

print("✅ Project structure created successfully!")
