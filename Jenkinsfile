pipeline {
    agent any

    environment {
        VENV_PATH = "venv"
    }

    stages {
        stage('Clone & Setup') {
            steps {
                bat '''
                echo Current dir: %CD%
                python -m venv %VENV_PATH%
                call %VENV_PATH%\\Scripts\\activate.bat
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                bat '''
                call %VENV_PATH%\\Scripts\\activate.bat
                start /b python app.py
                timeout /t 5
                '''
            }
        }

        stage('Test Endpoint') {
            steps {
                bat 'curl -I http://localhost:5000 || echo App might not be up'
            }
        }
    }

    post {
        always {
            bat 'taskkill /F /IM python.exe || echo No process to kill'
        }
    }
}
