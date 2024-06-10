pipeline {
    agent { dockerfile true }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkouting...'
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
