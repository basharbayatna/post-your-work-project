>**Note**: Please **fork** this Udacity repository so you have a **remote** repository in **your** GitHub account. Then you can clone the remote repository to your local machine. Later, as a part of the project, you will push your changes to the remote repository in your GitHub account.


# Project Title

Describe what your project is about and what it does

## Information about how to use your project

This could include:

- Step-by-step instructions for installing or setting up your project.
- Any software dependencies that need to be installed.
- Instructions and examples for how to use your project, including any helpful code snippets.
- Common issues and troubleshooting tips

## Contribution guidelines

If you welcome contributions, provide guidelines on how others can contribute to your project.

## Credits

It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.

## Date created

Include the date you created this project and README file.

---

**Project Assignment Steps**

This repository includes a small starter project for the Udacity "Post Your Work" Git project. Follow the steps below to complete the assignment and prepare your submission.

- **Files added locally (already present in this repo):**
	- `bikeshare.py` — example Python script (code file)
	- `new_york_city.csv` — sample data file (excluded by `.gitignore`)
	- `.gitignore` — ignores the CSV data file and Python caches

**Quick usage**

Run the simple script locally to see it handle the CSV (it will warn if the CSV is not present):

```bash
python3 bikeshare.py
```

**Suggested Git workflow and commands**

Replace `<your-username>` and `<repo>` with your GitHub username and repository name when needed. Use `main` or `master` depending on your repository default branch.

1) Fork the template repository on GitHub and clone your fork:

```bash
# clone your fork to local machine
git clone git@github.com:<your-username>/<repo>.git
cd <repo>
```

2) Create the files locally (if you haven't already) and initialize a Git repo (if starting from scratch):

```bash
# create files (already done in this repo as an example)
touch bikeshare.py new_york_city.csv .gitignore
echo "new_york_city.csv" > .gitignore

# if you created a new repo locally (not necessary if you cloned a fork):
git init
git add .
git commit -m "Initial commit: add bikeshare starter files"
```

3) Create and switch to the `documentation` branch to add README documentation and comments:

```bash
git checkout -b documentation
# edit README.md and add comments to bikeshare.py
git add README.md bikeshare.py
git commit -m "Docs: improve README and code comments"
git push -u origin documentation
```

4) Create the `refactor` branch to change the code (make at least 3 commits here):

```bash
git checkout main            # or `master` if your default branch is master
git checkout -b refactor
# make small code changes, then repeat add/commit at least 3 times
git add bikeshare.py
git commit -m "Refactor: update helper functions (1 of 3)"
# repeat two more meaningful commits
git commit -am "Refactor: improve loading and summary (2 of 3)"
git commit -am "Refactor: misc cleanup (3 of 3)"
git push -u origin refactor
```

5) Merge both branches into `main` (locally), resolve any conflicts, and push:

```bash
git checkout main
git merge documentation --no-ff -m "Merge documentation branch"
git merge refactor --no-ff -m "Merge refactor branch"
git push origin main
```

6) Provide the Git commands you used in the submission template (copy/paste the commands above into the template table rows). Download the template as a PDF after filling in the commands, and submit it via the Udacity classroom along with the URL of your public GitHub repository.

**Submission checklist**

- Copy and paste the Git commands you executed into the Git Commands Documentation template.
- Add your public GitHub repository URL to the template (first box).
- Export the completed template to PDF and upload to the Project Submission page.

If you want, I can: create branches and commits here in the repo, or provide a ready-made list of commands you can copy into the template. Tell me which you'd prefer and whether your default branch on GitHub is `main` or `master`.