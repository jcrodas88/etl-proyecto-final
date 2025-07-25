pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'develop', url: 'https://github.com/jcrodas88/etl-proyecto-final.git'
            }
        }

        stage('Ejecutar ETL') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
