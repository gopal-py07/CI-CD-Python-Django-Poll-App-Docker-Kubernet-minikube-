pipeline {
    agent any

    environment {
        // Define environment variables for paths
        GIT_REPO_URL = 'https://github.com/gopal-py07/CI-CD-Python-Django-Poll-App-Docker-Kubernet-minikube-.git'
        WORKSPACE_PATH = "${env.WORKSPACE}"
        DOCKER_COMPOSE_FILE = "${WORKSPACE_PATH}/docker-compose.yml"
        MINIKUBE_PATH = '/usr/local/bin/minikube'
        KUBECTL_PATH = '/usr/local/bin/kubectl'
        DEPLOYMENT_YML_PATH = 'deployment.yml'
        SERVICE_NAME = 'django-backend-poll-app-jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    sh "pwd"
                    // Checkout the code from the specified repository URL
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'master']], // Specify the branch you want to checkout (main)
                        doGenerateSubmoduleConfigurations: false, // You can set this to true if you have submodules
                        extensions: [[$class: 'CleanBeforeCheckout']], // Clean before checkout
                        userRemoteConfigs: [[url: env.GIT_REPO_URL]]
                    ])
                }
            }
        }

        /*stage('Docker Compose') {
            steps {
                script {
                    // Build and run Docker Compose with the specified Compose file
                    sh "docker-compose -f ${env.DOCKER_COMPOSE_FILE} build --no-cache"
                    sh "docker-compose -f ${env.DOCKER_COMPOSE_FILE} up -d"
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
                        sh "docker push gopalghule05/lnx_poll_jenkins_prj:latest"
                    }
                }
            }
        }*/

        stage('Apply Kubernetes Deployment') {
            steps {
                script {
                    sh "${MINIKUBE_PATH} delete"
                    sh "${MINIKUBE_PATH} start"
                    sh "${KUBECTL_PATH} apply -f ${DEPLOYMENT_YML_PATH}"
                }
            }
        }

        stage('Expose Deployment as LoadBalancer') {
            steps {
                script {
                    sh "${KUBECTL_PATH} expose deployment ${SERVICE_NAME} --type=LoadBalancer --port=8000"
                }
            }
        }

        stage('Open Service in Minikube') {
            steps {
                script {
                    //sh "${MINIKUBE_PATH} service list"
                    //sh "${MINIKUBE_PATH} service ${SERVICE_NAME}"
                    //sh "${MINIKUBE_PATH} dashboard --url"
                    sh 'xdg-open ' + sh(script: "${MINIKUBE_PATH} service ${SERVICE_NAME} --url", returnStatus: true).trim()
                }
            }
        }

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
