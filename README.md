# Automatisierte Bereitstellung eines Webservers mit Ansible

## Projektbeschreibung

Dieses Projekt demonstriert die automatisierte Bereitstellung einer Webserver-Umgebung mittels Ansible.

Die Infrastruktur wird mit Vagrant und VirtualBox erstellt. Anschliessend installiert Ansible Docker und startet zwei Container:

- Nginx als Reverse Proxy
- Python Webserver als Backend

## Architektur

Browser
→ Nginx
→ Python Webserver

## Technologien

- Vagrant
- Ubuntu Server
- Ansible
- Docker
- Nginx
- Python

## Repository Struktur

ansible/
app/
nginx/
docs/

## Status

Projekt in Entwicklung.