pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkouting...'
                git url: 'https://github.com/jamberusimantov/WorldOfGames'
                sh 'make all'
                sh 'ls -ltra'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Run') {
            steps {
                echo 'Running...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Finalize') {
            steps {
                echo 'Finalizing....'
            }
        }
    }
}
