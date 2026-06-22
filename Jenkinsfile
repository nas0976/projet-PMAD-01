pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Récupération du code depuis le dépôt Git...'
            }
        }

        stage('Build & Test application') {
            steps {
                echo 'Compilation et exécution des tests unitaires...'
            }
        }

        stage('Docker Image Build') {
            steps {
                echo 'Construction de l image Docker pmad-client...'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Déploiement de l application sur le cluster Kubernetes PMAD...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline exécuté avec succès ! Tout est en production.'
        }
        failure {
            echo 'Échec du pipeline. Vérifiez les logs.'
        }
    }
}
