import socket
import sys

def scan_ports(host, ports):
    try:
        # Resolve o nome do host para IP (validação de rede)
        target_ip = socket.gethostbyname(host)
        print(f"\n" + "="*40)
        print(f"🔍 Escaneando Alvo: {host} ({target_ip})")
        print("="*40 + "\n")
    except socket.gaierror:
        print(f"❌ Erro: Não foi possível resolver o host '{host}'.")
        return

    for port in ports:
        # Cria o socket usando o gerenciador de contexto 'with'
        # Isso garante que o socket seja fechado automaticamente
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.8) # Um pouco mais de tempo para conexões lentas
            result = sock.connect_ex((target_ip, port))
            
            status = "ABERTA" if result == 0 else "FECHADA"
            icon = "✅" if result == 0 else "❌"
            
            # Formatação em colunas para o terminal
            print(f"{icon} Porta {port:<5} | Status: {status}")

if __name__ == "__main__":
    try:
        alvo = input("Digite o host ou IP: ").strip()
        if not alvo:
            print("Por favor, insira um alvo válido.")
            sys.exit()

        # Lista expandida com portas de serviços comuns
        portas_comuns = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 8080]
        scan_ports(alvo, portas_comuns)
        
    except KeyboardInterrupt:
        print("\n\n[-] Escaneamento interrompido pelo usuário.")
        sys.exit()
