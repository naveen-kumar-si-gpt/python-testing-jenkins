pipeline {
    agent any

    triggers {
        githubPush()  // Trigger on every push to GitHub
    }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    export PYTHONPATH=.
                    pytest tests/ --junitxml=report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
