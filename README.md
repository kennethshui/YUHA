# YUHA Website Editing Guide

This repository contains the static HTML and image files for the YUHA website: https://yuhafinance.com. Follow this guide to make, preview, and submit website updates safely.

## 1. Set up the website locally

Install the following tools:

- [Git](https://git-scm.com/downloads)
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)
- Access to this repository on GitHub

Clone the repository and open it in VS Code:

```bash
git clone <repository-url>
cd <repository-folder>
code .
```

If the `code` command is unavailable, open VS Code, select **File > Open Folder**, and choose the repository folder.

Before starting an update, make sure `main` is current and create a separate branch:

```bash
git switch main
git pull origin main
git switch -c update/short-description
```

Replace `short-description` with a brief summary, such as `update/team-bios` or `add/new-speaker`.

## 2. Install a coding agent

You may use either Codex or Claude Code. Run the agent from the repository folder so it can inspect the existing website structure and styles.

### Option A: Codex CLI

On macOS or Linux, install Codex using the [official Codex CLI guide](https://learn.chatgpt.com/docs/codex/cli):

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Then open the repository folder in a terminal and start Codex:

```bash
codex
```

Sign in when prompted. Windows users should follow the platform-specific instructions in the official guide.

### Option B: Claude Code

Install a current Node.js LTS release, then follow the [official Claude Code setup guide](https://docs.anthropic.com/en/docs/claude-code/getting-started):

```bash
npm install -g @anthropic-ai/claude-code
```

Start Claude Code from the repository folder:

```bash
claude
```

Sign in when prompted. Do not use `sudo` with the npm installation command.

When requesting an edit, identify the page, provide the exact text or image, and ask the agent to preserve the existing layout and styling. Always review the resulting file changes yourself.

## 3. Preview changes locally

Install the [Live Server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) by Ritwick Dey in VS Code:

1. Open the **Extensions** panel.
2. Search for `Live Server` by Ritwick Dey.
3. Select **Install**.
4. Open the HTML page you changed, such as `index.html`, `the-team.html`, or `speakers.html`.
5. Click **Go Live** in the VS Code status bar.

The page will open at a local address such as `http://127.0.0.1:5500`. Save your files to refresh the preview.

Before submitting your work, check:

- The edited page at desktop and mobile widths.
- Navigation links and any links you changed.
- Image paths, image crops, spelling, and punctuation.
- Other pages that share the same navigation or layout.
- The browser console for errors.

## 4. Review and commit the changes

Review exactly what changed:

```bash
git status
git diff
```

Stage only the intended files, then commit them with a clear message:

```bash
git add <file-1> <file-2>
git commit -m "Describe the website update"
```

Avoid `git add .` unless you have checked every changed and untracked file.

## 5. Open a pull request into `main`

Push your feature branch, not `main`:

```bash
git push -u origin update/short-description
```

On GitHub:

1. Open the repository and select **Pull requests > New pull request**.
2. Set the base branch to `main`.
3. Set the compare branch to your feature branch.
4. Describe what changed and how you tested it locally.
5. Create the pull request and request a review.
6. After approval and any required checks, merge the pull request into `main`.
7. Delete the feature branch after the merge if it is no longer needed.

See GitHub's [pull request quickstart](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart) for additional details.

## Important: Do not modify `CNAME`

Do not edit, delete, rename, or replace the `CNAME` file. GitHub Pages uses this file to associate the deployed site with its custom domain. Changing or removing it can disconnect the website from its domain or interrupt access to the site.

If a task appears to require a `CNAME` change, stop and ask the website administrator before proceeding.
