pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkouting...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'f410439b-b054-49bd-9eb2-5d3450760605', url: 'https://github.com/jamberusimantov/WorldOfGames.git']])
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                def container = docker.build '"sjamberu/world_of_games:1.1"'
                    container.inside {
                        sh 'make test'
                    } 
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
