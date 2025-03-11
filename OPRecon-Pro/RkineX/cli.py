import argparse
from .scanner import OPReconScanner
from tabulate import tabulate

def banner() -> None:
    print(r"""
     ____  ____  ____  ___  ____  _____
    / __ \/ __ \/ __ \/ _ \/ __ \/ ___/
   / /_/ / /_/ / /_/ /  __/ / / / __/ 
  / .___/\____/ .___/\___/_/ /_/____/  
 /_/        /_/        Recon Tool v2.0
    """)

def main():
    parser = argparse.ArgumentParser(description="OPRecon Pro - Advanced Network Scanner")
    parser.add_argument("target", help="Target IP/Domain")
    parser.add_argument("-p", "--ports", action="store_true", help="Full port scan")
    parser.add_argument("-s", "--services", action="store_true", help="Service detection")
    parser.add_argument("-d", "--dns", action="store_true", help="DNS enumeration")
    parser.add_argument("-w", "--web", action="store_true", help="Web technology detection")
    
    args = parser.parse_args()
    scanner = OPReconScanner(args.target)
    
    if args.ports:
        print("\n[+] Port Scanning Results:")
        ports = scanner.full_scan()
        print(tabulate(
            [(port, service) for port, service in ports.items()],
            headers=["Port", "Service"]
        ))

    if args.services:
        print("\n[+] Service Detection:")
        services = scanner.service_detection()
        print(tabulate(
            [(port, data['name'], data['version']) for port, data in services.items()],
            headers=["Port", "Service", "Version"]
        ))

    if args.dns:
        print("\n[+] DNS Records:")
        dns_info = scanner.dns_enumerate()
        for rtype, records in dns_info.items():
            print(f"{rtype}: {', '.join(records)}")

    if args.web:
        print("\n[+] Web Technologies:")
        web_info = scanner.web_tech_detect()
        print(tabulate(web_info.items(), tablefmt="plain"))

if __name__ == "__main__":
    banner()
    main()
