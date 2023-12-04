pipeline {
    agent any
    stages {
        stage('Run test') {
            parallel {
                stage ('RL1XXZ0007'){
                    steps {
                         script {
                            // 调用 Conda 初始化脚本
                            bat 'call C:\\Users\\barry.huang\\anaconda3\\envs\\test2'
                            // 激活 Conda 环境
                            bat 'call conda activate test2'
                            // 运行后续命令
                            bat 'pytest test/ --udid RL1XXZ0007 --platform-version 10 --alluredir report'
                         }
                    }
                }
            }
        }
    }
}
