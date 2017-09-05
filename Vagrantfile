# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  config.vm.provision "init", :type => "shell", :path => "init.bash"
  config.vm.provision "test", :type => "shell", :path => "run_test_only.bash"
end
