pipeline {
    agent any

    tools {
        allure 'Allure'
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                checkout scm
            }
        }

        stage('Preparar Entorno Virtual') {
            steps {
                echo 'Creando entorno virtual e instalando dependencias...'
                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Instalar Navegadores Playwright') {
            steps {
                echo 'Descargando binarios de Playwright...'
                bat """
                call venv\\Scripts\\activate
                playwright install chromium
                """
            }
        }

        stage('Ejecutar Pruebas Automatizadas') {
            steps {
                echo 'Iniciando pruebas con Pytest-BDD...'
                bat """
                call venv\\Scripts\\activate
                pytest --alluredir=allure-results
                """
            }
        }
    }

    post {
        always {
            echo 'Generando reporte de Allure...'
            allure includeProperties: false, 
                   jdk: '', 
                   properties: [], 
                   reportBuildPolicy: 'ALWAYS', 
                   results: [[path: 'allure-results']]
        }
    }
}