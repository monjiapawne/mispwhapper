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
method = "post"
endpoint = "admin/users/add"
data = {
    "email": "simple2@man",
    "org_id":"1",
    "server_id":"0",
    "password":"test",
}
response = api.call(method, endpoint, data)