\# Kochbuchanleitung – Projekt auf einem neuen Windows 11 Client starten



\## Ziel



Mit dieser Anleitung kann das Projekt auf einem anderen Windows 11 Computer vollständig neu gestartet werden.



Nach Abschluss der Schritte ist die Anwendung über folgende Adresse erreichbar:



```text

http://localhost:8080

```



\---



\# Voraussetzungen



Folgende Software muss installiert sein:



| Software           | Zweck                           |

| ------------------ | ------------------------------- |

| Git                | Repository herunterladen        |

| VirtualBox         | Virtualisierung                 |

| Vagrant            | Erstellung der Ubuntu-VM        |

| Internetverbindung | Download von Ubuntu und Paketen |



\---



\# 1. Repository herunterladen



PowerShell öffnen und ein Verzeichnis auswählen:



```powershell

cd D:\\Github

```



Repository klonen:



```powershell

git clone https://github.com/19boboy97/ansible-docker-python-webserver.git

```



In das Projekt wechseln:



```powershell

cd ansible-docker-python-webserver

```



\---



\# 2. Virtuelle Maschine erstellen



VM starten:



```powershell

vagrant up

```



Beim ersten Start werden automatisch:



\* Ubuntu 22.04 heruntergeladen

\* Die virtuelle Maschine erstellt

\* Die VM gestartet



Dieser Schritt kann mehrere Minuten dauern.



\---



\# 3. Verbindung zur VM herstellen



```powershell

vagrant ssh

```



Nach erfolgreicher Verbindung erscheint eine Linux-Konsole:



```text

vagrant@ansible-webserver:\~$

```



\---



\# 4. Ansible installieren



Paketlisten aktualisieren:



```bash

sudo apt update

```



Ansible installieren:



```bash

sudo apt install -y ansible

```



Kontrolle:



```bash

ansible --version

```



\---



\# 5. Zum Playbook wechseln



```bash

cd /vagrant/ansible/playbooks

```



\---



\# 6. Ansible Playbook ausführen



Playbook starten:



```bash

ANSIBLE\_ROLES\_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml

```



Ansible führt nun automatisch folgende Aufgaben aus:



\* Docker installieren

\* Docker-Dienst starten

\* Docker-Netzwerk erstellen

\* Python Docker-Image erstellen

\* Python-Container starten

\* Nginx-Container starten



\---



\# 7. Kontrolle der Container



Laufende Container anzeigen:



```bash

sudo docker ps

```



Erwartetes Ergebnis:



```text

python-app

nginx-proxy

```



Beide Container müssen den Status "Up" besitzen.



\---



\# 8. Anwendung testen



Webbrowser auf dem Windows-Host öffnen.



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



\---



\# 9. Projekt stoppen



VM stoppen:



```powershell

vagrant halt

```



\---



\# 10. Projekt erneut starten



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



ANSIBLE\_ROLES\_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml

```



\---



\# Troubleshooting



\## Port 8080 bereits belegt



Prüfen, ob bereits ein Dienst auf Port 8080 läuft.



Alternativ die Portweiterleitung im Vagrantfile anpassen.



\---



\## Docker läuft nicht



Status prüfen:



```bash

sudo systemctl status docker

```



Docker starten:



```bash

sudo systemctl start docker

```



\---



\## Container fehlen



Playbook erneut ausführen:



```bash

ANSIBLE\_ROLES\_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml

```



\---



\# Ergebnis



Nach erfolgreicher Durchführung dieser Anleitung steht die komplette Umgebung automatisch zur Verfügung:



\* Ubuntu VM

\* Ansible

\* Docker

\* Docker Netzwerk

\* Nginx Reverse Proxy

\* Python Webserver



Die Anwendung ist anschliessend über



```text

http://localhost:8080

```



erreichbar.



