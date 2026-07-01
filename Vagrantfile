Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.hostname = "ansible-webserver"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.network "public_network"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt update
    apt install -y ansible

    cd /vagrant/ansible/playbooks
    ANSIBLE_ROLES_PATH=/vagrant/ansible/roles ansible-playbook site.yml -i ../inventory/hosts.yml
  SHELL
end