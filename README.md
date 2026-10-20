# Exercise 4 — Docker Compose

## Aim
Run a web service and Redis using Docker Compose.

## Run
```bash
docker compose up --build
```
Open `http://localhost:5000`. In another terminal, run `docker compose down` to stop and remove the containers.

## Expected result
The app returns JSON with the Redis ping status. Redis is available to the app on the internal Compose network; it is not published to the host.

## Verify output
Run `docker compose ps` and `curl http://localhost:5000`; check that the response reports the Redis ping status.

## Troubleshooting
If the app starts before Redis is ready, inspect `docker compose logs` and retry after services are healthy. Confirm the app uses the Compose service name for Redis rather than `localhost`.
