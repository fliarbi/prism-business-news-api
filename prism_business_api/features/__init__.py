"""features — one module per business endpoint family. Each takes the
authenticated Principal and validated BusinessFilters and returns an envelope
(or raises ApiError); routers.py owns the transport."""
from . import company, events, funding, headlines, sentiment, themes, trends  # noqa: F401
