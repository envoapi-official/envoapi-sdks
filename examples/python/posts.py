import os
from envoapi import EnvoAPI

with EnvoAPI(
    base_url=os.environ.get("ENVOAPI_BASE_URL", "https://api.envoapi.com")
) as client:
    result = client.profiles.get_posts(
        username=os.environ.get("ENVOAPI_USERNAME", "alice")
    )
    print(result.body.to_dict())
