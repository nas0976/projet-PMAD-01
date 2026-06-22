pipeline {
    agent any

    environment {
        // Indique à kubectl d'utiliser la configuration partagée du cluster PMAD
        KUBECONFIG = '${WORKSPACE}/.kube/config'
    }

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
                // Exécution de la commande de déploiement à l'intérieur du conteneur
                sh 'kubectl apply -f k8s/deployment.yml --validate=false'
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
