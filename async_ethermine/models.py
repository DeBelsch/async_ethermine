

class Basicpoolstatistics:
    """Class that represents the basic pool Statistics in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Basicpoolstatistics object."""
        self.raw_data = raw_data


    @property
    def data(self) -> dict:
        """Return the data of the poolstats"""
        return self.raw_data["data"]

    @property
    def topMiners(self) -> list:
        """Returns a list of the top Miners"""
        return self.data["topMiners"]

    @property
    def minedBlocks(self) -> list:
        """Returns a list of the last mined blocks"""
        return self.data["minedBlocks"]

    @property
    def poolStats(self) -> dict:
        """Returns an object with General pool stats"""
        return self.data["poolStats"]

    @property
    def price(self) -> dict:
        """Returns an object with Price informations"""
        return self.data["price"]



class Minedblockshistory:
    """Class that represents the mined Blocks history in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a minedblockshistory object."""
        self.raw_data = raw_data


    @property
    def data(self) -> dict:
        """Return the data of the Mined Blocks Statistics"""
        return self.raw_data["data"]

    @property
    def minedBlocks(self) -> list:
        """Returns a list of blocks recently mined in the pool"""
        return self.data["minedBlocks"]



class Networkstatistics:
    """Class that represents the Network Statistics of the pool in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Networkstatistics object."""
        self.raw_data = raw_data


    @property
    def data(self) -> dict:
        """Return the data of the Network statistics"""
        return self.raw_data["data"]

    @property
    def time(self) -> int:
        """Returns the unix timestamp of the statistic entry"""
        return self.data["time"]

    @property
    def blockTime(self) -> float:
        """Returns the current block time of the network"""
        return self.data["blockTime"]

    @property
    def difficulty(self) -> int:
        """Returns the current difficulty of the network"""
        return self.data["difficulty"]

    @property
    def hashrate(self) -> int:
        """Returns the current hashrate of the network in H/s"""
        return self.data["hashrate"]

    @property
    def usd(self) -> float:
        """Returns the current price in USD"""
        return self.data["usd"]

    @property
    def btc(self) -> float:
        """Returns the current price in BTC"""
        return self.data["btc"]



class Serverhashratehistory:
    """Class that represents the Server Hashrate history in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Serverhashratestatistics object."""
        self.raw_data = raw_data


    @property
    def data(self) -> list:
        """Return a list of server hashrate ordered by time ASC"""
        return self.raw_data["data"]



class Minerdashboard:
    """Class that represents the Miner's dashboard data in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Minerdashboard object."""
        self.raw_data = raw_data
        

    @property
    def data(self) -> dict:
        """Return the data of the Miner's dashboard"""
        return self.raw_data["data"]

    @property
    def statistics(self) -> list:
        """Returns a list of the miner statistics"""
        return self.data["statistics"]

    @property
    def workers(self) -> list:
        """Returns a list of the workers"""
        return self.data["workers"]

    @property
    def currentStatistics(self) -> dict:
        """Returns the current miner statistics"""
        return self.data["currentStatistics"]

    @property
    def settings(self) -> dict:
        """Returns the miner settings"""
        return self.data["settings"]



class Minerhistory:
    """Class that represents the Miner's history in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Minerhistory object."""
        self.raw_data = raw_data
        

    @property
    def data(self) -> list:
        """Returns a list with the history of the miner"""
        return self.raw_data["data"]



class Payouts:
    """Class that represents the payouts in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Payouts object."""
        self.raw_data = raw_data


    @property
    def data(self) -> list:
        """Returns a list with the payouts"""
        return self.raw_data["data"]



class Rounds:
    """Class that represents the Rounds in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Rounds object."""
        self.raw_data = raw_data


    @property
    def data(self) -> list:
        """Returns a list with the rounds"""
        return self.raw_data["data"]



class Settings:
    """Class that represents the settings in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Settings object."""
        self.raw_data = raw_data


    @property
    def data(self) -> dict:
        """Returns a list with the rounds"""
        return self.raw_data["data"]

    @property
    def email(self) -> str:
        """Returns the masked email of the miner"""
        return self.data["email"]

    @property
    def monitor(self) -> int:
        """Returns if Monitoring is enabled (1 for yes, 0 for no)"""
        return self.data["monitor"]

    @property
    def minPayout(self) -> int:
        """Returns the Minimum payout amount defined by the miner in base units"""
        return self.data["minPayout"]

    @property
    def ip(self) -> str:
        """Returns the Masked IP address of one randomly selected worker"""
        return self.data["ip"]



class Minercurrentstatistics:
    """Class that represents the current statistics of the miner in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a MinercurrentStâts object."""
        self.raw_data = raw_data


    @property
    def data(self) -> dict:
        """Returns the data of the current Statistics"""
        return self.raw_data["data"]

    @property
    def time(self) -> int:
        """Returns the 	Unix timestamp of the statistic entry"""
        return self.data["time"]

    @property
    def lastSeen(self) -> int:
        """Returns the Unix timestamp of when the miner was last seen by the pool"""
        return self.data["lastSeen"]

    @property
    def reportedHashratet(self) -> float:
        """Returns the Reported hashrate of the miner in H/s"""
        return self.data["reportedHashrate"]

    @property
    def averageHashrate(self) -> float:
        """Returns the average hashrate of the miner in H/s during the last 24h"""
        return self.data["averageHashrate"]

    @property
    def currentHashrate(self) -> float:
        """Returns the current hashrate of the miner in H/s"""
        return self.data["currentHashrate"]

    @property
    def validShares(self) -> int:
        """Returns the number of valid shares submitted during the last hour."""
        return self.data["validShares"]

    @property
    def invalidShares(self) -> int:
        """Returns the Number of invalid shares submitted during the last hour."""
        return self.data["invalidShares"]

    @property
    def staleShares(self) -> int:
        """Returns the Number of stale shares submitted during the last hour."""
        return self.data["staleShares"]

    @property
    def activeWorkers(self) -> int:
        """Returns the number of currently active workers of the miner"""
        return self.data["activeWorkers"]

    @property
    def unpaid(self) -> int:
        """Returns the number of the Unpaid Balance"""
        return self.data["unpaid"]

    @property
    def unconfirmed(self) -> int:
        """Returns the number of the Unconfirmed balance (in base units) of the miner"""
        return self.data["unconfirmed"]

    @property
    def coinsPerMin(self) -> float:
        """Returns the Estimated number of coins mined per minute (based on your average hashrate as well as the average block time and difficulty of the network over the last 24 hours.)"""
        return self.data["coinsPerMin"]

    @property
    def usdPerMin(self) -> float:
        """Returns the Estimated number of USD mined per minute (based on your average hashrate as well as the average block time and difficulty of the network over the last 24 hours.)"""
        return self.data["usdPerMin"]

    @property
    def btcPerMin(self) -> float:
        """Returns the Estimated number of BTC mined per minute (based on your average hashrate as well as the average block time and difficulty of the network over the last 24 hours.)"""
        return self.data["btcPerMin"]    


class Workers:
    """Class that represents the  workers of the miner in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Workers object."""
        self.raw_data = raw_data


    @property
    def data(self) -> list:
        """Returns a list of the workers of the miner"""
        return self.raw_data["data"]



class Workerhistory:
    """Class that represents the individual worker history in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a Workerhistory object."""
        self.raw_data = raw_data


    @property
    def data(self) -> list:
        """Returns a list of the worker's history"""
        return self.raw_data["data"]


class Workercurrentstatistics:
    """Class that represents the current statistics of the worker in the ethermine API."""

    def __init__(self, raw_data: dict):
        """Initialize a WorkercurrentStats object."""
        self.raw_data = raw_data


    @property
    def data(self) -> dict:
        """Returns the data of the worker's current Statistics"""
        return self.raw_data["data"]

    @property
    def time(self) -> int:
        """Returns the Unix timestamp of the statistic entry"""
        return self.data["time"]

    @property
    def lastSeen(self) -> int:
        """Returns the Unix timestamp of when the worker was last seen by the pool"""
        return self.data["lastSeen"]

    @property
    def reportedHashrate(self) -> float:
        """Returns the Reported hashrate of the worker in H/s"""
        return self.data["reportedHashrate"]

    @property
    def averageHashrate(self) -> float:
        """Returns the average hashrate of the worker in H/s during the last 24h"""
        return self.data["averageHashrate"]

    @property
    def currentHashrate(self) -> float:
        """Returns the current hashrate of the worker in H/s"""
        return self.data["currentHashrate"]

    @property
    def validShares(self) -> int:
        """Returns the number of valid shares submitted by the worker during the last hour."""
        return self.data["validShares"]

    @property
    def invalidShares(self) -> int:
        """Returns the number of invalid shares submitted by the worker during the last hour."""
        return self.data["invalidShares"]

    @property
    def staleShares(self) -> int:
        """Returns the number of stale shares submitted by the worker during the last hour."""
        return self.data["staleShares"]