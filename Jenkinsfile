pipeline {
    agent  any
    
    stages {
        
        stage('Checkout') {
            steps {
                echo 'Checkouting...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'f410439b-b054-49bd-9eb2-5d3450760605', url: 'https://github.com/jamberusimantov/WorldOfGames.git']])
                ls '-ltra'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker build -t sjamberu/world_of_games:1.0 -p 8777:8777 --rm --no-cache -o out --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 .'
                sh 'docker ps -a'
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
