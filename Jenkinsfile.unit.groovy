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
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('API Tests') {
            steps {
                echo 'Running API tests'
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
                
            }
        }
        stage('E2E Tests') {
            steps {
                echo 'Running E2E tests'
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
            
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        failure {
            mail(
                to: 'jairohernan.espinoza245@comunidadunir.net',
                subject: "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The job ${env.JOB_NAME} #${env.BUILD_NUMBER} has failed. Check the logs for more information."
            )
        }
    }
}