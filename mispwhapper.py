# mispwhapper.py  ───────────────────────────────────────────────
import requests, json, urllib3, logging
from http import HTTPStatus
urllib3.disable_warnings()

class MISPClient:
    def __init__(self, baseurl: str, api_key: str,
                 verify_ssl: bool = False,
                 raw: bool        = False,
                 pretty: bool     = True,
                 log_level: str   = "INFO"
                 ) -> None:

        # library parameters
        self.baseurl        = baseurl.rstrip("/") + "/"
        self.api_key        = api_key
        self.verify_ssl     = verify_ssl
        self.raw            = raw
        self.pretty         = pretty

        self.headers = {
            'Authorization': api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        logging.basicConfig(level=getattr(logging, log_level.upper()),
                            format='[%(levelname)s] %(message)s')
        
    def call(self, method: str, endpoint: str, data: dict = None) -> dict | None:
        method = method.lower()
        url = self.baseurl + endpoint.lstrip('/')
        
        logging.info(f"Drafted: {url} -> Method: {method}")
        
        try:
            r = requests.request(method, url, headers=self.headers, json=data, verify=self.verify_ssl)
            logging.info(f'Response: {r.status_code} {HTTPStatus(r.status_code).phrase}')
            self._output_response(r)
            
            try:
                return r.json()
            except ValueError:
                logging.error('Invalid JSON Response')
                return None
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None

    def _output_response(self, r) -> None:
        try:
            if self.raw:
                print(r.json())
            if self.pretty:
                print(json.dumps(r.json(), indent=4))
        except ValueError:
            print(r.text or '<no JSON body>')
