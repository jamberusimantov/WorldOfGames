pipeline {
    agent any
    def docker_token = 'dckr_pat_JfyhCwfu9XqUloG1bmtHNuqCcTc'
    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker build -t sjamberu/world_of_games:1.0 .'
                sh 'docker images'
            }
        }
        stage('Run') {
            steps {
                sh 'echo Running...'
                sh 'docker run --name world_of_games --detach --rm --publish 8777:8777 --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 sjamberu/world_of_games:1.0'
                sh 'docker ps'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Testing...'
                sh 'docker exec -i world_of_games sh -c "python WorldOfGames/e2e.py"'
            }
        }
        stage('Finalize') {
            steps {
                sh 'echo Finalizing...'
                sh 'docker login -u sjamberu -p $docker_token'
                sh 'docker push sjamberu/world_of_games:1.0'
                sh 'docker stop world_of_games'
                sh 'docker rmi sjamberu/world_of_games:1.0'
            }
        }
    }
}
