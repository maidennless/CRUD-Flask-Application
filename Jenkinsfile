pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Prepare Python Environment') {
            steps {
                echo 'Creating virtual environment...'
                sh 'python3 -m venv $VENV_DIR'
                echo 'Activating virtual environment and installing dependencies...'
                sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Running the Flask application...'
                sh '''
                . $VENV_DIR/bin/activate
                export FLASK_APP=app.py
                export FLASK_ENV=development
                python3 app.py &
                sleep 5
                '''
                echo 'Flask app started!'
            }
        }

        stage('Test Endpoint') {
            steps {
                echo 'Testing the homepage...'
                sh 'curl -I http://localhost:5000 || true'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'pkill -f "python3 app.py" || true'
        }
