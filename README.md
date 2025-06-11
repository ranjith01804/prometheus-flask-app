Run a pyhton flask application under supervisorctl in ubutu with integration of prometheus and grafana.








Install supervisorctl to run a python application

sudo apt update
sudo apt install supervisor

sudo vi /etc/supervisor/conf.d/myapp.conf  #Use myapp.conf contents in my github repo.


After adding conf file, Run below command

sudo supervisorctl reread
sudo supervisorctl update

sudo supervisorctl start myapp

sudo supervisorctl status myapp

Install Prometheus

cd /tmp
curl -s https://api.github.com/repos/prometheus/prometheus/releases/latest \
  | grep browser_download_url \
  | grep linux-amd64.tar.gz \
  | cut -d '"' -f 4 \
  | wget -i -

# Extract and move binaries
tar xvf prometheus-*.tar.gz
cd prometheus-*/
sudo mv prometheus promtool /usr/local/bin/
sudo mkdir -p /etc/prometheus /var/lib/prometheus
sudo cp -r consoles console_libraries /etc/prometheus/


sudo vi /etc/prometheus/prometheus.yml












Grafana Installation
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana -y


sudo systemctl enable --now grafana-server
User: admin
Pass: admin
