
pipeline {
    agent any

    parameters {
        string(
            name: 'BRANCH_NAME',
            defaultValue: 'main',
            description: 'Enter the Git branch to build'
        )
    }

    environment {
        IMAGE_NAME = 'aws-devops-project'
        CONTAINER_NAME = 'flask-demo'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out branch: ${params.BRANCH_NAME}"

                git branch: "${params.BRANCH_NAME}",
                    url: 'https://github.com/yuvashreeSanthanam/aws-devops-project.git'
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
