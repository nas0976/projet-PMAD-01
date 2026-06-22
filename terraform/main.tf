terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# 1. Création du réseau bridge isolé
resource "docker_network" "pmad_network" {
  name = "pmad-private-network"
}

# 2. Déploiement du conteneur Jenkins
resource "docker_container" "jenkins" {
  name  = "jenkins-devops"
  image = "jenkins/jenkins:lts"

  networks_advanced {
    name = docker_network.pmad_network.name
  }

  ports {
    internal = 8080
    external = 8080
  }
}
