pipeline {
    agent any
    stages {
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                    container('python') {
                        dir('getac-camera-test') {
                            sh 'pwd'
                            sh 'ls -l'
                            catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                                    sh 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir allure-results'
                                } 
                            }
                        }
                    }
                }
            }
        }
    }
}