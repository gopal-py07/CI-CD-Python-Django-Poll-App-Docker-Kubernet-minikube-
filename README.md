Node: The repository update as per testing DevOps tools and document may me be old. i will update document asap

Dockerize Django Poll Application & Run As Kubernetes Pod With Minikube

Abstract

	After Develop Poll Application using Django Framework used to Dockerize and deploy on kubernetes pod with minikube and expose 8000 port. The Document have all process to reach to final stage

Document History
Revision	Date	Description	Author
1.0	15-June-2023	Initial creation	Gopal G
			
			
After Develop Poll Application using Django follow below steps to Dockerize and deploy on kubernetes pod with minikube
1.	Install Docker desktop on your laptop using WSL2
2.	Containerize poll app using docker
3.	Build docker image for poll app
4.	Install minikube on you laptop
5.	Run poll app as a kubernetes pod and expose it using a NodePort service on 8000 targetPort.
1.	Install Docker desktop on your laptop using WSL2.

1.1 Download the docker desktop for windows using below link
https://www.docker.com/products/docker-desktop/ 

1.2.	Check you WSL Enable or not. If not then Enable It .

1.3.	After installation of docker go to setting enable wsl-2 integration

1.3.1 if its not showing or given some error after run docker –version cmd in ubuntu terminal.
1.3.2 Run below command as well as follow given link below.
	https://docs.docker.com/desktop/windows/wsl/
	Open terminal of windows Run Command:
wsl.exe -l -v
														check  destro ..
As the default is wsl-1 but requirement is for wsl-2 use blow command on same terminal.
To upgrade your existing Linux distro to v2, run 
wsl.exe --set-version Ubuntu-18.04 2
To set Ubuntu as your default WSL distro, run:
wsl --set-default Ubuntu-18.04
	1.3.3. Go to Docker desktop setting and Enable your wsl instigation shown above.
	1.4. run docker –version in ubuntu terminal..

Done with Docker Desktop set-up with wsl-2



Note: From next steps Using os Linux(Ubuntu)







2. Containerize poll app using docker.
2.1. Create Dockerfile in the core project folder and create docker compose yaml file shown below

3 .Build docker image for poll application
 3.1. After wright a code in both files and Run the below command in same location on terminal.
	docker-compose -f docker-compose.yml up -d --build
3.2 . Check into Docker-desktop container and image are create successfully by running command or  docker on  deskstop	
•	Command run on terminal:
	      docker ps 
     docker ps -a 
     docker images
•	docker desktop

3.3. Open Browser and run localhost:8000 
3.4. Play with Poll app.

4. Install minikube on your laptop(win or lnx):
Note: In the example use Linux OS to install minikube.
4.1. Follow the below link 
	https://minikube.sigs.k8s.io/docs/start/
	note: choose Linux button on the link
4.2 . Optional step if you don’t go through 4.1 step Please follow below step to install minikube 
      4.2.1 Open terminal of ubuntu and run below commands:
•	Installation command:
	curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
              sudo install minikube-linux-amd64 /usr/local/bin/minikube 
•	Start your cluster
minikube start
•	Interact with your cluster
    If already kubernetes install
kubectl get po -A

    if not install kubernate then use below

minikube kubectl -- get po -A

   aliases with 

alias kubectl="minikube kubectl --"      
By using docker desktop you can enable kubernetes but its optional steps 

5.	Run poll app as a kubernetes pod and expose it using a NodePort  or  LoadBalancer service on 8000 targetPort.
5.1 Push Image to Docker Hub
•	Run below command on terminal

Note: create you account to docker before doing below process
docker login
docker push (image_name)
•	or push using docker desktop

5.2 create- deployment.yml and write code in core folder of Django Poll app

5.3 Run command to create pod
kubectl apply -f deployment.yml
•	Run command to check pods
		kubectl get pods
		kubectl get deploy -A
		kubectl get service




5.4	Expose port 8000
kubectl expose deployment django-backend-poll-app-two-test --type=LoadBalancer --port=8000
or
kubectl expose deployment django-backend-poll-app-two-test --type= NodePort  --port=8000

5.5 Get Urls
•	Before  get url check below command
                     minikube status
		
		minikube start	


•	Get Url
		minikube service (service_name)
minikube service django-backend-poll-app-two-test


OR
minikube service django-backend-poll-app-two-test --url

5.5 Click on Url or copy link to browser and enjoy to play with Poll Application


Successfully Done !










	





















 
