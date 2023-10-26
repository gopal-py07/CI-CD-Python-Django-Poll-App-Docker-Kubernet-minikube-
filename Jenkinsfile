pipeline {
    agent any

    environment {
        // Define environment variables for paths
        GIT_REPO_URL = 'https://github.com/gopal-py07/CI-CD-Python-Django-Poll-App-Docker-Kubernet-minikube-.git'
        WORKSPACE_PATH = "${env.WORKSPACE}"
        DOCKER_COMPOSE_FILE = "${WORKSPACE_PATH}/docker-compose.yml"
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

        stage('Docker Compose') {
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
                        sh "docker push gopalghule05/lnx_poll_prj_jenkins_test4:latest"
                    }
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
