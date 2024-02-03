# Git Commands Reference Guide

This guide provides basic commands for common Git operations

## 1. How to clone the code

```bash
git clone <repository-url>
```

## 2. How to Create a Branch

To create a new branch and switch to it 

```bash
git checkout -b <branch-name>
```

## 3. How to Stash changes

- **When to use:** Use *git stash* when you have uncommited changes in your working directory that you want to set aside temporariy. This is useful when you need to switch branches, pull in changes from the remote repository, or perform other operations wuthout commiting your changes.

- **How to Use:** 

    1. Suppose you are working on a feature branch and have some chnages but aren't ready to commit them.
        ```bash
        git stash
        ```
    2. Now you can switch to another branch or perform other Git operations.
        ```bash
        git checkout another-branch
        ```
    3. Once you are back on the original branch and ready to continue your work, you can apply the stashed changes
        ```bash
        git stash apply
        ```

## 3. How to add the files which needs to be commited

- **When to use:**

    1. **After making changes:** Whenever you make modifications to your project files, ypu can use *git add* to prepare these changes for the next commit. Staging your changes helps you organize and group related modifications together.

    2. **Before each commit**: As a best practice, it is recommended to stage your changes before every commit. This enables you to review and confirm the specific changes that will be included in the upcoming commit.

- **How to use:**
    1. To Stage specific files for the next commit, specify the file names after *git add*. For example
        ```bash
        #Stage a single file
        git add file1.txt

        #Stage multiple files
        git add file1.txt file2.txt
        ```

    2. Stage all changes in your working directory using a period *('.')* as follows
        ```bash
        git add .
        ```

    3. Checking the staging status
        ```bash
        git status
        ```

## 4. How to commit

To commit changes to your repository:

```bash
git commit -m "Commit message"
```
## 5. How to Push

To push changes to a remote repository 

```bash
git push origin <branch-name>
```
## 6. How to pull

To pull the latest changes from the remote repository

```bash
git pull origin <branch-name>
```



    
