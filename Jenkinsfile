pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker build -t sjamberu/world_of_games:1.0 .'
                sh 'docker images|grep sjamberu/world_of_games:1.0'
            }
        }
    }
}
