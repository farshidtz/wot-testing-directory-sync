# wot-testing-directory-sync

Python script and Github Action workflows to sync [W3C WoT Testing](https://github.com/w3c/wot-testing) TDs with a public Thing Description Directory.

# Run
Dependencies: Python 3, `requests`
```bash
ENDPOINT=http://localhost:8081 AUTHORIZATION="<basic/bearer>" TTL=60 python sync.py
```

`AUTHORIZATION` and `TTL` are optional.

## Workflows
### 2020.09.Online
- [Event TDs](https://github.com/w3c/wot-testing/blob/master/events/2021.03.Online/TDs)
- [Github workflow](https://github.com/farshidtz/wot-testing-directory-sync/blob/master/.github/workflows/2021.03.Online.yml)

### 2020.09.Online (disabled)
- [Event TDs](https://github.com/w3c/wot-testing/blob/master/events/2020.09.Online/TDs)
- [Github workflow](https://github.com/farshidtz/wot-testing-directory-sync/blob/master/.github/workflows/2020.09.Online.yml)

### 2020.06.Online (disabled)
- [Event TDs](https://github.com/w3c/wot-testing/blob/master/events/2020.06.Online/TDs)
- [Github workflow](https://github.com/farshidtz/wot-testing-directory-sync/blob/master/.github/workflows/2020.06.Online.yml.disabled)
