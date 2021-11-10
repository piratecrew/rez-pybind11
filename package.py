name = "pybind11"

version = "2.8.1"

variants = [
    ["platform-linux", "python-2.7"],
    ["platform-linux", "python-3.7"]
]

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    from subprocess import check_output
    valid = check_output(r"expr `gcc -dumpversion | cut -f1 -d.` \>= 9 || true", shell=True).strip().decode() == "1"
    if not valid:
        return ["devtoolset-9"]
    return []

build_command = "make -f {root}/Makefile {install}"

def commands():
    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
