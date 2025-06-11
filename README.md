# Run a pyhton flask application under supervisorctl in ubuntu with integration of prometheus and grafana.


# Install supervisorctl to run a python application

sudo apt update
sudo apt install supervisor

sudo vi /etc/supervisor/conf.d/myapp.conf  #Please find conf file in my repo


# After adding conf file, Run below command

sudo supervisorctl reread
sudo supervisorctl update

sudo supervisorctl start myapp

sudo supervisorctl status myapp

# restart my app
sudo supervisorctl restart myapp



# Install Prometheus

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

# create prometheus user and change owmer of prometheus related files.

sudo useradd --no-create-home --shell /usr/sbin/nologin prometheus

sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus


# Prometheus configuration to scrape the metrics from given target
sudo vi /etc/prometheus/prometheus.yml  #Please find conf file in my repo

# Check prometheus.yml is valid or not
promtool check config /etc/prometheus/prometheus.yml

# Run prometheus under systemd
sudo vi /etc/systemd/system/prometheus.service    #Please find conf file in my repo

# Systemctl command
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable --now prometheus

# Check the prometheus status
systemctl status prometheus

# If you change anything in existing conf file, Please run below command
sudo systemctl daemon-reload
sudo systemctl restart prometheus
sudo systemctl status prometheus

# After Proper installation expected output
<img width="1787" alt="image" src="https://github.com/user-attachments/assets/09a883bf-2e05-4166-8b43-51da3289e197" />

<img width="1787" alt="image" src="https://github.com/user-attachments/assets/2be58b96-7011-47df-9440-a4cb07e88412" />






# Install Node exporter to make a dashboard about system resource usage like CPU,Memory..

# Download latest Node Exporter (adjust version as needed)
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz

# Extract
tar xvfz node_exporter-1.6.1.linux-amd64.tar.gz

# Move binary to /usr/local/bin
sudo mv node_exporter-1.6.1.linux-amd64/node_exporter /usr/local/bin/

# Cleanup
rm -rf node_exporter-1.6.1.linux-amd64*

# Create a systemd service for Node Exporter

sudo vi /etc/systemd/system/node_exporter.service   #Please find conf file in my repo

# Systemctl command
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter

# Check the node exporter status
sudo systemctl status node_exporter





# Grafana Installation
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana -y


sudo systemctl enable --now grafana-server

# Grafana User and Password
User: admin
Pass: admin

# Prometheus datasource Integrated in grafana
<img width="1427" alt="image" src="https://github.com/user-attachments/assets/83814f5e-63e5-4d41-86b8-c837e318b3ce" />




<img width="1787" alt="image" src="https://github.com/user-attachments/assets/bf64a22b-8c00-4496-9544-efb3899acd05" />

