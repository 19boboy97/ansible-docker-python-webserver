# Automatisierte Bereitstellung einer Webanwendung mit Ansible, Docker, Nginx und Python

## Projektbeschreibung

Dieses Projekt zeigt die automatisierte Bereitstellung einer Webserver-Umgebung mit Vagrant, Ansible und Docker.

Beim ersten Start wird automatisch:

- eine Ubuntu-22.04-VM erstellt
- Ansible installiert
- Docker installiert
- ein Python-Webserver gestartet
- ein Nginx Reverse Proxy gestartet
- ein SSH-Server eingerichtet
- der Public Key des Dozenten hinterlegt

Die komplette Umgebung wird nach dem Prinzip **Infrastructure as Code** bereitgestellt.

---

## Verwendete Technologien

- Windows 11
- VirtualBox
- Vagrant
- Ubuntu 22.04 LTS
- Ansible
- Docker
- Python
- Nginx
- Git
- GitHub

---

## Architektur

![Architektur der Umgebung](images/ArchitekturDerUmgebung.png)

---

## Schnellstart

Repository herunterladen:

```powershell
git clone https://github.com/19boboy97/ansible-docker-python-webserver.git
cd ansible-docker-python-webserver
```

Virtuelle Maschine erstellen:

```powershell
vagrant up
```

Verbindung zur VM:

```powershell
vagrant ssh
```

Container prüfen:

```bash
sudo docker ps
```

Webseite öffnen:

```text
http://localhost:8080
```

---

## Dokumentation

Die ausführliche Projektdokumentation befindet sich unter:

- `docs/Projektdokumentation.md`

Die Schritt-für-Schritt-Anleitung befindet sich unter:

- `docs/Kochbuchanleitung.md`

---

## Repository-Struktur

```text
ansible-docker-python-webserver
│
├── ansible/
├── app/
├── docs/
├── images/
├── nginx/
├── README.md
└── Vagrantfile
```

---

## Autor

Christian Abbühl

TEKO HF Systemtechnik