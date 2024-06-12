pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker build -t mywog:1.0 .'
                sh 'docker images'
            }
        }
        stage('Run') {
            steps {
                sh 'echo Running...'
                sh 'docker run --name wog --detach --rm --publish 8777:8777 --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 mywog:1.0'
                sh 'docker ps'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Testing...'
                sh 'docker exec -it wog sh -c "python WorldOfGames/e2e.py"'
            }
        }
    }
}
