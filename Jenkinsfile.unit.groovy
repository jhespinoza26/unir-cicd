pipeline {
    agent {
        label 'docker'
    }
    triggers {
        // Se agrega un cron para ejecutar el build cada 5 minutos
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/jhespinoza26/unir-cicd'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
            }
        }
        stage('API Tests') {
            steps {
                echo 'Running API tests'
                sh 'make test-api'

            }
            post {
                always {
                    archiveArtifacts artifacts: 'results/*.xml'
                    junit 'results/*.xml'
                }
            }
        }
        stage('E2E Tests') {
            steps {
                echo 'Running E2E tests'
                sh 'make test-e2e'  // Asegúrate de que este comando ejecuta tus pruebas E2E
            }
            post {
                always {
                    archiveArtifacts artifacts: 'results/*.xml'
                    junit 'results/*.xml'
                }
            }
        }
        stage('Print logs') {
            steps {
                script {
                    echo "Trabajo: ${env.JOB_NAME}"
                    echo "Ejecución número: ${env.BUILD_NUMBER}"
                }
            }
        }
    }
    post {
        always {
            junit 'results/*.xml'
        }
        failure {
            mail(
                to: 'lab1@comunidadunir.net',
                subject: "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The job ${env.JOB_NAME} #${env.BUILD_NUMBER} has failed. Check the logs for more information."
            )
        }
    }
}
