from mispwhapper import MISPClient

api = MISPClient(
    baseurl    = "https://misp.local",
    api_key    = "APIKEY",
)

method = "get"
endpoint = "/organisations"
api.run(method, endpoint)
