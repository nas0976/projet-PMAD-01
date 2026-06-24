import sys
import subprocess
from agent_diagnostic import display_diagnostic

# Configuration de l'infrastructure PMAD (Kubernetes)
# On utilise l'IP publique détectée ou localhost pour tes tests locaux
RELAY_SERVER = "176.140.221.243:21117"
ID_SERVER = "176.140.221.243:21116"
PUBLIC_KEY = "krlNvdJn8X8q9IhpYqi5XO3kJziw6hb6ltnKD+4Hv7k="

def start_rustdesk_client():
    print("🚀 Initialisation du lien de maintenance à distance chiffré...")
    print(f"🔗 Connexion au serveur de signalement : {ID_SERVER}")
    
    # Commande théorique pour lancer le binaire RustDesk en lui injectant les paramètres du cluster PMAD
    # --id-server et --relay-server configurent les endpoints
    # --key force le chiffrement Ed25519 validé au Sprint 5
    rustdesk_cmd = [
        "rustdesk", 
        "--id-server", ID_SERVER,
        "--relay-server", RELAY_SERVER,
        "--key", PUBLIC_KEY
    ]
    
    print(f"💻 Commande d'exécution générée : {' '.join(rustdesk_cmd)}")
    print("\n✅ L'agent PMAD est prêt et configuré de manière sécurisée.")
    
    # Dans un environnement avec interface graphique, on lèverait le sous-processus ici :
    # subprocess.Popen(rustdesk_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    # 1. Lancement du diagnostic système
    display_diagnostic()
    
    # 2. Configuration et démarrage de l'infrastructure de prise en main
    start_rustdesk_client()

if __name__ == "__main__":
    main()
