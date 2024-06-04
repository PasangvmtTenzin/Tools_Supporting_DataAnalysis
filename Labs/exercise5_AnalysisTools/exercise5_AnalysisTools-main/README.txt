 
GIT introduction
https://gitlab.uw.edu.pl/python-tools/git-laboratory https://gitlab.mimuw.edu.pl/python-tools/git-laboratory

Local work
git init – create an empty repository
git status – check the status of the repository
git add <paths> – add files to repository
git add -u – add updated files
git add -A – add all files
git rm <path> – remove files from repository
git rm --cached <paths> – remove files from the repository but keep a local copy.
git commit -m "<message>" – create a commit with the currently added files, with <message> as the commit description
git branch <name> – create a new branch with name <name>
git checkout <name> – change the current branch to the branch named <name>
git checkout -b <name> – create a new branch with name <name> and checkout to it (equivalent to the sequence of commands: git branch and git checkout)
git reset - revert changes locally
git revert – create a commit reverting the changes introduced by a given list of commits
git merge – create a commit that merges the contents of two branches
git rebase – take diverging commits from one branch and put them on top of the other one
git log – show the history of commits in the current branch
Exercise 1
Create a new repository in the directory sample_project. Add two commits with the following descriptions: "initial commit" and "first changes". The history of commits should look as follows:

commit 6a2cf1d03f2429573c0a8baa99fb54296998c5b6 (HEAD -> master)
Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
Date:   Fri Nov 6 16:09:41 2020 +0100

    first changes

commit ebc2cdb495c93951e6c33657ac6d38561ff1e3b2
Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
Date:   Fri Nov 6 16:09:20 2020 +0100

    inital commit
Exercise 2
Create two branches in the repository. Each should contain at least one commit not present in the other.

$ git log --graph --all
* commit 6b0a08d280a573835339e66271a36f815299a26c (HEAD -> develop)
| Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
| Date:   Fri Nov 6 16:23:12 2020 +0100
| 
|     begin develop branch
|   
| * commit 6a2cf1d03f2429573c0a8baa99fb54296998c5b6 (master)
|/  Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
|   Date:   Fri Nov 6 16:09:41 2020 +0100
|   
|       first changes
| 
* commit ebc2cdb495c93951e6c33657ac6d38561ff1e3b2
  Author: Grzegorz Bokota <grzegorz.bokota@students.mimuw.edu.pl>
  Date:   Fri Nov 6 16:09:20 2020 +0100

      inital commit
Command git log --graph --oneline --all is nice to use

Exercise 2.2
Create a repository with at least 3 commits. Create branch develop and reset master branch to the previous commit. Results should be similar to:

* 42b2f9e (develop) third commit
* baad3d7 (HEAD -> master) second commit
* 0183122 initial commit
Exercise 3
Make two distinct branches (A and B) in your repository. Modify the same line in the same file on both branches. Commit your changes. Try a git merge and a git rebase operation between these two branches. Observe the conflict and how it's handled in each case.

Remote work
git clone – clone a remote repository locally
git pull – pull changes from remote and update the local branch
git fetch – update information from the remote repository
git push – push changes to the remote repository
Exercise 4
Clone the https://gitlab.mimuw.edu.pl/python-tools/git-example-repo repository and compare the local version with the server one.

Exercise 5
Create an empty repository on https://gitlab.mimuw.edu.pl. Clone it locally, modify it and push the changes to the gitlab repository.

(information about ssh access configuration https://gitlab.mimuw.edu.pl/help/user/ssh.md)