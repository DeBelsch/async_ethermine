
from aiohttp import ClientSession, ClientResponse
from .models import *



class Request:
    """Class to make requests."""

    def __init__(self, websession: ClientSession):
        """Initialize the request."""
        self.websession = websession
        self.host = "https://api.ethermine.org"

    async def get_data(self, path: str) -> ClientResponse:
        """Make a request."""
        return await self.websession.request("get", f"{self.host}/{path}")


class EthermineAPI:
    """Class to communicate with the Ethermine API."""

    def __init__(self, auth: Request):
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def async_get_basic_pool_statistics(self) -> Basicpoolstatistics:
        """Return the basic pool statistics."""
        resp = await self.auth.get_data("poolStats")
        resp.raise_for_status()
        return Basicpoolstatistics(await resp.json())

    async def async_get_mined_blocks_history(self) -> Minedblockshistory:
        """Return the mined blocks statistics."""
        resp = await self.auth.get_data("blocks/history")
        resp.raise_for_status()
        return Minedblockshistory(await resp.json())

    async def async_get_network_stats(self) -> Networkstatistics:
        """Return the Network statistics."""
        resp = await self.auth.get_data("networkStats")
        resp.raise_for_status()
        return Networkstatistics(await resp.json())

    async def async_get_server_hashrate_history(self) -> Serverhashratehistory:
        """Return the server hashrate statistics."""
        resp = await self.auth.get_data("servers/history")
        resp.raise_for_status()
        return Serverhashratehistory(await resp.json())

    async def async_get_miner_dashboard_data(self, mineraddress:str) -> Minerdashboard:
        """Return the Miner's dashboard data"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/dashboard")
        resp.raise_for_status()
        return Minerdashboard(await resp.json())

    async def async_get_miner_history(self, mineraddress:str) -> Minerhistory:
        """Return the Miner's history"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/history")
        resp.raise_for_status()
        return Minerhistory(await resp.json())

    async def async_get_payouts(self, mineraddress:str) -> Payouts:
        """Return the payouts"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/payouts")
        resp.raise_for_status()
        return Payouts(await resp.json())

    async def async_get_rounds(self, mineraddress:str) -> Rounds:
        """Return the rounds"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/rounds")
        resp.raise_for_status()
        return Rounds(await resp.json())

    async def async_get_settings(self, mineraddress:str) -> Settings:
        """Return the settings of the miner"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/settings")
        resp.raise_for_status()
        return Settings(await resp.json())

    async def async_get_miner_currentstats(self, mineraddress:str) -> Minercurrentstatistics:
        """Return the current Statistics of the miner"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/currentStats")
        resp.raise_for_status()
        return Minercurrentstatistics(await resp.json())

    async def async_get_workers(self, mineraddress:str) -> Workers:
        """Return the Workers of the miner"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/workers")
        resp.raise_for_status()
        return Workers(await resp.json())

    async def async_get_worker_history(self, mineraddress:str, worker:str) -> Workerhistory:
        """Return the history of the worker"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/worker/" + worker + "/history")
        resp.raise_for_status()
        return Workerhistory(await resp.json())

    async def async_get_worker_currentstats(self, mineraddress:str, worker:str) -> Workercurrentstatistics:
        """Return the current statistics of the worker"""
        resp = await self.auth.get_data("miner/" + mineraddress + "/worker/" + worker + "/currentStats")
        resp.raise_for_status()
        return Workercurrentstatistics(await resp.json())