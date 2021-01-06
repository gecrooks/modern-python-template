import subprocess


def git_init_and_tag():
    """
    Invoke the initial git and tag with 0.0.0 to make an initial version.
    """

    subprocess.check_output("git init", shell=True, stderr=subprocess.STDOUT)
    subprocess.check_output("git add -A .", shell=True, stderr=subprocess.STDOUT)
    subprocess.check_output(
        f"git commit -m 'Initialize from gecrooks-python-template'",
        shell=True,
        stderr=subprocess.STDOUT,
    )
    subprocess.check_output("git tag v0.0.0", shell=True, stderr=subprocess.STDOUT)
    subprocess.check_output(
        "pip install -e .[dev]", shell=True, stderr=subprocess.STDOUT
    )


git_init_and_tag()
