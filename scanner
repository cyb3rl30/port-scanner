import socket

def scan_ports(host, ports):
    print(f"🔍 Escaneando {host}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"✅ Porta {port} aberta")
            else:
                print(f"❌ Porta {port} fechada")
            sock.close()
        except Exception as e:
            print(f"Erro na porta {port}: {e}")

if __name__ == "__main__":
    alvo = input("Digite o host ou IP para escanear: ")
    portas = [21, 22, 80, 443, 3306]  # portas comuns
    scan_ports(alvo, portas)
