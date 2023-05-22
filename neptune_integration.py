import neptune
from getpass import getpass

"""
This script allows you to create a workspace in Neptune AI and integrate your python code to the tool.
"""


def run_neptune():
    print("The program will shortly ask for your API token")
    api_token = getpass("Enter your private neptune AI token:") # this token can be accessed through Neptune App

    workspace = "somyagoel"
    project_name = "Neptune-Integration"
    project = f"{workspace}/{project_name}"
    print("Project directory:", project)

    run = neptune.init_run(
        project=project,
        api_token=api_token,
        capture_hardware_metrics=True,
        capture_stderr=True,
        capture_stdout=True,
    )


if __name__ == '__main__':
    run_neptune()
