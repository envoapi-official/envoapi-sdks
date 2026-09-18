"""EnvoAPI Python SDK. Generated resource bindings; see runtime for transport policy."""
import httpx as _httpx
from .runtime import APIError, DecodeError, TransportError, Response
from .runtime import SyncTransport, AsyncTransport
from . import resources
from ._generated import models
from ._generated.types import UNSET, Unset

class EnvoAPI(SyncTransport):
    def __init__(self, *, api_key: str | None = None, base_url: str = 'https://api.envoapi.com',
                 timeout: float | _httpx.Timeout = 60.0, transport: _httpx.BaseTransport | None = None):
        super().__init__(api_key=api_key, base_url=base_url, timeout=timeout, transport=transport)
        self.profiles = resources.Profiles(self)
        self.companies = resources.Companies(self)
        self.schools = resources.Schools(self)
        self.search = resources.Search(self)
        self.jobs = resources.Jobs(self)
        self.posts = resources.Posts(self)

class AsyncEnvoAPI(AsyncTransport):
    def __init__(self, *, api_key: str | None = None, base_url: str = 'https://api.envoapi.com',
                 timeout: float | _httpx.Timeout = 60.0, transport: _httpx.AsyncBaseTransport | None = None):
        super().__init__(api_key=api_key, base_url=base_url, timeout=timeout, transport=transport)
        self.profiles = resources.AsyncProfiles(self)
        self.companies = resources.AsyncCompanies(self)
        self.schools = resources.AsyncSchools(self)
        self.search = resources.AsyncSearch(self)
        self.jobs = resources.AsyncJobs(self)
        self.posts = resources.AsyncPosts(self)
