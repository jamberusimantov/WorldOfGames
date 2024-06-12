pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker images'
                sh 'docker build -t sjamberu/world_of_games:1.0 .'
                sh 'docker images'
            }
        }
        stage('Run') {
            steps {
                sh 'echo Running...'
                sh 'docker ps'
                sh 'docker run --name web --detach --rm --publish 8777:8777 --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 sjamberu/world_of_games:1.0'
                sh 'docker ps'
            }
        }
    }
}
