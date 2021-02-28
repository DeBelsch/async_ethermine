from aiohttp import ClientSession, ClientResponse

class Request:
    """Class to make requests."""

    def __init__(self, websession: ClientSession):
        """Initialize the.request."""
        self.websession = websession
        self.host = "https://api.ethermine.org"

    async def get_data(self, path: str) -> ClientResponse:
        """Make a request."""
        return await self.websession.request("get", f"{self.host}/{path}")
