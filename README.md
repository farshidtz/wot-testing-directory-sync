# wot-testing-directory-sync

Python script and Github Action workflows to sync TDs with an instance of [LinkSmart Thing Directory](https://github.com/linksmart/thing-directory).

# Run
Dependencies: Python 3, `requests`
```bash
ENDPOINT=http://localhost:8081 AUTHORIZATION="<basic/bearer>" TTL=60 python sync.py
```

## Workflows
### 2020.09.Online
- [Github workflow](https://github.com/farshidtz/wot-testing-directory-sync/blob/master/.github/workflows/2020.09.Online.yml)

### 2020.06.Online (disabled)
- [Event TDs](https://github.com/w3c/wot-testing/blob/master/events/2020.06.Online/TDs)
- [Github workflow](https://github.com/farshidtz/wot-testing-directory-sync/blob/master/.github/workflows/2020.06.Online.yml.disabled)
