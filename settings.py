
# ALL CONFIGS RELATED TO CACHING

CACHE_CONFIG = {
    "DEBUG": True,
    "CACHE_TYPE": 'simple',
    "CACHE_DEFAULT_TIMEOUT": 20
}

# ALL CONFIGS RELATED TO CROSS-ORIGIN

CORS_RESOURCES = {
    '/api/each/*': {
        'origins': ['http://127.0.0.1:5600', 'http://127.0.0.1:5500'], # LIST OF DOMAINS WHICH CAN TAKE DATA FROM THIS PARTICULARLY URL. ex: you can test using different ports.
        'max_age': 1
    },
    '/api/all/*': {
        'origins': ['http://127.0.0.1:5600', '*'], # LIST OF DOMAINS WHICH CAN TAKE DATA FROM THIS PARTICULARLY URL. ex: you can test using different ports.
        'max_age': 1
    }
}
