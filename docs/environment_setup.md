---
layout: default
nav_order: 2
---

# Environment setup
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Install the Python interpreter:

G-Cubed models require you have a working Python 3.10+ interpreter 
installed on the computer. It is necessary to use Python 3.10 or later versions
of the interpreter to ensure compatibility with the G-Cubed model implementation.

### Running commands at a command prompt

Throughout this documentation, you are instructed to run various text commands 
at a prompt.

The prompt is available in a variety of forms, depending on 
the computer's operating system.

#### Windows operating systems

For Windows computers, the command prompt is available from either the PowerShell 
or the command prompt software (cmd.exe).

- [How to access the command prompt](https://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/)

- [How to use the command prompt](https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/)

- [How to access the Powershell](https://www.howtogeek.com/662611/9-ways-to-open-powershell-in-windows-10/)

- [Powershell cheatsheet](https://www.comparitech.com/net-admin/powershell-cheat-sheet/)

#### MacOS operating systems

A prompt is accessible via the Terminal in MacOS. The Terminal enables commands to be run within a "shell". 
Different shells are available on MacOS but recent versions of MacOS default to using the Z-shell, `zsh`.

- [How to access the Terminal in MacOS](https://www.idownloadblog.com/2019/04/19/ways-open-terminal-mac/)

- [Terminal cheatsheet](https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/)
### Windows installation

Install Python 3.10+ on Windows from [the Python site](https://www.python.org/downloads/windows/).

### MacOS installation

If you do not have `homebrew` installed already, [follow these instructions](https://brew.sh/)
to install it.

Then, install the latest Python version using homebrew:

```
brew install python
```

### Python package management 
Python itself cannot do too much, it needs all kinds of packages for all kinds of purposes (including the newly developed gcubed package). Pip is widely used for managing Python's packages.

To install `pip`, please follow these instructions:

* [Pip official website for installation](https://packaging.python.org/en/latest/tutorials/installing-packages/)
* [Instructions for installing pip on Windows](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)  

G-Cubed has a number of packages that it depends on. These must be installed. They are:  

* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [scipy](https://scipy.org/)
* [regex](https://pypi.org/project/regex/)

However, they do not needed to be installed manually, when you install the gcubed package, 
`pip` will automatically check which packages are missing in your local environment and 
install them.

Thus, make sure pip is properly setup before you install the `gcubed` package.

## `gcubed` package installation

The first thing you need to do is to download 
[the binary gcubed package](../distributions/gcubed-*version*-py3-none-any.whl). 
It has a `whl` filename extension.

To install `gcubed`, run the following command in your terminal from within 
the directory containing the downloaded file:

```
pip install gcubed-*version*-py3-none-any.whl
```

The current `gcubed` version is 1.0.0 but new versions are released regularly. 
You will probably need to reinstall `gcubed` whenever there is a version update. 
Uninstall the old version of gcubed then install the newest version when you want 
to update `gcubed`.

To uninstall:

```
pip uninstall gcubed
```
