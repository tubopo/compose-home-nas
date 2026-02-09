# compose-home-nas 💿

> Docker compose to use with home UGEEN NAS Setup.

## File Structure

```txt
.MEDIA_SHARE
└──media
  ├──downloads
  ├──tv
  └──movies

.CONFIG_ROOT
├──jellyfin
│  └──cache
├──transmission
├──sonarr
└──jakett

```
## Dns resolve

```mermaid
sequenceDiagram
    participant U as User Browser
    participant DNS as DNS Provider (Cloudflare)
    participant T as Traefik (Proxy)
    participant APP as App (Jellyfin/Other)
    participant CA as Certificate Authority (Let's Encrypt)

    Note over T, CA: 1. THE SSL CHALLENGE (DNS-01)
    T->>DNS: Sets "Proof of Ownership" TXT record via API
    CA->>DNS: Checks for the TXT record
    DNS-->>CA: Record verified
    CA->>T: Issues valid SSL Certificate

    Note over U, APP: 2. THE CONNECTION
    U->>DNS: "Where is my-app.custom-domain.com?"
    DNS-->>U: "It is at [Your-Private-IP]"
    U->>T: Requests page via HTTPS
    T->>APP: Forwards traffic to [Internal-Container-Port]
    APP-->>U: App loads securely
```
