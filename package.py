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
