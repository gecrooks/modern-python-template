import subprocess


def git_init_and_tag():
    """
    Invoke the initial git and tag with 0.0.0 to make an initial version.
    """

    subprocess.check_output("git init", shell=True, stderr=subprocess.STDOUT)
    subprocess.check_output("git add -A .", shell=True, stderr=subprocess.STDOUT)
    subprocess.check_output(
        "git commit -m 'Initialize from modern-python-template'",
        shell=True,
        stderr=subprocess.STDOUT,
    )
    subprocess.check_output("git tag v0.0.0", shell=True, stderr=subprocess.STDOUT)
    subprocess.check_output(
        "pip install -e .[dev]", shell=True, stderr=subprocess.STDOUT
    )


if __name__ == "__main__":
    if "{{ cookiecutter.initilize_git_repo }}" in ["y", "Y"]:
        git_init_and_tag()
