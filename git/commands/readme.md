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
    2. Now you can switch to another branch or perform other Git operations.\
    ```
    git checkout another-branch
    ```
    3. Once you are back on the original branch and ready to continue your work, you can apply yhe stashed changes
    ```
    git stach apply
    ```

## 3. How to add the files which needs to be commited

    
