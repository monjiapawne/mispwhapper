from mispwhapper import MISPClient 

api = MISPClient(
    baseurl    = "https://misp.local",
    api_key    = "API_KEY_GOES_HERE",
    verify_ssl = False,
    silent     = False,
    raw        = False,
    pretty     = True,
    log_level  = "INFO"
)

#WIP
method = "get"
endpoint = "admin/users"
response = api.call(method, endpoint)