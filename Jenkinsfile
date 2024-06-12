pipeline {
    agent any
    // agent {
    //     docker { image 'node:20.11.1-alpine3.19' }
    // }
    stages {
        stage('Test') {
            steps {
                sh 'docker build -t sjamberu/world_of_games:1.0 .'
                sh 'docker images'
                sh 'docker ps'
            }
        }
    }
}
