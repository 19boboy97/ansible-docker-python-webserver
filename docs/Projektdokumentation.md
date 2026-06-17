\# Automatisierte Bereitstellung einer Webanwendung mit Ansible, Docker, Nginx und Python



\## Inhaltsverzeichnis



1\. Einleitung

2\. Zielsetzung

3\. Verwendete Technologien

4\. Systemarchitektur

5\. Projektstruktur

6\. Erstellung der virtuellen Maschine

7\. Ansible-Konfiguration

8\. Ansible Playbook

9\. Rolle "webserver"

10\. Python-Webanwendung

11\. Nginx Reverse Proxy

12\. Ausführung des Playbooks

13\. Funktionstest

14\. Zielerreichung

15\. GitHub Repository

16\. Fazit

17\. Quellen



\---



\# 1. Einleitung



Im Rahmen dieses Projekts wurde eine automatisierte Webserver-Umgebung mit Vagrant, Ansible und Docker erstellt.



Ziel war es, eine virtuelle Ubuntu-Maschine automatisiert bereitzustellen und anschliessend mittels Ansible zu konfigurieren. Als Anwendungsbeispiel wurde eine einfache Python-Webanwendung implementiert, welche über einen Nginx Reverse Proxy erreichbar ist.



Die Umsetzung orientiert sich am Konzept "Infrastructure as Code", bei welchem Infrastruktur und Konfigurationen durch Code beschrieben und automatisiert bereitgestellt werden.



\---



\# 2. Zielsetzung



Ziel dieses Projekts ist die automatisierte Bereitstellung einer Webanwendung mithilfe von Ansible.



Hierzu soll eine virtuelle Ubuntu-Umgebung erstellt und vollständig automatisiert konfiguriert werden. Die Installation und Konfiguration der benötigten Software soll reproduzierbar und ohne manuelle Eingriffe erfolgen.



\## Funktionale Anforderungen



\- Erstellung einer virtuellen Ubuntu-Maschine mittels Vagrant

\- Installation und Konfiguration von Ansible

\- Automatische Installation von Docker über ein Ansible-Playbook

\- Automatischer Start des Docker-Dienstes

\- Bereitstellung eines Nginx-Webservers als Reverse Proxy

\- Bereitstellung eines Python-Webservers als Backend-Anwendung

\- Kommunikation zwischen Nginx und Python-Webserver über ein Docker-Netzwerk

\- Veröffentlichung des Dienstes über HTTP auf Port 8080

\- Sicherstellung der Erreichbarkeit der Anwendung über einen Browser



\## Nicht-funktionale Anforderungen



\- Vollständige Automatisierung der Installation

\- Reproduzierbarkeit der Umgebung

\- Dokumentation als Code (Infrastructure as Code)

\- Verwendung ausschliesslich von Open-Source-Technologien

\- Möglichkeit zur jederzeitigen Neuerstellung der Umgebung



\---



\# 3. Verwendete Technologien



| Technologie | Zweck |

|------------|--------|

| Windows 11 | Hostsystem |

| VirtualBox | Virtualisierung |

| Vagrant | Automatisierte VM-Erstellung |

| Ubuntu 22.04 | Serversystem |

| Ansible | Automatisierung |

| Docker | Containerisierung |

| Nginx | Reverse Proxy |

| Python | Webanwendung |

| Git | Versionsverwaltung |

| GitHub | Codeverwaltung |



\---



\# 4. Systemarchitektur



Die Architektur besteht aus einer Ubuntu-VM, welche mittels Vagrant erstellt wird.



Innerhalb der VM installiert Ansible automatisch Docker. Anschliessend werden zwei Container bereitgestellt:



\- Nginx als Reverse Proxy

\- Python-Webserver als Backend



```text

Windows 11

│

├── VirtualBox

│

└── Ubuntu VM (Vagrant)

&#x20;     │

&#x20;     ├── Ansible

&#x20;     │

&#x20;     └── Docker

&#x20;           │

&#x20;           ├── Nginx Container

&#x20;           │      (Reverse Proxy)

&#x20;           │

&#x20;           └── Python Container

&#x20;                  (Backend)

```



\---



\# 5. Projektstruktur



```text

ansible-docker-python-webserver/

│

├── README.md

├── Vagrantfile

│

├── ansible/

│   ├── inventory/

│   ├── playbooks/

│   └── roles/

│

├── app/

│   ├── app.py

│   └── Dockerfile

│

├── nginx/

│   └── nginx.conf

│

└── docs/

&#x20;   └── Projektdokumentation.md

```



\---



\# 6. Erstellung der virtuellen Maschine



Die virtuelle Maschine wurde mit Vagrant erstellt.



VM starten:



```bash

vagrant up

```



Verbindung zur VM:



```bash

vagrant ssh

```



Der Port 8080 wurde vom Gast auf den Host weitergeleitet.



\---



\# 7. Ansible-Konfiguration



Für die Automatisierung wurde Ansible verwendet.



Installation:



```bash

sudo apt update

sudo apt install -y ansible

```



Ansible führt anschliessend die definierten Playbooks und Rollen aus.



\---



\# 8. Ansible Playbook



Datei:



```text

ansible/playbooks/site.yml

```



Inhalt:



```yaml

\---

\- hosts: localhost

&#x20; become: yes



&#x20; roles:

&#x20;   - webserver

```



Das Playbook ruft die Rolle `webserver` auf.



\---



\# 9. Rolle "webserver"



Die Rolle übernimmt folgende Aufgaben:



1\. Installation von Docker

2\. Start des Docker-Dienstes

3\. Erstellung eines Docker-Netzwerks

4\. Erstellung des Python-Docker-Images

5\. Start des Python-Containers

6\. Start des Nginx-Containers



\---



\# 10. Python-Webanwendung



Die Anwendung wurde mit Python erstellt.



Der Webserver lauscht auf Port 5000 und liefert eine einfache HTML-Seite aus.



Der Zugriff erfolgt ausschliesslich über den Nginx Reverse Proxy.



\---



\# 11. Nginx Reverse Proxy



Nginx nimmt HTTP-Anfragen auf Port 80 entgegen.



Anschliessend werden die Anfragen an den Python-Webserver weitergeleitet.



Konfiguration:



```nginx

location / {

&#x20;   proxy\_pass http://python-app:5000;

}

```



\---



\# 12. Ausführung des Playbooks



Das Playbook wird mit folgendem Befehl gestartet:



```bash

ANSIBLE\_ROLES\_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml

```



Erfolgreiche Ausführung:



```text

PLAY RECAP

localhost : ok=7 changed=5 failed=0

```



\---



\# 13. Funktionstest



Nach erfolgreicher Bereitstellung kann die Anwendung über folgende Adresse aufgerufen werden:



```text

http://localhost:8080

```



Die Webseite wird vom Python-Webserver ausgeliefert und über den Nginx Reverse Proxy bereitgestellt.



\---



\# 14. Zielerreichung



Die definierten Projektziele konnten vollständig erreicht werden.



Die virtuelle Ubuntu-Maschine wurde mittels Vagrant erstellt und anschliessend durch Ansible automatisiert konfiguriert.



Docker wurde installiert und gestartet. Die Container für Nginx und die Python-Webanwendung wurden automatisch bereitgestellt.



Der abschliessende Funktionstest bestätigte die erfolgreiche Erreichbarkeit der Anwendung über den Browser.



\---



\# 15. GitHub Repository



Der gesamte Quellcode wird über Git und GitHub versioniert.



Repository:



```text

https://github.com/19boboy97/ansible-docker-python-webserver

```



Durch die Verwendung von Git konnten sämtliche Änderungen nachvollziehbar dokumentiert und versioniert werden.



\---



\# 16. Fazit



Mit Vagrant, Ansible und Docker konnte eine vollständig automatisierte Webserver-Umgebung erstellt werden.



Das Projekt zeigt den praktischen Einsatz moderner DevOps-Werkzeuge zur automatisierten Bereitstellung von Infrastruktur und Anwendungen.



Besonders hilfreich war das Zusammenspiel von Vagrant zur Erstellung der virtuellen Maschine, Ansible zur Automatisierung der Konfiguration sowie Docker zur Containerisierung der Anwendung.



Die Lösung ist reproduzierbar, einfach erweiterbar und erfüllt sämtliche definierten Anforderungen.



\---



\# 17. Quellen



\- https://www.ansible.com

\- https://docs.ansible.com

\- https://www.docker.com

\- https://docs.docker.com

\- https://developer.hashicorp.com/vagrant

\- https://ubuntu.com

\- https://nginx.org

\- https://www.python.org

\- https://github.com

