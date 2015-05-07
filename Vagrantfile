# config
public_http_port = 8000

# add a useful function to String
class String
    def strip_heredoc
        indent = scan(/^[ \t]*(?=\S)/).min.size || 0
        gsub(/^[ \t]{#{indent}}/, '')
    end
end

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network "forwarded_port", guest: 8000, host: public_http_port

    # extra configuration for the shared folder
    config.vm.synced_folder ".", "/vagrant",
        # use rsync instead of VirtualBox/VMWare shared folders,
        type: "rsync",
        # and exclude some more folders when syncing
        rsync_exclude: %(.vagrant .git .gitignore)

    # configure and install dependencies
    config.vm.provision "shell", privileged: true, inline: <<-SHELL.strip_heredoc
        # fail on error
        set -e

        mkdir -p /.litus_installation

        # run only once
        if [ -f /.litus_installation/1 ]; then
            exit 0
        fi

        # set the timezone to Brussels
        echo Europe/Brussels > /etc/timezone
        dpkg-reconfigure -fnoninteractive tzdata

        touch /.litus_installation/1
    SHELL

    config.vm.provision "shell", privileged: true, inline: <<-SHELL.strip_heredoc
        # fail on error
        set -e

        if [ -f /.litus_installation/2 ]; then
            exit 0
        fi

        cd /vagrant

        # update source lists
        apt-get update

        # install dependencies
        apt-get install -y python-dev python-pip postgresql-9.3 postgresql-server-dev-9.3

        pip install -r /vagrant/requirements.txt

        touch /.litus_installation/2
    SHELL

    config.vm.provision "shell", privileged: true, inline: <<-SHELL.strip_heredoc
        # fail on error
        set -e

        # run only once
        if [ -f /.litus_installation/3 ]; then
            exit 0
        fi

        # have postgres trust local users
        sed -i "s#host    all             all             127.0.0.1/32            md5#host    all             all             127.0.0.1/32            trust#" /etc/postgresql/9.3/main/pg_hba.conf
        sed -i "s#host    all             all             ::1/128                 md5#host    all             all             ::1/128                 trust#" /etc/postgresql/9.3/main/pg_hba.conf
        service postgresql restart

        # create postgres user
        if [ 0 -eq $(echo "SELECT COUNT(*) FROM pg_catalog.pg_user WHERE usename = 'root';" | su -c 'psql -t' postgres) ]; then
            echo "CREATE USER root WITH SUPERUSER;" | su -c psql postgres
        fi

        # create log directory
        mkdir /var/log/helios

        # creating some scripts
        echo "#! /bin/bash" >> /usr/local/sbin/start_helios
        echo "" >> /usr/local/sbin/start_helios
        echo "export GOOGLE_CLIENT_ID=\"999029084014-p2ld4u0oadsngvjbgqi7m4a8ehpjl56h.apps.googleusercontent.com\"" >> /usr/local/sbin/start_helios
        echo "export GOOGLE_CLIENT_SECRET=\"pUm29VHyzYCZAc8mSEfkQHvB\"" >> /usr/local/sbin/start_helios
        echo "" >> /usr/local/sbin/start_helios
        echo "python /vagrant/manage.py runserver 0.0.0.0:8000 >> /var/log/helios/web.log 2>&1 &" >> /usr/local/sbin/start_helios
        echo "python /vagrant/manage.py celeryd -E -B --beat --concurrency=1 -l INFO >> /var/log/helios/celeryd.log 2>&1" >> /usr/local/sbin/start_helios

        chmod +x /usr/local/sbin/start_helios

        echo "#! /bin/bash" >> /usr/local/sbin/start_screen
        echo "" >> /usr/local/sbin/start_screen
        echo "screen -dmS helios /usr/local/sbin/start_helios" >> /usr/local/sbin/start_screen

        chmod +x /usr/local/sbin/start_screen

        # make sure Helios starts on boot
        sed -i "s/exit 0//" /etc/rc.local
        sed -i "/^$/d" /etc/rc.local

        echo "" >> /etc/rc.local
        echo "/usr/local/sbin/start_screen" >> /etc/rc.local
        echo "" >> /etc/rc.local
        echo "exit 0" >> /etc/rc.local

        touch /.litus_installation/3
    SHELL

    config.vm.provision "shell", privileged: true, inline: <<-SHELL.strip_heredoc
        # fail on error
        set -e

        # run only once
        if [ -f /.litus_installation/4 ]; then
            exit 0
        fi

        # change path
        cd /vagrant

        # initialise database
        ./reset.sh

        touch /.litus_installation/4
    SHELL

    config.vm.provision :reload
end
