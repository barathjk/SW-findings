load("@bazel_tools//tools/python:toolchain.bzl", "py_runtime", "py_runtime_pair")

py_runtime(
    name = "my_py3_runtime",
    interpreter_path = "/usr/bin/python3",  # Path to your local Python interpreter
    python_version = "PY3",
)

py_runtime_pair(
    name = "my_py3_runtime_pair",
    py3_runtime = ":my_py3_runtime",
    py2_runtime = None,
)

toolchain(
    name = "my_python_toolchain",
    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
    toolchain = ":my_py3_runtime_pair",
)
