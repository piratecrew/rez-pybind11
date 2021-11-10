name = "pybind11"

version = "2.8.1"

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3.7"]
]

build_command = "make -f {root}/Makefile {install}"

def commands():
    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
