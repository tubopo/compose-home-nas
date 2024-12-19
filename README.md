# compose-home-nas 💿

> Docker compose to use with home NAS Setup.

## Applications

| Application                                   | Image                                                                         | Description                                                                                                                                                                                                                 |
| --------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [jellyfin](https://jellyfin.org/)             | [linuxserver/jellyfin](https://hub.docker.com/r/linuxserver/jellyfin)         | Media server designed to organize, manage, and share digital media files to networked devices                                                                                                                               |
| [gitea](https://about.gitea.com/)             | [gitea/gitea](https://hub.docker.com/r/gitea/gitea)                           | Gitea is a self-hosted platform for teams and developers to create, manage, and deploy code repositories, code reviews, and CI/CD workflows.                                                                                |
| [transmission](https://transmissionbt.com)    | [linuxserver/transmission](https://hub.docker.com/r/linuxserver/transmission) | Bittorrent client with a complete web UI                                                                                                                                                                                    |
| [sonarr](https://sonarr.tv/)                  | [linuxserver/sonarr](https://hub.docker.com/r/linuxserver/sonarr)             | Sonarr is a PVR for Usenet and BitTorrent users.                                                                                                                                                                            |
| [jackett](https://github.com/Jackett/Jackett) | [linuxserver/jackett](https://hub.docker.com/r/linuxserver/jackett)           | Works as a proxy server: it translates queries from apps (Sonarr, SickRage, CouchPotato, Mylar, etc) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. |
| [prowlarr](https://prowlarr.com/)             | [linuxserver/prowlarr](https://hub.docker.com/r/linuxserver/prowlarr)         | Prowlarr provides a web interface and API for searching trackers/indexers and automatically managing the results.                                                                                                           |
| [prometheus](https://prometheus.io/)          | [prom/prometheus](https://hub.docker.com/r/prom/prometheus)                   | Systems monitoring and alerting.                                                                                                                                                                                      |
| [grafana](https://grafana.com/)               | [grafana/grafana](https://hub.docker.com/r/grafana/grafana/tags)              | Observability/visualization tool.                                                                                                                                                                                             |

## Environment Variables

| Variable                   | Default      | Description                                                  |
| -------------------------- | ------------ | ------------------------------------------------------------ |
| USER_ID                    | `1000`       | ID of the user to use in Docker containers                   |
| GROUP_ID                   | `1000`       | ID of the user group to use in Docker containers             |
| TIMEZONE                   | `Etc/UTC`    | TimeZone used by the container.                              |
| MNT_DATA                   | `/mnt/data0` | Host location of the data files                              |
| HOSTNAME                   | `localhost`  | Hostname of the NAS, could be a local IP or a domain name    |
| MNT_METRIC_DATA            | `/mnt/data1` | Host location of the metrics data - differ from main storage |
| METRIC_RETENTION_DAYS      | `31d`        | Storing metric data no longer then n days                    |
| GF_SECURITY_ADMIN_PASSWORD | `Password`   | Admin password for the graphana setup                        |

## File Structure

```txt
MNT_DATA
├──Torrents
│    ├──downloads
│    └──watch
├──Configs
│     ├──Jellyfin
│     ├──Transmission
│     ├──Gitea
│     ├──Prometheus
│     ├──Grafana
│     ├──Sonarr
│     ├──Jakett
│     └──Prowlarr
├──TV
├──Movies
├──Photos
└──Music

MNT_METRIC_DATA
├──Grafana
└──Prometheus
```
