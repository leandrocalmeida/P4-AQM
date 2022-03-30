#Adjust mime types for apache server
sudo cp /vagrant/host/apache/mime.conf /etc/apache2/mods-available/mime.conf

#adjust apache and symbol links 
cd /var/www/html && sudo mv index.html index.html.def && \
sudo ln -s /vagrant/videos/ /var/www/html/

#reload apache2
sudo systemctl reload apache2