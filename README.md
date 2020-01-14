# Cacheing / Caching

This is a simple django app to demonstrate how to store items in a cache to speed up application response times.

The following caching engines have been configured:
1. Memcached
2. Redis

### How it works
When the application is loaded for the first time, the flag is loaded from the db and cached.

However, for subsequent times, to speed things up, only the cached value is returned.
If that value is ever updated, The Flag model sends a signal that is received and the cache is invalidated.
At this point, the very first request to the app will not find the key in the cache. A cache reload will be
forced.

Therefore we are only reading from the db when we really have to.

### Other configured services
- Database: Postgres
- Load Balancer: 
	1. Haproxy: Main app load balancer
	2. Nginx to serve static files
	3. Caching engines: memcached, redis
- I'm using supervisor to run gunicorn to run the application

### Tests
- ```my_app/tests.py```


FYI: The credentials in ```devops/secrets/compose.env``` and ```my_app/management/commands/customcreatesuperuser.py``` are all fake and are obviously not in use anywhere