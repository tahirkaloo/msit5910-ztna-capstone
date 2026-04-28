# MSIT 5910 Capstone: ZTNA & IAM Framework

## Project Overview
This repository contains the Infrastructure-as-Code (IaC) and configuration files for a centralized Zero-Trust Network Access (ZTNA) and Identity and Access Management (IAM) framework. It is designed to secure decentralized, containerized homelab and SME environments (specifically Proxmox/Docker setups) while eliminating reliance on legacy VPNs.

## Core Architecture
* **Hypervisor:** Proxmox VE
* **Identity Provider (IdP):** Authentik
* **Zero-Trust Ingress:** Twingate / Cloudflare ZTNA
* **Target Applications:** NetBox, Portainer

## Key Features
* **VPN Replacement:** Utilizes outbound ZTNA tunnels to expose internal services securely without opening inbound firewall ports.
* **Deterministic OIDC Mapping:** Custom Python property mappings in Authentik ensure immutable UUIDs are passed to applications like NetBox, completely mitigating the risk of duplicate user creation during SSO handshakes.

## Deployment Instructions
1. Clone this repository to your Docker host.
2. Navigate to the `/docker` directory.
3. Rename the `.env.example` files to `.env` and populate your secure database passwords and secret keys.
4. Run `docker-compose -f authentik-compose.yml up -d` to spin up the IdP.
5. Apply the custom OIDC mappings from the `/configs` directory within the Authentik admin dashboard.