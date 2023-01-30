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

for root, dirs, files in os.walk(build_dir):
    depth = root[len(build_dir) + len(os.path.sep):].count(os.path.sep)
    if depth > 5:
        del dirs[:]
    print(root, dirs, files)

def before_buildprog(source, target, env):
    print("before_buildprog")
    for root, dirs, files in os.walk(build_dir):
        depth = root[len(build_dir) + len(os.path.sep):].count(os.path.sep)
        if depth > 5:
            del dirs[:]
        print(root, dirs, files)

env.AddPreAction("buildprog", before_buildprog) # type: ignore