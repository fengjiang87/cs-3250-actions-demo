# cs-3250-actions-demo test
## Step-by-step guide to cloning a repo, installing & running pytest, and setting up GitHub Actions for automated unit testing, linting, and formatting

### Clone the repo

First, make sure you are signed in to GitHub. Fork this repo by visiting https://github.com/bednie/cs-3250-actions-demo/fork. Create a fork with yourself as the owner. 

Next, in VS Code, open a new window, and click "Clone Git Repository...".

At the top of the window, paste in your repo's .git link, https://github.com/{your_username}/cs-3250-actions-demo.git, and hit enter. 

Then select the local folder where you would like this repo to be located. It is a good idea to put it in its own temp folder so it can be deleted easily once you finish this demo.

Now you can open the repo and begin the next section of this demo. 

### Install pytest

To install pytest, open your terminal and run the command ```pip install -U pytest```, or follow the intructions here: https://docs.pytest.org/en/7.1.x/getting-started.html.

### Run pytest 

Now that you have installed pytest, run it using the command ```pytest```. There are many optional commands which you can see by running ```pytest --help```, but for this simple demo, pytest will automatically discover and run our tests (pytest will run all files that match the form "test_\*.py" or "\*_test.py"). 

Upon running pytest, you should see some terminal output showing the results of the tests. 

But what if we forget to run pytest, or a contributor merges code that hasn't been tested?

### Automating unit tests

We can automate unit tests, and even other actions like linting and formatting.

GitHub Actions is one way to do this. Actions has many templates, or you can set up an action with your own YAML script, the configuration file format that Actions uses.

For this demo, you can download these two files by clicking the links and doing "Save as..." pytest.yml and ruff.yml,respectively: 

- [pytest.yml](https://gist.githubusercontent.com/bednie/bbf1418b5a5af15cfb0a548a4865cfec/raw/d68b6f0568532209ec35056cf01e9058955a92e8/pytest.yml)

- [ruff.yml](https://gist.githubusercontent.com/bednie/7d2863227e4263b618eb91656681227d/raw/d1f1017a7dd73803de09198dc43855493b729ac5/ruff.yml)

Now that you have downloaded these files, we will need to put them in a special folder so that GitHub Actions knows where to find them. 

In the root of this demo repo, create a directory called ".github" (the "." is important so make sure to include it. Also, this folder will be hidden--make sure to set hidden folders to be visible on your machine), and then within .github/, create another directory called "workflows".

Move both pytest.yml and ruff.yml into workflows. 

### Running GitHub Actions

First, we will need to push the changes we made in the repo--which is a local repo on your machine--to GitHub.com. GitHub we be our remote repo. You can do this by running the command "git push origin main" in your terminal. 

Now, whenever we merge code into this repo (whether by pull request or pushing), these Actions will run on the repo. 

Once you have pushed this demo repo to your GitHub account, add a failing unit test to "test_demo_functions.py", and then merge in these changes, too:

```
def test_false():
    assert False, "This will always fail"
```

Finally, go to https://github.com/{your_username}/cs-3250-actions-demo/settings/actions and update the Workflow Permissions at the bottom of the page to allow "Read and write permissions" as well as "Allow GitHub Actions to create and approve pull requests". See the screenshot below:

![workflow-permissions.png](/workflow_permissions.png)

### Checking results of Actions runs 

When we attempt to push this code to our remote repo on GitHub, Actions will run the ruff linter & formatter as well as the unit tests.

We can view past runs' results and re-run jobs here: https://github.com/{your_username}/cs-3250-actions-demo/actions

A failed pytest run should be visible here if you merged in the failing test above.

### Next steps 

This is just a demo: it is possible to add more Actions, and even disallow merges with failing tests, by editing the .yml files in ".github/workflows/".

Add a workflow status [badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge).

Check out the [Actions documentation](https://docs.github.com/en/actions). 
