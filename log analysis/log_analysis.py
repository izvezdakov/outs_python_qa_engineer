import argparse
import collections
import fnmatch
import json
import os
import re


class Parser:
    total_number_of_completed_requests = 0
    ip_addresses_counts = collections.defaultdict(int)
    top_three_ips = []
    top_used_methods = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0, 'HEAD': 0, 'CONNECT': 0, 'OPTIONS': 0, 'TRACE': 0}
    top_long_requests = collections.defaultdict(int)
    top_three_long_request = []
    answer = {}

    def process(self, line: str):
        self.total_number_of_completed_requests += 1
        req_expr = '(?P<ip>\d+.\d+.\d+.\d+).*(?P<date>\[.*]) \\"(?P<method>\w+) (?P<url>.*\\") (?P<duration>.\d*)'
        parse_string = re.search(req_expr, line)
        self.ip_addresses_counts[parse_string.groupdict()['ip']] += 1
        self.top_used_methods[parse_string.groupdict()['method']] += 1
        uniq_query = line[:re.search(r'\" \d.. ', line).span()[0]]
        self.top_long_requests[uniq_query] = int(parse_string.groupdict()['duration'])

    def calculate_statistic(self):
        max_request = set(sorted(self.ip_addresses_counts.values(), reverse=True)[:3])
        for ip in self.ip_addresses_counts.keys():
            if len(self.top_three_ips) > 2:
                break
            if self.ip_addresses_counts[ip] in max_request:
                self.top_three_ips.append(ip)

        longest_request = set(sorted(self.top_long_requests.values(), reverse=True)[:3])
        for request in self.top_long_requests.keys():
            if len(self.top_three_long_request) > 2:
                break
            if self.top_long_requests[request] in longest_request:
                self.top_three_long_request.append(request)

        self.answer.update({
            'total number of completed requests': self.total_number_of_completed_requests,
            'number of requests by HTTP methods:': self.top_used_methods,
            'top 3 IP addresses from which requests were made': self.top_three_ips,
            'top 3 longest queries': self.top_three_long_request
        })

    def print_statistic(self):
        out_str = f'Общее количество выполненных запросов: {self.total_number_of_completed_requests};\n'
        out_str += '\n'
        out_str += f'Количество запросов по HTTP-методам:\n'
        for k in self.top_used_methods.keys():
            out_str += f'    {k}:    {self.top_used_methods[k]},\n'
        out_str += '\n'
        out_str += 'Топ 3 IP адресов с которых были сделаны запросы:\n'
        for i in self.top_three_ips:
            out_str += f'    {i},\n'
        out_str += '\n'
        out_str += 'Топ 3 самых долгих запроса:\n'
        for i in self.top_three_long_request:
            out_str += f'    {i},\n'
        print(out_str)

    def save_statistic_to_json(self):
        with open('statistic.json', 'w') as f:
            json.dump(self.answer, f)


def main():
    access_parser = Parser()
    parser = argparse.ArgumentParser(description="Log parser")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--directory", type=str,
                       help="Directory. If this parameter is passed, all *.log files in directory "
                            "will be processed."
                            "If script was called without parameters, only access.log "
                            "in current directory will be processed.")

    group.add_argument("-f", "--file", type=str, help="File. If this parameter is passed, just this file will be "
                                                      "processed. Files in the directory will NOT be processed. "
                                                      "If script was called without parameters, only access.log "
                                                      "in current directory will be processed.")
    args = parser.parse_args()
    if args.directory:
        # parse all *.log file in directory
        files = os.listdir(args.directory)
        pattern = "*.log"
        for entry in files:
            if fnmatch.fnmatch(entry, pattern):
                with open(entry) as f:
                    for line in f:
                        access_parser.process(line)
    elif args.file:
        # parse only file in param -f
        with open(args.file) as f:
            for line in f:
                access_parser.process(line)
    else:
        # parse only access.log
        with open("access.log") as f:
            for line in f:
                access_parser.process(line)
    access_parser.calculate_statistic()
    access_parser.save_statistic_to_json()
    access_parser.print_statistic()


if __name__ == '__main__':
    main()
