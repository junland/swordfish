from os.path import join, isfile, abspath

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

# List all files in build_dir
print("Build dir files:")
for f in os.listdir(build_dir):
    print("  " + f)

