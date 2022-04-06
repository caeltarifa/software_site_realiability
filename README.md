

#  App Reliability Project  <img src="https://i.pinimg.com/originals/89/27/01/892701252dab9ead045f745d999cf9fc.gif" width="100" height="100" />
## 1 Project description
### 1.1 Application description
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/login.png)
- - - - 
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/app_api.png)
- - - - 
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/app_api_countries.png)

### 1.2 PromQL of the webapp

![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/many_times_restart_app.png)
- - - -
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/how_resident_memory_changing.png)
- - - -
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/how_many_memory_would_be_free.png)
- - - -

### 1.3 Dashboard visualization
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/grafana_dashboard.png)
- - - -
## 2 File structure of the project

    ├───initial_sre
    │   ├───initial_sre
    │   │   └───__pycache__
    │   ├───templates
    │   │   └───registration
    │   └───weatherapp
    │   |   ├───migrations
    │   |   │   └───__pycache__
    │   |   ├───templates
    │   |   │   └───weatherapp
    │   |   └───__pycache__
    │   └───Dockerfile
    │   └───db.sqlite3
    │   └───manage.py
    │   └───requirements.txt
    └───monitoring
    │   └───prometheus
    │   └───docker-compose.monitoring.yml
    │   └───prometheus.yml
    └───bash_initial.sh
    └───docker_commands
        
## 3 How does the app work?
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/arquitecture_app.png)

## 4 Architecture of containers
![alt text](https://github.com/caeltarifa/software_site_realiability/blob/main/containers.png)

## 5 Architecture of AWS services

api rest, containerized, monitoring, building, deploying and data visualization of a web app.



## 6 How installing and running?

### 6.1 Mounting the application docker container
Open this project in a terminal. You would open "initial_sre" and then introduce the following commands:

        $ docker build . -t django-dev 
        $ docker run -p 8001:8000 -it --rm django-dev
        ( $ winpty docker run -p 8001:8000 -it --rm django-dev  (only if you are in windows) )

That is enough and you will have the container running with the application running.

### 6.2 Mounting the monitoring and dashboard visualization services in docker container
Over the main directory from dis project, open the monitoring directory, and introduce the following commands:

        $ docker-compose  -f docker-compose.monitoring.yml up -d
        $ docker-compose  -f docker-compose.monitoring.yml ps

The firs command will execute the services: Prometheus and Grafana in the ports 9090 and 3060, respectively. For prometheus, in the docker-compose you have a file configuration in .yml to initialize the service interconected with the python application and customize some metrics to get from the app.

The second command show you the status of the services after lunch the container.
        

## 7 REFERENCES
### 7.1 WEB APPLICATION
- [How to consume API with django](https://codigofacilito.com/articulos/consumir-api-django "How to consume API with django")
- [Containerized a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application "Containerized a Python Django Web Application")
- [Set up and Run Django First Application](https://towardsdev.com/set-up-and-run-django-first-application-38f3a066cbb3?gi=ea52fb6526a9 "Set up and Run Django First Application")
- [Django First Steps for Total Beginners: A Quick Tutorial](https://towardsdatascience.com/django-first-steps-for-the-total-beginners-a-quick-tutorial-5f1e5e7e9a8c "Django First Steps for Total Beginners: A Quick Tutorial")
### 7.2 API REST
- [Web services weather API](https://www.weatherapi.com/ "Web services weather API")
- [Web services Cities API](https://documenter.getpostman.com/view/1134062/T1LJjU52  "web services Cities API")

### 7.3 DOCKER
- [Docker compose](https://docs.docker.com/compose/ "Docker compose")
### 7.4 PROMETHEUS & GRAFANA
- [Monitoring Couchbase Using Python, Prometheus, and Grafana (video)"](https://www.youtube.com/watch?v=w_sTCF8TCyk "Monitoring Couchbase Using Python, Prometheus, and Grafana (video)") 
- [YML prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/ "YML prometheus getting started")
- [Get Started to monitor your Django application with Prometheus & Grafana](https://www.sipios.com/blog-tech/monitoring "Get Started to monitor your Django application with Prometheus & Grafana")
- [Grafana demo online](https://play.grafana.org/d/000000012/grafana-play-home?orgId=1 "Grafana demo online")
- [Monitoring Docker container metrics using cAdvisor](https://prometheus.io/docs/guides/cadvisor/#docker-compose-configuration "Monitoring Docker container metrics using cAdvisor")
- [Prometheus + Grafana in Django](https://karanchuri.medium.com/prometheus-grafana-in-django-92da4d782f8a "Prometheus + Grafana in Django")
- [[video] Grafana Dashboard📊: Monitor CPU, Memory, Disk and Network Traffic Using Prometheus and Node Exporter](https://www.youtube.com/watch?v=YUabB_7H710 "[video] Grafana Dashboard📊: Monitor CPU, Memory, Disk and Network Traffic Using Prometheus and Node Exporter")
- [Promql](https://medium.com/@knoldus/introduction-to-promql-46260307fd83 "Promql")
- [The Top 25 Grafana Dashboards & Visualisations](https://logit.io/blog/post/the-top-21-grafana-dashboards-and-visualisations "Promql")

### 7.5 AWS
- [Cost manager AWS](https://us-east-1.console.aws.amazon.com/cost-management/home?region=us-east-1&skipRegion=true#/startupError?code=_CE_Not_Ready_&title=_CE_Not_Ready_Title_ "Cost manager AWS")









