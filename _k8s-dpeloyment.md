# k8s checklist / components

## Cluster setup

### RKE2

#### Set up three nodes with public

- Set up master and ETCD MASTER node
- Set up two worker nodes

### DNS loadbalancing

- Either set A-records for all IPs in domain provider
- Or set up all IPs in TD DNS server to point to all node ips

## Storage

- Install Rancher Longhorn storage Class
- Storage backup to ????

## Database

- Store images into mongodb as BSON

### Set up mongodb

- replicaCount : 3
- storageClass : longhorn
- rootpassword : password
- rootUsername : root

## Frontend

- Set TLS temination on ingress level

### Prefix

- If prefix: Set up prefix for frontend
- set PUBLIC_URL in .env to prefix

## Backend

- PVC,PV for mounted storage
- ETCD distributed locks
- Fix TLS termination on ingress level
- Access mongodb RS service through secret with root password

## TLS

- Cluster-issuer
- secret

## CI/CD

- ArgoCD
- Create GitHub secret for ArgoCD
- ArgoCD on /argo-cd
- Version / Release hash as label on images to trigger helm from ArgoCD

## Monitoring

- Prometheus
- Grafana
