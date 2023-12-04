pipeline {
    agent any
    stages {
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                         script {
                            bat 'pip install -r requirements.txt'
                            bat 'conda list'
                            bat 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir allure-results'
                         }
                    }
                }
            }
        }
    }
}
