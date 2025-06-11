for i in {1..500}; do curl -s http://34.203.42.223:5000/hello >> ~/flask-metrics-app/output.log ; echo ""; sleep 1; done
