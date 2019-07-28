from requests.sessions import Session
from test_interface.orther.base_requests import Base_Requests


class Login_Api(Base_Requests):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ss = Session()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass
