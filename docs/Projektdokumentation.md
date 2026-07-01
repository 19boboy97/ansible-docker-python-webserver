# Automatisierte Bereitstellung einer Webanwendung mit Ansible, Docker, Nginx und Python

## Inhaltsverzeichnis

1. Einleitung
2. Zielsetzung
3. Verwendete Technologien
4. Systemarchitektur
5. Projektstruktur
6. Erstellung der virtuellen Maschine
7. Ansible-Konfiguration
8. Ansible Playbook
9. Rolle "webserver"
10. Python-Webanwendung
11. Nginx Reverse Proxy
12. SSH-Zugriff
13. Ausführung des Projekts
14. Funktionstest
15. Zielerreichung
16. GitHub Repository
17. Fazit
18. Quellen

---

# 1. Einleitung

Im Rahmen dieses Projekts wurde eine vollständig automatisierte Webserver-Umgebung erstellt.

Ziel war es, eine Ubuntu-Serverumgebung automatisiert bereitzustellen und anschliessend mittels Ansible zu konfigurieren. Als Anwendungsbeispiel wurde eine einfache Python-Webanwendung entwickelt, welche über einen Nginx Reverse Proxy veröffentlicht wird.

Die komplette Infrastruktur wird als Code beschrieben (Infrastructure as Code). Dadurch kann die gesamte Umgebung jederzeit reproduzierbar neu erstellt werden.

---

# 2. Zielsetzung

Ziel dieses Projekts ist die automatisierte Bereitstellung einer Webanwendung mithilfe moderner DevOps-Werkzeuge.

Anstatt einen Server manuell zu konfigurieren, soll die gesamte Infrastruktur automatisch aufgebaut werden.

## Funktionale Anforderungen

- Erstellung einer Ubuntu-VM mittels Vagrant
- Automatische Installation von Ansible
- Automatische Installation von Docker
- Erstellung eines Docker-Netzwerks
- Bereitstellung einer Python-Webanwendung
- Bereitstellung eines Nginx Reverse Proxy
- Veröffentlichung der Webseite über HTTP
- Automatische Einrichtung eines SSH-Servers
- Automatisches Hinterlegen des Public Keys des Dozenten

## Nicht-funktionale Anforderungen

- Vollständige Automatisierung
- Reproduzierbarkeit
- Infrastructure as Code
- Verwendung von Open-Source-Software
- Versionsverwaltung mittels Git
- Dokumentation der gesamten Umgebung

---

# 3. Verwendete Technologien

| Technologie | Zweck |
|-------------|------|
| Windows 11 | Hostsystem |
| VirtualBox | Virtualisierung |
| Vagrant | Erstellung der virtuellen Maschine |
| Ubuntu 22.04 LTS | Serversystem |
| Ansible | Konfigurationsmanagement |
| Docker | Containerisierung |
| Nginx | Reverse Proxy |
| Python | Webanwendung |
| Git | Versionsverwaltung |
| GitHub | Codeverwaltung |

---

# 4. Systemarchitektur

Die Architektur besteht aus mehreren Komponenten.

Der Entwickler arbeitet auf einem Windows-11-Computer.

Vagrant erstellt automatisch eine Ubuntu-VM innerhalb von VirtualBox.

Während der Bereitstellung installiert Vagrant automatisch Ansible.

Anschliessend führt Ansible das Playbook aus.

Dieses installiert Docker und erstellt automatisch zwei Container:

- Python-Webserver
- Nginx Reverse Proxy

Der Benutzer verbindet sich ausschliesslich mit Nginx.

Nginx leitet sämtliche HTTP-Anfragen intern an den Python-Webserver weiter.

Zusätzlich wird ein SSH-Server eingerichtet, damit sich der Dozent direkt auf die virtuelle Maschine verbinden kann.

## Architektur

![Architektur der Umgebung](../images/ArchitekturDerUmgebung.png)

---

# 5. Projektstruktur

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

Alle Projektdateien befinden sich innerhalb eines GitHub-Repositories.

Dadurch kann das Projekt jederzeit erneut heruntergeladen und auf einem anderen Rechner gestartet werden.

---

# 6. Erstellung der virtuellen Maschine

Die virtuelle Maschine wird mit Vagrant erstellt.

Zum Start genügt folgender Befehl:

```powershell
vagrant up
```

Beim ersten Start werden automatisch:

- Ubuntu 22.04 heruntergeladen
- die virtuelle Maschine erstellt
- Ansible installiert
- das Ansible-Playbook ausgeführt

Der Entwickler muss keine manuellen Installationsschritte innerhalb der VM durchführen.

---

# 7. Ansible-Konfiguration

Für die Automatisierung wird Ansible verwendet.

Die Installation erfolgt automatisch durch Vagrant.

Das eigentliche Konfigurationsmanagement übernimmt anschliessend ein Playbook.

Die Rollen befinden sich im Verzeichnis:

```text
ansible/roles
```

Das Playbook befindet sich unter:

```text
ansible/playbooks/site.yml
```

Das Playbook ruft die Rolle **webserver** auf und führt sämtliche Installationsschritte automatisch aus.

---

# 8. Ansible Playbook

Das zentrale Playbook befindet sich unter:

```text
ansible/playbooks/site.yml
```

Das Playbook ruft die Rolle **webserver** auf.

Beispiel:

```yaml
---
- hosts: localhost
  become: yes

  roles:
    - webserver
```

Dadurch werden sämtliche Installations- und Konfigurationsschritte automatisch ausgeführt.

---

# 9. Rolle "webserver"

Die Rolle **webserver** übernimmt die vollständige Konfiguration der Ubuntu-VM.

Folgende Aufgaben werden automatisch ausgeführt:

1. Installation des OpenSSH-Servers
2. Start und Aktivierung des SSH-Dienstes
3. Hinterlegen des Public Keys des Dozenten
4. Installation von Docker
5. Start des Docker-Dienstes
6. Erstellung eines Docker-Netzwerks
7. Erstellen des Python-Docker-Images
8. Start des Python-Containers
9. Start des Nginx-Containers

Durch diese Automatisierung ist keine manuelle Konfiguration des Servers mehr notwendig.

---

# 10. Python-Webanwendung

Als Beispielanwendung wurde ein einfacher Webserver mit Python erstellt.

Die Anwendung lauscht auf Port **5000** und liefert eine HTML-Seite aus.

Die Python-Anwendung läuft innerhalb eines Docker-Containers.

Der Container ist ausschliesslich über das interne Docker-Netzwerk erreichbar.

Ein direkter Zugriff von aussen ist nicht vorgesehen.

---

# 11. Nginx Reverse Proxy

Vor dem Python-Webserver befindet sich ein Nginx Reverse Proxy.

Der Benutzer verbindet sich ausschliesslich mit Nginx.

Nginx nimmt die HTTP-Anfragen entgegen und leitet sie an den Python-Webserver weiter.

Die Kommunikation erfolgt über das Docker-Netzwerk.

Beispiel der Weiterleitung:

```nginx
location / {
    proxy_pass http://python-app:5000;
}
```

Dadurch bleibt die eigentliche Anwendung vom öffentlichen Zugriff getrennt.

---

# 12. SSH-Zugriff

Zusätzlich zur Webserver-Umgebung wurde ein SSH-Zugriff eingerichtet.

Ansible übernimmt automatisch folgende Aufgaben:

- Installation des OpenSSH-Servers
- Start des SSH-Dienstes
- Aktivierung beim Systemstart
- Hinterlegen des Public Keys des Dozenten

Dadurch kann sich der Dozent ohne Passwort auf die virtuelle Maschine verbinden.

Damit die VM direkt aus dem gemeinsamen WLAN erreichbar ist, wurde zusätzlich im Vagrantfile ein **public_network** konfiguriert.

Die VM erhält dadurch eine eigene IP-Adresse im Netzwerk.

Die aktuelle IP-Adresse kann mit folgendem Befehl angezeigt werden:

```bash
hostname -I
```

Beispiel:

```text
10.0.2.15 10.100.44.21 172.17.0.1 172.18.0.1
```

Der Zugriff erfolgt anschliessend beispielsweise mit:

```bash
ssh vagrant@10.100.44.21
```

Voraussetzung ist, dass der passende private Schlüssel zum hinterlegten Public Key verwendet wird.

---

# 13. Ausführung des Projekts

Die komplette Umgebung kann mit wenigen Befehlen gestartet werden.

Repository herunterladen:

```powershell
git clone https://github.com/19boboy97/ansible-docker-python-webserver.git
```

Ins Projekt wechseln:

```powershell
cd ansible-docker-python-webserver
```

Virtuelle Maschine starten:

```powershell
vagrant up
```

Nach erfolgreichem Start kann eine Verbindung zur VM hergestellt werden:

```powershell
vagrant ssh
```

Die laufenden Docker-Container können anschliessend überprüft werden:

```bash
sudo docker ps
```

Die Ausgabe zeigt den Python-Webserver sowie den Nginx Reverse Proxy.

---

# 14. Funktionstest

Nach erfolgreicher Ausführung des Projekts wurde die Umgebung getestet.

## Prüfung der laufenden Container

Mit folgendem Befehl können die laufenden Docker-Container angezeigt werden:

```bash
sudo docker ps
```

Es werden zwei Container ausgeführt:

- python-app
- nginx-proxy

Dadurch wird bestätigt, dass sowohl die Python-Webanwendung als auch der Nginx Reverse Proxy erfolgreich gestartet wurden.

## Prüfung des SSH-Zugriffs

Der SSH-Dienst kann mit folgendem Befehl überprüft werden:

```bash
sudo systemctl status ssh
```

Die Ausgabe zeigt, dass der Dienst aktiv ist.

Anschliessend wurde überprüft, ob der Public Key des Dozenten korrekt hinterlegt wurde:

```bash
cat ~/.ssh/authorized_keys
```

Dabei wurde sowohl der Standard-Schlüssel des Benutzers **vagrant** als auch der Public Key des Dozenten angezeigt.

## Prüfung der Webseite

Die Webanwendung wurde anschliessend im Browser getestet.

Aufruf:

```text
http://localhost:8080
```

Die Webseite wurde erfolgreich angezeigt.

Damit konnte bestätigt werden, dass Nginx die HTTP-Anfragen korrekt an den Python-Webserver weiterleitet.

---

# 15. Zielerreichung

Alle definierten Projektziele konnten erfolgreich umgesetzt werden.

Folgende Anforderungen wurden erfüllt:

- Ubuntu-VM wird automatisch mit Vagrant erstellt
- Ansible wird automatisch installiert
- Docker wird automatisch installiert
- Docker-Netzwerk wird automatisch erstellt
- Python-Webanwendung wird automatisch bereitgestellt
- Nginx Reverse Proxy wird automatisch gestartet
- SSH-Server wird automatisch eingerichtet
- Public Key des Dozenten wird automatisch hinterlegt
- Die Umgebung ist vollständig reproduzierbar
- Sämtlicher Quellcode wird über Git und GitHub versioniert

Zusätzlich konnte das Projekt erfolgreich auf einem zweiten Windows-11-Rechner getestet werden.

Dadurch wurde bestätigt, dass die komplette Umgebung anhand der Dokumentation reproduzierbar aufgebaut werden kann.

---

# 16. GitHub Repository

Der vollständige Quellcode befindet sich in einem öffentlichen GitHub-Repository.

Repository: <https://github.com/19boboy97/ansible-docker-python-webserver>

Durch Git und GitHub werden sämtliche Änderungen nachvollziehbar dokumentiert.

Zusätzlich ermöglicht das Repository den einfachen Download sowie den erneuten Aufbau der kompletten Umgebung.

---

# 17. Fazit

Im Rahmen dieses Projekts wurde eine vollständig automatisierte Webserver-Umgebung entwickelt.

Durch den Einsatz von Vagrant, Ansible und Docker konnte der gesamte Bereitstellungsprozess automatisiert werden.

Anstelle einer manuellen Serverkonfiguration genügt heute der Befehl:

```powershell
vagrant up
```

Die virtuelle Maschine wird erstellt, Ansible installiert und das Playbook ausgeführt.

Dieses installiert Docker, richtet den SSH-Zugriff ein und startet automatisch die benötigten Container.

Die entwickelte Lösung ist reproduzierbar, einfach erweiterbar und entspricht dem Konzept **Infrastructure as Code**.

Das Projekt zeigt, wie moderne DevOps-Werkzeuge zusammenarbeiten und den Aufwand für die Bereitstellung von Servern und Anwendungen deutlich reduzieren können.

---

# 18. Quellen

- https://developer.hashicorp.com/vagrant
- https://www.virtualbox.org
- https://ubuntu.com
- https://www.ansible.com
- https://docs.ansible.com
- https://www.docker.com
- https://docs.docker.com
- https://nginx.org
- https://www.python.org
- https://git-scm.com
- https://github.com