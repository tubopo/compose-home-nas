# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Docker Compose stack for a UGreen NAS: media automation, photo management, Git hosting, camera surveillance, note sync. All services sit behind Traefik with automatic Let's Encrypt SSL via Cloudflare DNS-01.

## Commands

### Validate a service compose file

```bash
docker compose -f <service>/docker-compose.yaml --env-file .env config
```

### CI validation (runs on every push)

The GitHub Actions workflow (`.github/workflows/build.yml`) validates compose configs for: traefik, arr, gitea, immich, gotify. It copies `.env.dev` to `.env`, generates dummy secrets in `./secrets/`, then runs `docker compose config` for each.

### Start/stop a service

```bash
docker compose -f <service>/docker-compose.yaml --env-file .env up -d
docker compose -f <service>/docker-compose.yaml --env-file .env down
```

## Architecture

### Network

All services share a single external bridge network `restricted_wan` (subnet `172.20.30.0/24`) with static IPs. Databases use separate internal bridge networks (`internal_db`, `internal_immich`) so they are not exposed to the wider network.

### Service Directories

Each service directory contains its own `docker-compose.yaml` and optionally a `.env` file with service-specific variables. The root `.env` provides shared variables (paths, domain, user/group IDs, timezone). `.env.dev` is a template for CI and new deployments.

| Directory | Services | Key IPs |
|-----------|----------|---------|
| `traefik/` | Reverse proxy, SSL termination | .10 |
| `arr/` | Sonarr, Radarr, Prowlarr, Seerr, Jackett, QBittorrent, Jellyfin, Gluetun VPN, FlareSolverr | .20-.66, .90 |
| `gitea/` | Gitea + PostgreSQL | .70 |
| `immich/` | Immich server + ML + PostgreSQL + Redis | .80 |
| `frigate/` | Frigate NVR | .31 |
| `obsidian-sync/` | CouchDB-based Obsidian sync | .25 |

### VPN Routing

Gluetun (Private Internet Access) provides a VPN gateway. Radarr and Seerr use `network_mode: "service:gluetun"` to route all traffic through the VPN. Traefik labels for VPN-routed services are placed on the Gluetun container.

### Secrets

Docker secrets are loaded from files in the `${SECRETS}` directory. Required secret files: `cf_dns_api_token`, `cf_api_email`, `traefik_basic_auth`, `pia_user`, `pia_pass`, `pg_user`, `pg_pas`, `gitea_key`, `gitea_token`.

### Compose Conventions

- **YAML anchors** for logging: all services reference `*default-logging` (json-file, 10m max, 3 files, compressed).
- **Resource limits**: every service has `deploy.resources.limits` for memory and CPU.
- **Health checks**: services include health checks with proper intervals, timeouts, and retries.
- **Security**: `security_opt: [no-new-privileges:true]` on all containers.
- **Traefik labels**: standard pattern using `traefik.http.routers.<svc>.rule=Host(...)` with `tls.certresolver=cloudflare` and `entrypoints=websecure`.
- **GPU access**: Jellyfin, Immich, Ollama, and Frigate mount `/dev/dri/*` for Intel GPU hardware acceleration.

### Environment Variables (root .env)

| Variable | Purpose |
|----------|---------|
| `CONFIG_ROOT` | Base path for persistent service configs |
| `MEDIA_SHARE` | Media storage mount |
| `SECRETS` | Directory containing Docker secret files |
| `DOMAIN` | Base domain for Traefik routing (`<service>.${DOMAIN}`) |
| `USER_ID` / `GROUP_ID` | Container UID/GID mapping |
| `TIMEZONE` | Timezone for all containers |
