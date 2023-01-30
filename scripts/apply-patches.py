import os

# Access to global construction environment
Import("env") # type: ignore

project_dir = env["PROJECT_DIR"] # type: ignore
workspace_dir = env["PROJECT_DIR"] # type: ignore
src_dir = env["PROJECT_SRC_DIR"] # type: ignore
build_dir = env["PROJECT_BUILD_DIR"] # type: ignore

# Output project_dir to console
print("Project dir: " + project_dir)
print("Workspace dir: " + workspace_dir)
print("Source dir: " + src_dir)
print("Build dir: " + build_dir)

# List all files in build_dir within 3 levels
for root, dirs, files in os.walk(build_dir, topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))


