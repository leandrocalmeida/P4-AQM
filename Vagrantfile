Vagrant.configure("2") do |config|
    
    config.vm.define "sw1" do |sw1|
        sw1.vm.box = "leandrocdealmeida/bmv2-p4"
        sw1.vm.hostname = "sw1"
        sw1.vm.network "private_network", ip: "192.168.56.201",
            name: "vboxnet0"
        sw1.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "ds-S1"
        sw1.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S1-S2"
        sw1.vm.provider "virtualbox" do |v|
            v.memory = 512
            v.cpus = 1
            v.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
            v.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
        end
        sw1.vm.provision "ansible" do |ansible| 
            ansible.playbook = "sw/sw1.yml"
        end
    end

    config.vm.define "sw2" do |sw2|
        sw2.vm.box = "leandrocdealmeida/bmv2-p4"
        sw2.vm.hostname = "sw2"
        sw2.vm.network "private_network", ip: "192.168.56.202",
            name: "vboxnet0"
        sw2.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S1-S2"
        sw2.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S2-S3"
        sw2.vm.provider "virtualbox" do |v|
            v.memory = 512
            v.cpus = 1
            v.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
            v.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
        end
        sw2.vm.provision "ansible" do |ansible| 
            ansible.playbook = "sw/sw2.yml"
        end
    end

    config.vm.define "sw3" do |sw3|
        sw3.vm.box = "leandrocdealmeida/bmv2-p4"
        sw3.vm.hostname = "sw3"
        sw3.vm.network "private_network", ip: "192.168.56.203",
            name: "vboxnet0"
        sw3.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S2-S3"
        sw3.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S3-clientvlc"
        sw3.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S3-lg1"
        sw3.vm.network "private_network", auto_config: false,
            virtualbox__intnet: "S3-lg2"
        sw3.vm.provider "virtualbox" do |v|
            v.memory = 512
            v.cpus = 1
            v.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
            v.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
            v.customize ["modifyvm", :id, "--nicpromisc5", "allow-all"]
            v.customize ["modifyvm", :id, "--nicpromisc6", "allow-all"]
        end
        sw3.vm.provision "ansible" do |ansible| 
            ansible.playbook = "sw/sw3.yml"
        end
    end

    config.vm.define "dashServer" do |ds|
        ds.vm.box = "ubuntu/focal64"
        ds.vm.hostname = "dashServer"
        ds.vm.network "private_network", ip: "192.168.50.50", mac: "080027000000",
            virtualbox__intnet: "ds-S1"
        ds.vm.provider "virtualbox" do |v|
            v.memory = 512
            v.cpus = 1
        end
        ds.vm.provision "ansible" do |ansible| 
            ansible.playbook = "host/dash.yml"
        end
    end

    config.vm.define "clientVlc" do |cvlc|
        cvlc.vm.box = "leandrocdealmeida/ubuntu-vlc"
        cvlc.vm.hostname = "clientVlc"
        cvlc.vm.network "private_network", ip: "192.168.50.51", mac: "080027000001",
            virtualbox__intnet: "S3-clientvlc"
        cvlc.vm.provider "virtualbox" do |v|
            v.memory = 4096
            v.cpus = 4
            v.customize ["modifyvm", :id, "--accelerate3d", "on"]
            v.customize ["modifyvm", :id, "--vrde", "on"]
            v.customize ["modifyvm", :id, "--vrdeport", "8080"]

        end
        cvlc.vm.provision "ansible" do |ansible| 
            ansible.playbook = "host/client.yml"
        end
    end

    config.vm.define "loadGen1" do |lg1|
        lg1.vm.box = "leandrocdealmeida/ubuntu-vlc"
        lg1.vm.hostname = "loadGen1"
        lg1.vm.network "private_network", ip: "192.168.50.52", mac: "080027000002",
            virtualbox__intnet: "S3-lg1"
        lg1.vm.provider "virtualbox" do |v|
            v.memory = 8192
            v.cpus = 12
            v.customize ["modifyvm", :id, "--accelerate3d", "on"]
            v.customize ["modifyvm", :id, "--vrde", "on"]
            v.customize ["modifyvm", :id, "--vrdeport", "8081"]

        end
        lg1.vm.provision "ansible" do |ansible| 
            ansible.playbook = "host/loadGen.yml"
        end
    end
end