from pytest import mark

from api.factory.anything import AnythingFactory


class TestGetAnything:

    @mark.api
    def test_get_anything(self):
        resp = AnythingFactory().get_params().get_anything("value").resp
        assert resp.headers["content-type"] == "application/json"
