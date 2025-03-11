import socket
import concurrent.futures
from typing import List, Dict
import nmap
import dns.resolver
import requests
from urllib.parse import urlparse

class OPReconScanner:
    def __init__(self, target: str, threads: int = 100):
        self.target = target
        self.threads = threads
        self.nm = nmap.PortScanner()
        self.results: Dict[int, str] = {}

    def port_scan(self, port: int) -> None:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                service = socket.getservbyport(port, 'tcp') if result == 0 else None
                if result == 0:
                    self.results[port] = service or 'unknown'
        except (socket.error, socket.herror, socket.gaierror):
            pass

    def full_scan(self) -> Dict[int, str]:
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.port_scan, range(1, 65535))
        return self.results

    def service_detection(self) -> Dict[str, str]:
        self.nm.scan(self.target, arguments='-sV')
        return self.nm[self.target]['tcp']

    def dns_enumerate(self) -> Dict[str, List[str]]:
        records = {}
        record_types = ['A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT']
        for rtype in record_types:
            try:
                answers = dns.resolver.resolve(self.target, rtype)
                records[rtype] = [str(r) for r in answers]
            except dns.resolver.NoAnswer:
                continue
        return records

    def web_tech_detect(self) -> Dict[str, str]:
        headers = requests.get(f"http://{self.target}").headers
        return {
            'Server': headers.get('Server'),
            'X-Powered-By': headers.get('X-Powered-By'),
            'Cookies': headers.get('Set-Cookie')
        }
