pipeline {
    agent  any
    
    stages {
        
        stage('Build') {
            steps {
                echo 'Building...'
                // sh 'docker build -t sjamberu/world_of_games:1.0 -p 8777:8777 --rm --no-cache -o out --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 .'
                // sh 'docker ps -a'
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
