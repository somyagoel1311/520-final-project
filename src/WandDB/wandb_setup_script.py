import wandb

"""
This script allows you to create a workspace in Wandb and integrate your python code to the tool.
"""

def run_wandb():
    print("The program will shortly ask for your API token")
    wandb.login() # this token can be accessed through Wandb authorise with your wandb account
    # https://wandb.ai/authorize
    project = "520"
    run = wandb.init(
        project=project,
         config={
    "architecture": "Alex-Net",
    "dataset": "CIFAR-10",
    }
    
        )

if __name__ == '__main__':
    run_wandb()