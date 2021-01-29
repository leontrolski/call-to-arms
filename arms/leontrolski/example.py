class ApiClient:
    def __init__(self, root_url: str, session_cls: sessionmaker):
        self.root_url = root_url
        self.session_cls = session_cls

    def construct_url(self, entity: str) -> str:
        return f"{self.root_url}/v1/{entity}"

    def get_items(self, entity: str) -> List[Item]:
        resp = requests.get(self.construct_url(entity))
        resp.raise_for_status()
        return [Item(**n) for n in resp.json()["items"]]

    def save_items(self, entity: str) -> None:
        with scoped_session(self.session_cls) as session:
            session.add(self.get_items(entity))


class ClientA(ApiClient):
    def construct_url(self, entity: str) -> str:
        return f"{self.root_url}/{entity}"


class ClientB(ApiClient):
    def construct_url(self, entity: str) -> str:
        return f"{self.root_url}/a/special/place/{entity}"


client_a = ClientA("https://client-a", session_cls)
client_a.save_items("bars")
