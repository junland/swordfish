from os.path import join, isfile, abspath

# Access to global construction environment
Import("env") # type: ignore

project_dir = env["PROJECT_DIR"] # type: ignore

# Output project_dir to console
print("Project dir: " + project_dir)