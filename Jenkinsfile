pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/gopal-py07/CI-CD-Python-Django-Poll-App-Docker-Kubernet-minikube-.git'
        WORKSPACE_PATH = "${env.WORKSPACE}"
        DOCKER_COMPOSE_FILE = "${WORKSPACE_PATH}/docker-compose.yml"
        MINIKUBE_PATH = '/usr/local/bin/minikube'
        KUBECTL_PATH = '/usr/local/bin/kubectl'
        DEPLOYMENT_YML_PATH = 'deployment.yml'
        SERVICE_NAME = 'django-backend-poll-app-jenkins-service'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    sh "pwd"
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'master']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [[$class: 'CleanBeforeCheckout']],
                        userRemoteConfigs: [[url: env.GIT_REPO_URL]]
                    ])
                }
            }
        }

        stage('Docker Compose') {
            steps {
                script {
                    sh "docker-compose -f ${env.DOCKER_COMPOSE_FILE} build --no-cache"
                    sh "docker-compose -f ${env.DOCKER_COMPOSE_FILE} up -d"
                }
            }
        }

        stage('Push Docker Images to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                        sh "docker push gopalghule05/lnx_poll_prj_jenkins:1.3"
                    }
                }
            }
        }

        /*stage('Check Minikube Status') {
            steps {
                script {
                    def minikubeStatus = sh(script: "${MINIKUBE_PATH} status", returnStatus: true)
                    
                    if (minikubeStatus == 0) {
                        echo "Minikube is running. Skipping this stage."
                        currentBuild.result = 'SUCCESS'
                    } else {
                        echo "Minikube is not running. Starting Minikube..."
                        sh "${MINIKUBE_PATH} start"
                    }
                }
            }
        }*/
        //commentin jenkins file argocd dplyment testing // for jenkins and minkune please uncomment below code and push file at code level not in any folder
        /*stage('Apply Kubernetes Deployment') {
            steps {
                script {
                    sh "${KUBECTL_PATH} apply -f ${DEPLOYMENT_YML_PATH}"
                }
            }
        }

        stage('Check Service in Kubernetes') {
            steps {
                script {
                    def serviceExists = sh(script: "${KUBECTL_PATH} get service ${SERVICE_NAME}", returnStatus: true)
                    
                    if (serviceExists == 0) {
                        echo "Service ${SERVICE_NAME} exists. Skipping the 'Expose Port' stage."
                        currentBuild.result = 'SUCCESS' // Mark the build as success
                    } else {
                        echo "Service ${SERVICE_NAME} does not exist. Proceeding to the 'Expose Port' stage."
                        sh "${KUBECTL_PATH} expose deployment ${SERVICE_NAME} --type=LoadBalancer --port=8000"
                    }
                }
            }
        }

        stage('Open Service in Minikube') {
            steps {
                script {
                    sh "${MINIKUBE_PATH} service list"
                    sh "${MINIKUBE_PATH} service ${SERVICE_NAME}"
                    //sh "${MINIKUBE_PATH} dashboard --url"
                    //sh "xdg-open $(minikube service ${SERVICE_NAME} --url)"
                }
            }
        }*/
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
