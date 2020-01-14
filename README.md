# Sublime Text mypy stubs

## Install

Just clone it to wherever you like, example:

```
$ git clone https://github.com/gerardroche/sublime-mypy-stubs.git ~/sublime-mypy-stubs
```

Then in your Sublime Linter mypy settings set the `MYPYPATH` path.

Example:

    {
        "linters":
        {
            "mypy":
            {
                "env": {
                    "MYPYPATH": "~/sublime-mypy-stubs"
                }
                "args":
                [
                ],
                "disable": false,
                "excludes":
                [
                ],
                "executable": "~/.local/bin/mypy",
            }
        }
    }
