import requests

from api.constants.http import StatusCode, HttpMethod
from api.constants.path import Path


class AnythingService(requests.Session):

    def __init__(self, params=None, req=None, resp=None):
        super().__init__()
        self.params = params
        self.req = req
        self.resp = resp

    def send_request(self, method, url, headers=None, params=None, payload=None, expected_code=None):
        self.headers["Accept-Language"] = "application/json"
        self.resp = self.request(method, f"https://{url}",  headers=headers, params=params, json=payload)
        if expected_code:
            assert expected_code == self.resp.status_code
        return self.resp

    def post_anything(self, expected_code=StatusCode.OK):
        self.resp = self.send_request(
            method=HttpMethod.POST,
            payload=self.req,
            url=Path.ANYTHING,
            expected_code=expected_code
        )
        return self

    def get_anything(self, value, expected_code=StatusCode.OK):
        self.resp = self.send_request(
            method=HttpMethod.GET,
            params=self.params,
            url=f"{Path.ANYTHING}/{value}",
            expected_code=expected_code
        )
        return self
