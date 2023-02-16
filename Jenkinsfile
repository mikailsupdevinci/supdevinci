pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Unit tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Publish test results') {
            steps {
                junit 'tests/*.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts 'tests/*.xml'
        }
    }
}