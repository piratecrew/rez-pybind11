name = "pybind11"

version = "2.13.5"

variants = [
    ["platform-linux", "python-3.9"],
    ["platform-linux", "python-3.10"],
    ["platform-linux", "python-3.11"],
]

private_build_requires = [
    "gcc-11"
]

build_requires = [
    "cmake-3.15+<4"
]

build_command = "make -f {root}/Makefile {install}"

def commands():
    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
