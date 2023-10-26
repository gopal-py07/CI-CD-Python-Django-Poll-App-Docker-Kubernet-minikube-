pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Define the GitLab repository URL
                    def gitHubRepoURL = 'https://github.com/gopal-py07/CI-CD-Python-Django-Poll-App-Docker-Kubernet-minikube-.git'
                    sh 'pwd'

                    // Checkout the code from GitLab using the Git SCM step
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'master']], // Specify the branch you want to checkout (main)
                        doGenerateSubmoduleConfigurations: false, // You can set this to true if you have submodules
                        extensions: [[$class: 'CleanBeforeCheckout']], // Clean before checkout
                        userRemoteConfigs: [[url: gitHubRepoURL]]
                    ])
                }
            }
        }

        stage('Docker Compose') {
            steps {
                script {
                    // Run Docker Compose with the specified Compose file
                    //sh 'docker-compose -f /var/lib/jenkins/workspace/ci-cd-Python-Django-Poll-app/docker-compose.yml up -d'
                    sh 'sudo docker-compose -f /var/lib/jenkins/workspace/ci-cd-pyhton-Django-poll-app-github/docker-compose.yml build --no-cache'
                    sh 'sudo docker-compose -f /var/lib/jenkins/workspace/ci-cd-pyhton-Django-poll-app-github/docker-compose.yml up -d'

                }
            }
        }

        stage('Push Docker Images to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub using Jenkins credentials
                    withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"

                        // Push the Docker images to your Docker Hub repository
                        sh 'docker push  gopalghule05/lnx_poll_prj_jenkins_test4:latest'
                    }
                }
            }
        }

        /*stage('Apply Kubernetes Deployment') {
            steps {
                script {
	
		            sh '/usr/local/bin/minikube start'
		            sh '/usr/local/bin/kubectl apply -f deployment.yml' 
                }
            }
        }
        stage('Expose Deployment as LoadBalancer') {
            steps {
                script {
                    // Expose the Kubernetes deployment as a LoadBalancer service
                    sh '/usr/local/bin/kubectl expose deployment django-backend-poll-app-jenkins-test4 --type=LoadBalancer --port=8000'
                }
            }
        }
        
        stage('Open Service in Minikube') {
            steps {
                script {
                    // Open the service in Minikube (this will open the default web browser)
                    sh '/usr/local/bin/minikube service --all'
		            sh '/usr/local/bin/minikube service django-backend-poll-app-jenkins-test4'
                    sh '/usr/local/bin/minikube dashboard --url'

                }
            }
        }*/


        // Add more stages for your build, test, and deployment steps here
    }

    post {
        success {
            echo 'Code checkout, Docker Compose, image upload, and deployment were successful.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}


