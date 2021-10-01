# wot-testing-directory-sync

Python script and Github Action workflows to sync [W3C WoT Testing](https://github.com/w3c/wot-testing) TDs with a public Thing Description Directory.

# Run
Dependencies: Python 3, `requests`
```bash
ENDPOINT=http://localhost:8081 AUTHORIZATION="<basic/bearer>" TTL=60 python sync.py
```

`AUTHORIZATION` and `TTL` are optional.

## Github Action Workflows
See [.github/workflows](.github/workflows)
