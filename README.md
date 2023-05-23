# 520-final-project
520 final project

## Tool Comparison : Neptune AI vs WanDB AI

### Model Integration:

#### 1. Neptune 

Steps to Integrate your own ML model to Neptune AI:

a.Run the script 'neptune_integration.py'.
b.It'll prompt you for an API token. This token can be accessed from your Neptune account. 

Steps to find your NEPTUNE API token:

a. There will be a user menu at the bottom left of your Neptune app. Expand it and click on "Get your API token." That will display your API token. Copy it to your clipboard, and enter it when asked by the code.

#### 2. WanDB AI 

Steps to Initiate WandB logging to the ML model - 

1. On Running the wandb script (wandb_setup_script), you will receive a prompt for authorising with an API Token on https://wandb.ai/authorize. 
2. This token can be found in the "User settings" Section. 

Wandb results Report Link -

The following is the link to one of the reports we had created using Wandb for our experiments. 
[Published report of results](https://api.wandb.ai/links/ssmm/pj7nk9y3)


#### 3. Evaluation

Our Approach:

We have run AlexNet on CIFAR-10 dataset to perform an image classification task. The code has been integrated with both the tools and required information has been stored on the tool.
We used this as the basis of our tool comparison.

##### 3.1 Evaluation metrics
For an effective study and analysis we have identified a set of functional and non-functional requirements that are essential for MLOps tools. We have studied features encapsulating these requirements and are quantitatively measuring them using a Rating scale described in detail below.

Functional Requirements:

1. Dataset versioning -> Versioning of data in different stages and experiments for reproducibility
2. Model versioning -> Versioning of models to help in comparison, running multiple experiments, etc
3. Collaboration ->  Features supporting multi-member team collaboration on projects.
4. Framework Integration -> Integration of popular ML frameworks in the market
5. Report generation and management -> Creating and managing of reports for cataloging and stakeholder communication.
6. Model Visualization -> Visualization of the model for explainability

Non Functional Requirements:

1. Understandability -> The documentation and resources available to learn and onboard with the tools.
2. Usability -> The ease of onboarding and working with the tool day to day.
3. Debuggability -> Capabilities supporting the debugging of issues as part of any experiment/run.


##### 3.2 Rating scale

We are using a 3 point quantitative scale to evaluate how well a tool works. For each of our mentioned evaluation criterias,
both the tools get a rating between 1 and 3. Following is the definition of each rating:


1. Tool does not have this ability.
2. Tool has a satisfactory performance for this evaluation criteria.
3. Tool performs well for this criteria and also makes it easy to use this ability.


#### 4. Result

Each tool has been given a rating based on the above definitions. For a more comprehensive analysis of comparison between these two tools, please refer to our report present in the repository.

#### 5. Work Distribution

The study involved two pairs, with each pair being assigned responsibility for one of the tools being compared. The pairs conducted individual investigations into their respective tools, gathering and analyzing data on various aspects. Subsequently, the findings from each tool were compiled, and a comprehensive group comparison of the results was performed.

Git hub Username: Madhusamhitha, 
Programming pair: Sushrita Yerra, Madhu Samhitha Vangara
Tool: wandb

Git hub Username: somyagoel1311
Programming pair: Somya Goel, Mahima Choudha
Tool: NeptuneAI




