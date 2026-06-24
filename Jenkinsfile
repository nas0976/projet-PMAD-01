pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Récupération du code depuis le dépôt Git...'
                // Récupère automatiquement le code de la branche courante
                checkout scm 
            }
        }

        stage('Build & Test application') {
            steps {
                echo 'Compilation et exécution des tests unitaires...'
                // Ajoute tes scripts de test ici quand ils seront prêts
            }
        }

        stage('Docker Image Build') {
            steps {
                echo 'Construction de l image Docker pmad-client...'
                // Ajoute tes commandes de build docker ici si nécessaire
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Déploiement de l infrastructure RustDesk sur le cluster Kubernetes PMAD...'
                script {
                    // Application des fichiers dans l'ordre logique d'interdépendance
                    sh 'kubectl apply -f k8s/pv-pvc.yml --validate=false'
                    sh 'kubectl apply -f k8s/hbbs-deployment.yml --validate=false'
                    sh 'kubectl apply -f k8s/hbbr-deployment.yml --validate=false'
                    sh 'kubectl apply -f k8s/services.yml --validate=false'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline exécuté avec succès ! Tout est en production. 🚀'
        }
        failure {
            echo 'Échec du pipeline. Vérifiez les logs. ❌'
        }
    }
}
