# Build and lauch Docker image
./build_and_launch.sh 

# check that port 3000 is in use by using e.g.
netstat -apn | grep 3000

tcp        0      0 0.0.0.0:3000            0.0.0.0:*               LISTEN 

# check REST and WEBSOCKET examples in python_examples folder
