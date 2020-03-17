from pytest import mark

from api.factory.anything import AnythingFactory


class TestPostAnything:

    @mark.api
    def test_post_anything(self):
        resp = AnythingFactory().post_payload().post_anything().resp
        assert resp.headers["content-type"] == "application/json"
