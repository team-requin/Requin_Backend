from app.views.base import BaseResource

class Index(BaseResource):
    def get(self):
        return {
                'TESTKEY':'TESTVALUE'
               }, 200