import platform
import socket
import urllib.request
import json

def collect_system_info():
    print("🔍 Collecte des informations de diagnostic en cours...")
    
    # 1. Informations Système
    info = {
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "hostname": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname())
    }
    
    # 2. Tentative de récupération de l'IP publique
    try:
        info["public_ip"] = urllib.request.urlopen('https://api.ipify.org', timeout=3).read().decode('utf8')
    except Exception:
        info["public_ip"] = "Inconnue (Pas d'accès internet)"
        
    return info

def display_diagnostic():
    data = collect_system_info()
    print("\n==========================================")
    print("       RAPPORT DE DIAGNOSTIC PMAD         ")
    print("==========================================")
    print(f"🖥️  Système d'exploitation : {data['os']} {data['os_release']} ({data['architecture']})")
    print(f"Nom de la machine     : {data['hostname']}")
    print(f"🌐 IP Locale          : {data['local_ip']}")
    print(f"🌍 IP Publique        : {data['public_ip']}")
    print("==========================================\n")

if __name__ == "__main__":
    display_diagnostic()
