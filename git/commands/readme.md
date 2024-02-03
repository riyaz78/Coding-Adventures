# Git Commands Reference Guide

This guide provides basic commands for common Git operations, essential for effective version control and collaboration in software development projects.

## 1. Cloning the Code

To clone an existing repository:

```bash
git clone <repository-url>
```

## 2. Creating a Branch

To create a new branch and switch to it 

```bash
git checkout -b <branch-name>
```

**Why**: Branches are used to work on new features and bug fixes in isolation from the main project.

## 3. Stashing Changes

- **When to use:** Use *git stash* when you have uncommited changes in your working directory that you want to set aside temporariy. This is useful when you need to switch branches, pull in changes from the remote repository, or perform other operations without commiting your changes.

- **How to Use:** 

    1. Stash changes:
        ```bash
        git stash
        ```
    2. Switch branches:
        ```bash
        git checkout another-branch
        ```
    3. Apply Stashed changes:
        ```bash
        git stash apply
        ```
- **Managing Stashes:**

    1. View stashes:
        ```bash
        git stash list
        ```
    2. Remove a stash:
        ```
        git stash drop
        ```

## 3. Adding files to be commited

- **When to use:** After modifications, stage your changes to prepare for a commit.

- **How to use:**
    1. Stage specific files:
        ```bash
        #Stage a single file
        git add file1.txt

        #Stage multiple files
        git add file1.txt file2.txt
        ```

    2. Stage all changes:
        ```bash
        git add .
        ```

    3. Check status:
        ```bash
        git status
        ```

## 4. Commiting Changes

To commit staged changes

```bash
git commit -m "Commit message"
```
**Best Practice:** Write clear, meaningful commit messages

## 5. Pushing changes

To push changes to the remote repository 

```bash
git push origin <branch-name>
```
**Role in Collaboration":** Pushing shares your commits with the team and updates the remote repository

## 6. Pulling Changes

To pull the latest changes from the remote repository

```bash
git pull origin <branch-name>
```
**Insight:** *git pull* combines *git fetch* followed by *git merge* .

## Additional Common Commands

- **Merging Branches:** *git merge <branch-name>* to combine branch changes
- **Fetching Branches:** *git fetch origin* to download remote updates
- **Viewing Commit History:** *git log* for a history of commits

## Troubleshooting 

- **Undoing Changes:** Use *git reset* to unstage changes or *git revert* to undo commited changes.
- **Common Issues:** For resolving merge conflicts, use *git mergetool*.

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - Comprehensive guide to Git
- [Official Git Documentation](https://git-scm.com/doc) - For in-depth understanding and additional commands

## Conclusion

This guide covers the basics of Git operations. For more complex scenarios, refer to the additional resources provided. Happy Coding!



    
