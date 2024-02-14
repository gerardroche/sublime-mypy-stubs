# Sublime Text mypy stubs

## Install

Just clone it to wherever you like, example:

```
$ git clone https://github.com/gerardroche/sublime-mypy-stubs.git ~/sublime-mypy-stubs
```

## Running mypy

To run mypy for a package using the stubs, either CD into package directory:

```
MYPYPATH="$HOME/sublime-mypy-stubs:../../Packages" python3 -m mypy --show-error-codes ../PackageName
```

Or if the package was installed via Package Control, rather than cloned directory into the Packages directory, CD into the Packages directory:

```
MYPYPATH="$HOME/sublime-mypy-stubs:../../Packages" python3 -m mypy --show-error-codes -p PackageName
```

Bash function

```sh
mypysubl() {
    MYPYPATH="$HOME/sublime-mypy-stubs:../../Packages" python3 -m mypy --show-error-codes $@
}
```

With this bash function you can run `mypysubl ../PackageName` or `mypysubl -p PackageName`.

## SublimeLinter

In your Sublime Linter mypy settings set the `MYPYPATH` path.

```json
{
    "linters": {
        "mypy": {
            "env": {
                "MYPYPATH": "~/sublime-mypy-stubs"
            },
            "args": [],
            "disable": false,
            "excludes": [],
            "executable": "~/.local/bin/mypy",
        }
    }
}
```
