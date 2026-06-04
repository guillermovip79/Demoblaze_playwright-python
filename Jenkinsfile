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
                echo 'Preparando entorno virtual e instalando dependencias...'
                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                
                :: Forzar instalacion de una version de greenlet compatible o precompilada
                pip install greenlet --pre --only-binary :all: 2>nul || pip install greenlet>=3.1.0a1 || echo "Continuando con el requirements..."
                
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