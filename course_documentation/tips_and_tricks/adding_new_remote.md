# Adding a new remote

One reason why you might want to add a new remote can be if you want to pull in code that a team member has on his or her fork.

Start by listing your existing remotes. It may look like this:

```bash
$ git remote -v

origin  https://github.com/<your_username>/intro-to-software-development (fetch)
origin  https://github.com/<your_username>/intro-to-software-development (push)
upstream        https://github.com/equinor/intro-to-software-development.git (fetch)
upstream        https://github.com/equinor/intro-to-software-development.git (push)
```

You can then add you team mate's fork as a remote by calling
```
$ git remote add <your_team_mates_username> https://github.com/<your_team_mates_username>/intro-to-software-development.git
```

The list of remotes should now look something like:
```bash
$ git remote -v

origin  https://github.com/<your_username>/intro-to-software-development (fetch)
origin  https://github.com/<your_username>/intro-to-software-development (push)
upstream        https://github.com/equinor/intro-to-software-development.git (fetch)
upstream        https://github.com/equinor/intro-to-software-development.git (push)
<your_team_mates_username>        https://github.com/<your_team_mates_username> /intro-to-software-development.git (fetch)
<your_team_mates_username>        https://github.com/<your_team_mates_username> /intro-to-software-development.git (push)
```

Run `git fetch` to get the references to your team mate's branches, and see them in your log with `git lg`, or list them with `git branch --all --verbose`.

Including their work / commits into one of your branch can be done in one of two ways (at least). In any case, start by going to your own branch with `git switch <your_branch_name>`.

Then,
A) Rebase your work on top of their branch with `git rebase <your_team_mates_username>/<your_team_mates_branch_namee>`

or
B) Cherry-pick commit(s) by pointing to the commit hash(es) with `git cherry-pick <commit_hash>`
