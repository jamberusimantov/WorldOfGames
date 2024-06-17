pipeline {
    agent any
    environment {
        DOCKER_CONTAINER = 'sjamberu/world_of_games'
        DOCKER_IMAGE = 'sjamberu/world_of_games:1.0'
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker build -t $DOCKER_IMAGE .'
                sh 'docker images $DOCKER_IMAGE'
            }
        }
        stage('Run') {
            steps {
                sh 'echo Running...'
                sh 'docker run --name $DOCKER_CONTAINER --detach --rm --publish 8777:8777 --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 $DOCKER_IMAGE'
                sh 'docker ps -f "name=${DOCKER_CONTAINER}"'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Testing...'
                sh 'docker exec -i world_of_games sh -c "python WorldOfGames/e2e.py"'
            }
        }
        stage('Finalize') {
            environment {
                DOCKER_TOKEN = 'dckr_pat_JfyhCwfu9XqUloG1bmtHNuqCcTc'
            }
            steps {
                sh 'echo Finalizing...'
                sh 'docker login -u sjamberu -p $DOCKER_TOKEN'
                sh 'docker push $DOCKER_IMAGE'
            }
        }
        stage('Clear') {
            steps {
                sh 'echo Clearing...'
                sh 'docker stop $DOCKER_CONTAINER'
                sh 'docker rmi  $DOCKER_IMAGE'
            }
        }
    }
}
