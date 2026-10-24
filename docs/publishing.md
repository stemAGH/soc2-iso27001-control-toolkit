# Publish the prepared repository

Repository: [stemAGH/soc2-iso27001-control-toolkit](https://github.com/stemAGH/soc2-iso27001-control-toolkit).
The owner approved public visibility. Repository creation used the signed-in browser; uploads use the GitHub
connector as stemAGH. The local CLI uses a different account, so confirm the login before attempting future pushes.

Run the following PowerShell commands from this project folder. Python 3.10+ is needed for validation.
If python is a Windows Store alias, use an installed interpreter; this session used the bundled runtime.

```powershell
python scripts/validate.py
python -m unittest discover -s tests -v
git status --short --branch
git log -1 --oneline
gh auth login --hostname github.com
gh auth status
gh api user --jq .login
git remote -v
git push -u origin main
gh repo view --json url --jq .url
```

Confirm that the reported login is stemAGH before pushing. For a fresh checkout, use
`git clone https://github.com/stemAGH/soc2-iso27001-control-toolkit.git`.
For an existing local copy, inspect its remote and fetch the current history before integrating changes.
The original local commit and connector-created remote history may differ; preserve both and do not force-push.

If a local commit was not created because your Git identity was unavailable, set an appropriate identity for this
repository, review the diff, run `git add .` and `git commit -m "Build SOC 2 and ISO 27001 control toolkit"` before publishing.
You can set a verified GitHub noreply address using `git config user.email` if desired; do not use invented identity details.

Alternatively create an empty repository through GitHub with no README, license or initial commit. In PowerShell:

```powershell
$toolkitRemote = Read-Host 'Paste the HTTPS URL of your new empty repository'
git remote add origin $toolkitRemote
git remote -v
git ls-remote origin
git push -u origin main
```

If `git ls-remote` shows existing branches, fetch and inspect them before reconciling; do not force-push.
If origin already exists, inspect it and stop before changing its URL. Never embed tokens in remote URLs.
After a successful push, confirm the branch and file list on GitHub, and include that verified URL in your interview notes.
GitHub Actions is included for subsequent pushes; a local check does not establish that remote CI has run.

If you downloaded the source ZIP, extract it first. The ZIP excludes Git history, so initialize and commit before
the create/push commands: `git init -b main`, then `git add .` and
`git commit -m "Build SOC 2 and ISO 27001 control toolkit"`. Review your Git author identity before committing.
