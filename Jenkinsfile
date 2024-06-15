pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                sh 'echo Checkouting...'
                git branch: 'main', url: 'https://github.com/jamberusimantov/WorldOfGames.git'
                sh 'ls -ltra'
            }
        }
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
                sh 'docker exec -i wog sh -c "python WorldOfGames/e2e.py"'
            }
        }
        stage('Finalize') {
            steps {
                sh 'echo Finalizing...'
                sh 'docker stop wog'
                sh 'docker rmi mywog:1.0'
            }
        }
    }
}
