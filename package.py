name = "pybind11"

version = "2.13.5"

variants = [
    ["platform-linux", "python-3.9"],
    ["platform-linux", "python-3.10"],
    ["platform-linux", "python-3.11"],
]

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    requirements = ["cmake-3.15+<4"]
    from subprocess import check_output
    gcc_major = int(check_output(r"gcc -dumpversion | cut -f1 -d.", shell=True).strip().decode())
    if gcc_major < 9:
        requirements.append("devtoolset-9")

    return requirements

build_command = "make -f {root}/Makefile {install}"

def commands():
    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
