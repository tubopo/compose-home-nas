# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Docker Compose stack for a UGreen NAS. All services behind Traefik with Let's Encrypt SSL via Cloudflare DNS-01.

## Commands

```bash
# Validate a service
docker compose -f <service>/docker-compose.yaml --env-file .env config

# Start/stop a service
docker compose -f <service>/docker-compose.yaml --env-file .env up -d
docker compose -f <service>/docker-compose.yaml --env-file .env down
```

CI (`.github/workflows/build.yml`) validates compose configs on every push using `.env.dev` and dummy secrets.

## Architecture

Single external bridge network `restricted_wan` (`172.20.30.0/24`, static IPs). Databases on separate internal networks.

Each directory has its own `docker-compose.yaml` and optional `.env`. Root `.env` has shared config; `.env.dev` is the CI/new-deploy template.

### Compose Conventions

- YAML anchors (`*default-logging`) for standardized json-file logging
- `deploy.resources.limits` on every service
- `security_opt: [no-new-privileges:true]` on all containers
- Traefik labels: `Host(...)` + `tls.certresolver=cloudflare` + `entrypoints=websecure`
- Secrets loaded from files in `${SECRETS}` directory
- VPN-routed services (Radarr, Seerr) use `network_mode: "service:gluetun"`; their Traefik labels go on the Gluetun container
