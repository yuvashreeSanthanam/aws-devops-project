
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'aws-devops-project'
        CONTAINER_NAME = 'flask-demo'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting application source code from GitHub'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing Flask application'

                sh '''
                    docker rm -f flask-test || true

                    docker run -d \
                      --name flask-test \
                      -p 5001:5000 \
                      ${IMAGE_NAME}:${BUILD_NUMBER}

                    sleep 5

                    curl -f http://localhost:5001

                    docker rm -f flask-test
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying application on EC2'

                sh '''
                    docker rm -f ${CONTAINER_NAME} || true

                    docker run -d \
                      --name ${CONTAINER_NAME} \
                      -p 5000:5000 \
                      ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rm -f flask-test || true'
        }

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }
    }
}
