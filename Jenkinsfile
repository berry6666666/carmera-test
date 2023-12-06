pipeline {
    agent any
    stages {
        stage('install env'){
            steps{
                script {
                        bat 'pip install -r requirements.txt'
                        bat 'conda list'
                }
            }
        }
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                         script {
                            catchError(buildResult: 'FAILURE', stageResult: 'FAILURE'){
                                bat 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir allure-results'
                            }
                         }
                    }
                }
            }
        }
    }
    post {
        always {
            // 生成并显示 Allure 报告
            allure includeProperties: false, results: [[path: 'allure-results']]
        }
    }
}
