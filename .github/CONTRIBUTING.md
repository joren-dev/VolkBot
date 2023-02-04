# Contributing

## 1. Creating a fork of the VolkBot repository
You first need to create a fork of the [VolkBot](https://github.com/joren-dev/VolkBot) repository to commit your changes to it. Methods to fork a repository can be found in the [GitHub Documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Then add your fork as a local project (on your PC), pick one of the methods:

```sh
# Using HTTPS
git clone https://github.com/joren-dev/VolkBot.git

# Using SSH
git clone git@github.com:joren-dev/VolkBot.git
```

> [Which remote URL should be used ?](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)

Then, go to your local folder. And open your terminal in that folder, [GitBash](https://gitforwindows.org/) is recommended for windows.

```sh
cd VolkBot
```

Add git remote controls, pick one of the methods:

```sh
# Using HTTPS
git remote add fork https://github.com/YOUR-USERNAME/VolkBot.git
git remote add upstream https://github.com/joren-dev/VolkBot.git


# Using SSH
git remote add fork git@github.com:YOUR-USERNAME/VolkBot.git
git remote add upstream git@github.com/joren-dev/VolkBot.git
```

You can now verify that you have your two git remotes:

```sh
git remote -v
```

## Setup Project
1. Follow all the [Prerequisites](https://github.com/joren-dev/VolkBot/blob/main/README.md#prerequisites)
2. Open terminal inside project again.
3. Create local pipenv: `pipenv install`.
4. Activate it with: `pipenv shell` after getting the dependencies.
5. Open folder DeVolk folder inside your Text Editor of choice and press "Select/Choose interpreter".
6. On windows navigate to: `C:\Users\xxxx\.virtualenvs\` and find the `volk_bot-xxxxxxxx` folder.
7. Select the `volk_bot-xxxxxxxx\Scripts\python.exe` as interpreter.


## Receive remote updates
In view of staying up to date with the central repository:

```sh
git pull upstream master
```

## Choose a base branch
Before starting development, you need to know which branch to base your modifications/additions on. When in doubt, use dev.

| Type of change                |           | Branches              |
| :------------------           |:---------:| ---------------------:|
| Documentation                 |           | `dev`                 |
| Bug fixes                     |           | `dev`                 |
| New features                  |           | `dev`                 |

```sh
# Switch to the desired branch
git switch dev

# Pull down any upstream changes
git pull

# Create a new branch to work on. Name the branch to the issue, feature or documentation you're about to write.
git switch --create branch_name
```

Commit your changes, then push the branch to your fork with `git push -u fork` and open a pull request on [the VolkBot repository](https://github.com/joren-dev/VolkBot/) following the template provided.