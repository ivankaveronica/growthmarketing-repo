## Tools Installed
- **Cursor IDE** — AI-powered code editor
- **Claude Code extension** — installed and logged in via Cursor Extensions
- **Codex extension** — installed and logged in via Cursor Extensions
- **Git** — installed via Xcode Command Line Tools after resolving macOS compatibility issues

## Steps Completed
1. Created a public GitHub repository
2. Downloaded and installed Cursor IDE
3. Installed Claude Code and Codex extensions inside Cursor
4. Cloned the GitHub repository into Cursor using `git clone` via the terminal
5. Opened the repository in Cursor

## Issues I Ran Into & How I Solved Them

### 1. No prior experience with GitHub or Cursor
I had never used GitHub, Cursor, or any developer tools before this task. I searched YouTube for tutorials on "how to create a GitHub repository" and "how to install Cursor extensions" to get started from scratch.

### 2. Git was not installed on my Mac
When I ran `git clone`, the terminal returned an error saying developer tools were missing. I tried `xcode-select --install` but kept getting: *"Can't install the software because it is not currently available from the Software Update server."*

### 3. Homebrew also failed
I attempted to install Git through Homebrew as an alternative, but it failed midway because it also depended on the same missing Xcode tools.

### 4. Root cause identified through AI-assisted troubleshooting
I had a back-and-forth conversation with Claude to diagnose the problem. Through that process, we identified that my macOS (Tahoe 26.0) was outdated and Apple's server was rejecting the download. Claude suggested updating macOS first — I updated to **Tahoe 26.5** via System Settings → Software Update.

### 5. Resolution
After the update, `xcode-select --install` worked successfully. Git was installed and `git clone` ran without errors.

## Reflection
This task pushed me well outside my comfort zone. I came in with zero experience in GitHub, Cursor, or terminal commands. By combining YouTube tutorials, AI assistance, and a willingness to keep trying after repeated failures, I was able to complete the full setup independently. The process took several hours but built real problem-solving confidence with developer tools.