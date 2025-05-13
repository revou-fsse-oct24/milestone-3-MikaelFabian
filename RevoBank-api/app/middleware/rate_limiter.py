# app/middleware/rate_limiter.py
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def setup_rate_limiter(app):
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=[
            "100 per day",
            "30 per hour"
        ]
    )
    
    # Custom rate limits for sensitive endpoints
    limiter.limit("5 per minute")(
        app.view_functions['user_routes.register']
    )
    
    return limiter