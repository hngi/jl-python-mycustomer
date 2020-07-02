# Contributing

This project is open to contributions. However, here are the guidelines to follow:

### Submitting Issues

Issues are the way by which contributions will be tracked so don't hesitate to pick an issue and try to work on them.

### Submitting code (features, bugfixes .....)

If you have picked an issue and are ready to contribute some code to resolve them:

- Ensure that an issue is opened for your feature or bug.

- Fork the [repository](https://github.com/hngi/jl-python-mycustomer) and clone it on your local system.

- Change into the directory of the cloned repository i.e `cd jl-python-mycustomer` then do the following before starting to work on your issue.

  ```bash
  git remote add upstream https://github.com/hngi/jl-python-mycustomer.git
  ```

  ```bash
  git pull upstream develop
  ```

- Create a branch with an explicit name (like `my-new-feature` or `issue-XX`) by 

  ```bash
  git checkout -b <my-chosen-feature>
  ```
- Install the required packages by
  ```bash
  pip install -r requirements.txt
  ```
- Do your work.

- Commit your changes. Ensure that your commit messages properly references the issue by following this style [guide](https://udacity.github.io/git-styleguide/)

  ```bash
  git add .
  git commit -m "<Commit Message>"
  ```

- rebase it on the develop branch from the official repository

  ```bash
  git pull --rebase upstream develop
  ```

- Push the changes in the new branch to your forked GitHub repository(assuming your branch is new_branch) i.e

  ```bash
  git push origin <new_branch>:<new_branch>
  ```

See you in Stage 5

### Running the Unittest Scripts
- Change into the 'test' directory in the 'jl-python-mycustomer' parent directory by carrying the following commands in the command line.
  ```cmd
  cd test\
  ```
  To run all tests together, use:
  ```cmd
  python -m unittest
  ```
  
  To run separately, if you so choose use the following
  - To run the Unittest scripts for the store endpoints, run the following:
    
    ```cmd
      python -m unittest test_store_endpoint.py
    ```
  - Now to run the Unittest scripts for the transaction endpoints, run the following:
    
    ```cmd
      python -m unittest test_transaction_endpoint.py
    ```
  - Now to run the Unittest scripts for the user endpoints, run the following:
    
    ```cmd
      python -m unittest test_user_endpoint.py
    ```

  By the Senior Endpoints Testing Developer
