# Kochbuchanleitung

## Automatisierte Bereitstellung einer Webanwendung mit Ansible, Docker, Nginx und Python

---

# Ziel

Mit dieser Anleitung kann das Projekt auf einem beliebigen Windows-11-Computer vollständig neu aufgebaut werden.

Nach Abschluss läuft:

- Ubuntu 22.04
- Docker
- Python-Webserver
- Nginx Reverse Proxy
- SSH-Server

Die komplette Konfiguration erfolgt automatisch über Vagrant und Ansible.

---

# Voraussetzungen

Folgende Software muss auf dem Windows-Computer installiert sein:

- Git
- VirtualBox
- Vagrant

---

# 1. Repository herunterladen

PowerShell öffnen.

In den gewünschten Ordner wechseln:

```powershell
cd C:\GithubRepo
```

Repository herunterladen:

```powershell
git clone https://github.com/19boboy97/ansible-docker-python-webserver.git
```

In das Projekt wechseln:

```powershell
cd ansible-docker-python-webserver
```

---

# 2. Projektstruktur kontrollieren

Die Projektstruktur sollte ungefähr wie folgt aussehen:

```text
ansible-docker-python-webserver
│
├── Vagrantfile
├── README.md
│
├── ansible
│   ├── inventory
│   ├── playbooks
│   └── roles
│
├── app
│   ├── app.py
│   └── Dockerfile
│
├── nginx
│   └── nginx.conf
│
├── docs
│   ├── Projektdokumentation.md
│   └── Kochbuchanleitung.md
│
└── images
    └── ArchitekturDerUmgebung.png
```

---

# 3. Virtuelle Maschine erstellen

Zum Erstellen der virtuellen Maschine genügt folgender Befehl:

```powershell
vagrant up
```

Beim **ersten Start** werden automatisch:

- Ubuntu 22.04 heruntergeladen
- die virtuelle Maschine erstellt
- die VM gestartet
- Ansible installiert
- das Ansible-Playbook ausgeführt
- Docker installiert
- der SSH-Server installiert
- der Docker-Dienst gestartet
- das Docker-Netzwerk erstellt
- das Python-Docker-Image erstellt
- der Python-Container gestartet
- der Nginx-Container gestartet
- der Public Key des Dozenten hinterlegt

Es sind keine manuellen Installationsschritte innerhalb der virtuellen Maschine notwendig.

Bei einem erneuten Aufruf von

```powershell
vagrant up
```

wird die bereits vorhandene virtuelle Maschine lediglich gestartet. Die Provisionierung wird dabei standardmässig **nicht erneut ausgeführt**.

Soll die komplette Konfiguration erneut angewendet werden, kann dies mit folgendem Befehl erfolgen:

```powershell
vagrant provision
```

Alternativ kann die virtuelle Maschine neu gestartet und gleichzeitig erneut provisioniert werden:

```powershell
vagrant reload --provision
```

Soll die virtuelle Maschine vollständig neu erstellt werden, kann sie zuerst gelöscht werden:

```powershell
vagrant destroy -f
```

Anschliessend wird sie erneut aufgebaut mit:

```powershell
vagrant up
```

---

# 4. Verbindung zur VM

Nach erfolgreichem Start:

```powershell
vagrant ssh
```

Nun befindet man sich auf der Ubuntu-VM.

---

# 5. Docker prüfen

Laufende Container anzeigen:

```bash
sudo docker ps
```

Erwartete Ausgabe:

- python-app
- nginx-proxy

---

# 6. SSH prüfen

SSH-Dienst kontrollieren:

```bash
sudo systemctl status ssh
```

Public Keys anzeigen:

```bash
cat ~/.ssh/authorized_keys
```

Der Public Key des Dozenten sollte dort vorhanden sein.

---

# 7. IP-Adresse der VM anzeigen

Die VM erhält durch das **public_network** zusätzlich eine eigene IP-Adresse im Netzwerk.

Anzeige:

```bash
hostname -I
```

Beispiel:

```text
10.0.2.15 10.100.44.21 172.17.0.1 172.18.0.1
```

Die relevante Adresse ist die WLAN-IP.

Im Beispiel:

```text
10.100.44.21
```

---

# 8. SSH-Zugriff für den Dozenten

Die aktuelle IP-Adresse der virtuellen Maschine kann jederzeit mit folgendem Befehl angezeigt werden:

```bash
hostname -I
```

Der Dozent kann sich anschliessend beispielsweise mit folgendem Befehl verbinden:

```bash
ssh vagrant@10.100.44.21
```

Voraussetzung:

- gleicher Netzwerkbereich
- passender privater Schlüssel zum hinterlegten Public Key

---

# 9. Webseite testen

Im Browser öffnen:

```text
http://localhost:8080
```

Die Python-Webanwendung sollte angezeigt werden.

---

# 10. VM stoppen

Virtuelle Maschine herunterfahren:

```powershell
vagrant halt
```

---

# 11. VM erneut starten

```powershell
vagrant up
```

---

# 12. VM löschen

Soll die VM vollständig entfernt werden:

```powershell
vagrant destroy -f
```

Danach kann sie jederzeit erneut erstellt werden:

```powershell
vagrant up
```

---

# 13. Repository aktualisieren

Änderungen übernehmen:

```powershell
git status
git add .
git commit -m "Beschreibung der Änderungen"
git push
```

---

# Ergebnis

Nach erfolgreicher Durchführung stehen automatisch folgende Komponenten bereit:

- Ubuntu 22.04 LTS
- Docker
- Python-Webserver
- Nginx Reverse Proxy
- Docker-Netzwerk
- SSH-Server
- SSH-Zugriff für den Dozenten
- GitHub-Repository
- Vollständig reproduzierbare Entwicklungsumgebung

Das Projekt kann dadurch jederzeit reproduzierbar auf einem neuen Windows-Computer aufgebaut werden. Dank der Automatisierung sind nur wenige Befehle erforderlich, um die komplette Umgebung bereitzustellen.