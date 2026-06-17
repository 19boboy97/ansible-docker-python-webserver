# Kochbuchanleitung – Umgebung auf einem neuen Windows 11 Client starten

## Ziel

Mit dieser Anleitung kann das Projekt auf einem neuen Windows 11 Computer vollständig eingerichtet und gestartet werden.

Nach erfolgreicher Durchführung ist die Anwendung erreichbar unter:

```text
http://localhost:8080
```

---

# Voraussetzungen

Folgende Software muss installiert sein:

| Software           | Zweck                            |
| ------------------ | -------------------------------- |
| Git                | Repository herunterladen         |
| VirtualBox         | Virtualisierung                  |
| Vagrant            | Erstellung und Verwaltung der VM |
| Internetverbindung | Download von Ubuntu und Paketen  |

---

# 1. Repository herunterladen

PowerShell öffnen.

In ein gewünschtes Verzeichnis wechseln:

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

# 2. Projekt aktualisieren

Vor jedem Start sollte geprüft werden, ob neue Änderungen im Repository vorhanden sind.

Neueste Version von GitHub herunterladen:

```powershell
git pull
```

Dadurch werden alle aktuellen Änderungen übernommen.

---

# 3. Virtuelle Maschine erstellen oder starten

VM starten:

```powershell
vagrant up
```

Beim ersten Start werden automatisch:

* Ubuntu 22.04 heruntergeladen
* Die virtuelle Maschine erstellt
* Die VM gestartet

Dieser Schritt kann mehrere Minuten dauern.

---

# 4. Verbindung zur VM herstellen

```powershell
vagrant ssh
```

Nach erfolgreicher Anmeldung erscheint:

```text
vagrant@ansible-webserver:~$
```

---

# 5. Ansible prüfen

Kontrolle:

```bash
ansible --version
```

Wenn eine Versionsnummer angezeigt wird, ist Ansible installiert.

Falls Ansible nicht installiert ist:

```bash
sudo apt update
sudo apt install -y ansible
```

Danach erneut prüfen:

```bash
ansible --version
```

---

# 6. Zum Playbook wechseln

```bash
cd /vagrant/ansible/playbooks
```

---

# 7. Ansible Playbook ausführen

Playbook starten:

```bash
ANSIBLE_ROLES_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml
```

Das Playbook führt automatisch folgende Aufgaben aus:

* Docker installieren
* Docker-Dienst starten
* Docker-Netzwerk erstellen
* Python Docker-Image erstellen
* Python-Container starten
* Nginx-Container starten

---

# 8. Container prüfen

Laufende Container anzeigen:

```bash
sudo docker ps
```

Erwartetes Ergebnis:

```text
python-app
nginx-proxy
```

Beide Container müssen den Status **Up** besitzen.

---

# 9. Anwendung testen

Auf dem Windows-Host einen Browser öffnen.

Adresse aufrufen:

```text
http://localhost:8080
```

Erwartetes Ergebnis:

```text
Python Webserver läuft
Diese Seite wird vom Python-Backend ausgeliefert.
Der Zugriff erfolgt über Nginx als Reverse Proxy.
```

---

# 10. Projekt stoppen

VM stoppen:

```powershell
vagrant halt
```

---

# 11. Projekt erneut starten

VM starten:

```powershell
vagrant up
```

Verbindung herstellen:

```powershell
vagrant ssh
```

Falls Änderungen am Ansible-Code vorgenommen wurden:

```bash
cd /vagrant/ansible/playbooks

ANSIBLE_ROLES_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml
```

---

# 12. Umgebung vollständig neu erstellen

Falls die Umgebung komplett neu aufgebaut werden soll:

VM löschen:

```powershell
vagrant destroy -f
```

Danach erneut erstellen:

```powershell
vagrant up
```

Anschliessend:

```powershell
vagrant ssh
```

Und erneut das Playbook ausführen.

---

# Troubleshooting

## Repository existiert bereits

Fehlermeldung:

```text
destination path already exists
```

Lösung:

```powershell
Remove-Item -Recurse -Force ansible-docker-python-webserver
```

Danach erneut:

```powershell
git clone https://github.com/19boboy97/ansible-docker-python-webserver.git
```

---

## Ansible nicht installiert

Installation:

```bash
sudo apt update
sudo apt install -y ansible
```

---

## Docker läuft nicht

Status prüfen:

```bash
sudo systemctl status docker
```

Docker starten:

```bash
sudo systemctl start docker
```

---

## Container fehlen

Playbook erneut ausführen:

```bash
cd /vagrant/ansible/playbooks

ANSIBLE_ROLES_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml
```

---

## Port 8080 bereits belegt

Falls Port 8080 bereits verwendet wird, muss die Portweiterleitung im Vagrantfile angepasst werden.

Beispiel:

```ruby
config.vm.network "forwarded_port", guest: 8080, host: 8081
```

Danach ist die Anwendung erreichbar unter:

```text
http://localhost:8081
```

---

# Ergebnis

Nach erfolgreicher Durchführung dieser Anleitung läuft folgende Umgebung:

```text
Windows 11
│
├── VirtualBox
│
└── Ubuntu VM
    │
    ├── Ansible
    │
    └── Docker
        │
        ├── Nginx Reverse Proxy
        │
        └── Python Webserver
```

Die Anwendung ist anschliessend erreichbar unter:

```text
http://localhost:8080
```
