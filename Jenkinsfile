pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
        dockerfile {
            filename 'Dockerfile'
            dir '.'
            additionalBuildArgs  '--build-arg version=1.0.2'
            args '-v /tmp:/tmp'
        }
    }
    stages {
        stage('Build') {
            agent  any
            steps {
                echo 'Building...'
                sh 'ls -ltra'
                sh 'docker build -t sjamberu/world_of_games:1.0 -p 8777:8777 --rm --no-cache -o out --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 .'
                // sh 'docker ps -a'
            }
        }
        
        stage('Run') {
            agent  any
            steps {
                echo 'Running...'
            }
        }
        
        stage('Test') {
            agent  any
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
