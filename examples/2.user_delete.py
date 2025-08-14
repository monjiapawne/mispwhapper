"""
Bulk delete users by ID
In this example users 57-125 will be deleted.
"""
from mispwhapper import MISPClient

api = MISPClient(
    baseurl    = "https://misp.local",
    api_key    = "APIKEY",
)

method = "post"
for i in range(57,125):
    endpoint = f"admin/users/delete/{i}"
    response = api.call(method, endpoint)
