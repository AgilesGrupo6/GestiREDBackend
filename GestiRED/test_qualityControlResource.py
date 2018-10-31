from unittest import TestCase


class TestQualityControlResource(TestCase):
    def test_get_user_rols(self):
        resp = self.api_client.get('/gestired/user/?rols=1', format='json')
        self.assertValidJSONResponse(resp)
