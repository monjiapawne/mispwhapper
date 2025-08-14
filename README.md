# mispwhapper
Simple wrapper for MISP API.

See MISP API Docs for info: [MISP API Docs](https://www.misp-project.org/openapi/)

# Arguments
```python
baseurl: str,                 # set target url, including schema            [required]
api_key: str,                 # api key, ideally point to env variable      [required]
verify_ssl: bool = False,     # false - accept self signed certifcates
raw: bool        = False,     # false - don't return the raw api response
pretty: bool     = True,      # true - return the formatted json response
log_level: str   = "INFO"     # set the logging level, headers are included
data: dict                    # provide a json dictionary for the api call  [dependant on api call]
```
