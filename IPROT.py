#!/usr/bin/env python3

import os
import sys
import time
import platform
import subprocess
import signal

ASCII_ART = """
██╗██████╗ ██████╗  ██████╗ ████████╗
██║██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║██████╔╝██████╔╝██║   ██║   ██║   
██║██╔═══╝ ██╔══██╗██║   ██║   ██║   
██║██║     ██║  ██║╚██████╔╝   ██║   
╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   
"""
print("by quadraturbo <3\n")

def signal_handler(sig, frame):
    print("\n[!] Deteniendo IPROT...")
    sys.exit(0)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_tor_installed(os_type):
    try:
        if os_type == "windows":
            result = subprocess.run(["where", "tor"], capture_output=True, text=True)
        else:
            result = subprocess.run(["which", "tor"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False

def start_tor(os_type):
    try:
        if os_type == "windows":
            subprocess.Popen(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
        return True
    except:
        return False

def rotate_ip():
    try:
        if os.name == 'nt':
            subprocess.run('echo AUTHENTICATE | nc 127.0.0.1 9051', shell=True, capture_output=True)
            subprocess.run('echo "SIGNAL NEWNYM" | nc 127.0.0.1 9051', shell=True, capture_output=True)
        else:
            subprocess.run('echo -e "AUTHENTICATE\nSIGNAL NEWNYM" | nc 127.0.0.1 9051', shell=True, capture_output=True)
        return True
    except:
        return False

def get_current_ip():
    try:
        if os.name == 'nt':
            result = subprocess.run(
                'curl -s --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/api/ip',
                shell=True,
                capture_output=True,
                text=True
            )
        else:
            result = subprocess.run(
                ['curl', '-s', '--socks5-hostname', '127.0.0.1:9050', 'https://check.torproject.org/api/ip'],
                capture_output=True,
                text=True
            )
        
        if result.returncode == 0 and result.stdout:
            import json
            data = json.loads(result.stdout)
            return data.get('IP', 'Unknown')
        return "Unknown"
    except:
        return "Unknown"

def main():
    signal.signal(signal.SIGINT, signal_handler)
    
    clear_screen()
    print(ASCII_ART)
    print("=" * 50)
    
    print("\n[?] Sistema operativo:")
    print("1. Windows")
    print("2. Linux")
    os_choice = input("\nSelecciona (1/2): ").strip()
    
    os_type = "windows" if os_choice == "1" else "linux"
    
    print(f"\n[+] Sistema seleccionado: {os_type.upper()}")
    
    if not check_tor_installed(os_type):
        print("[!] TOR no está instalado en el sistema")
        print("[!] Instala TOR antes de continuar")
        sys.exit(1)
    
    interval = input("\n[?] Intervalo de rotación en segundos: ").strip()
    
    try:
        interval = int(interval)
        if interval < 1:
            print("[!] El intervalo debe ser mayor a 0")
            sys.exit(1)
    except ValueError:
        print("[!] Valor inválido")
        sys.exit(1)
    
    print("\n[+] Iniciando TOR...")
    if not start_tor(os_type):
        print("[!] Error al iniciar TOR")
        sys.exit(1)
    
    print("[+] TOR iniciado correctamente")
    print(f"[+] Rotación configurada cada {interval} segundos")
    print("\n[*] Presiona Ctrl+C para detener\n")
    
    rotation_count = 0
    
    while True:
        try:
            current_ip = get_current_ip()
            print(f"[{rotation_count}] IP actual: {current_ip}")
            
            time.sleep(interval)
            
            print(f"[*] Rotando IP...")
            if rotate_ip():
                rotation_count += 1
                time.sleep(2)
                new_ip = get_current_ip()
                print(f"[✓] Nueva IP: {new_ip}\n")
            else:
                print("[!] Error al rotar IP\n")
                
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(interval)

if __name__ == "__main__":
    main()
