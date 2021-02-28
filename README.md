# async_ethermine

This package is an asynchronus Python library for the ethermine.org API.

# Installation

```python
pip install async_ethermine
```

# Usage
```python
import asyncio
import aiohttp

import async_ethermine

async def main():
    async with aiohttp.ClientSession() as session:
        api = EthermineAPI(Request(session))
        test = await api.async_get_workers("walletaddress")
        print(test.data)

asyncio.run(main())
```
