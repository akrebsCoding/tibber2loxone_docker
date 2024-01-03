# tibber2loxone_docker
You can run tibber2loxone in a container

based on ubuntu (complete size ~ 480mb)


<b>Instructions</b>

- clone the rep
- cd into the rep
- run "docker build -t ubuntu ."
- run "docker run --name server -d -p9946:9945 ubuntu"
- browse to "localhost:9946"
 
