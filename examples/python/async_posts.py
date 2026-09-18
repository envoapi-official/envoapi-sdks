import asyncio
import os
from envoapi import AsyncEnvoAPI


async def main():
    async with AsyncEnvoAPI(
        base_url=os.environ.get("ENVOAPI_BASE_URL", "https://api.envoapi.com")
    ) as client:
        result = await client.profiles.get_posts(
            username=os.environ.get("ENVOAPI_USERNAME", "alice")
        )
        print(result.body.to_dict())


asyncio.run(main())
