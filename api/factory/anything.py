from api.services.anything import AnythingService


class AnythingFactory(AnythingService):

    def __init__(self, params=None, req=None):
        super().__init__(params=params, req=req)

    def post_payload(self, any_payload=None):
        self.req = any_payload
        return self

    def get_params(self, any_params=None):
        self.params = any_params
        return self
