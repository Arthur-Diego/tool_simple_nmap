import subprocess
from ipaddress import ip_address


def icmp_scan_menu():
    print("Escolha uma opção de varredura ICMP:")
    print("1. Ping simples em um único host")
    print("2. Ping em uma faixa de IPs")
    print("3. Ping em uma lista de hosts a partir de um arquivo")
    print("4. Ping em um intervalo de IPs")
    print("5. Ping com detecção de hosts vivos")

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        host = input("Digite o endereço IP do host: ")
        icmp_ping(host)
    elif choice == '2':
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        icmp_ping(ip_range)
    elif choice == '3':
        hosts_file = input("Digite o caminho do arquivo com a lista de hosts: ")
        icmp_ping_from_file(hosts_file)
    elif choice == '4':
        start_ip = input("Digite o endereço IP inicial: ")
        end_ip = input("Digite o endereço IP final: ")
        icmp_ping_range(start_ip, end_ip)
    elif choice == '5':
        network = input("Digite a rede (exemplo: 192.168.1.0/24): ")
        icmp_ping_live_hosts(network)
    else:
        print("Opção inválida.")


def icmp_ping(target, options=""):
    command = ["ping", "-c", "4", target]
    execute_ping(command)


def icmp_ping_from_file(file_path):
    with open(file_path, 'r') as file:
        hosts = file.readlines()
        for host in hosts:
            host = host.strip()
            icmp_ping(host)


def icmp_ping_range(start_ip, end_ip):
    start = ip_address(start_ip)
    end = ip_address(end_ip)

    for ip_int in range(int(start), int(end) + 1):
        ip = ip_address(ip_int)
        icmp_ping(str(ip))


def icmp_ping_live_hosts(network):
    command = ["nmap", "-sn", network]
    execute_nmap_scan(command)


def execute_ping(command):
    try:
        print("Comando executado: {}".format(" ".join(command)))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")
    except KeyboardInterrupt:
        print("Comando interrompido pelo usuário.")


def execute_nmap_scan(command):
    try:
        print("Comando executado: {}".format(" ".join(command)))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")
    except KeyboardInterrupt:
        print("Comando interrompido pelo usuário.")