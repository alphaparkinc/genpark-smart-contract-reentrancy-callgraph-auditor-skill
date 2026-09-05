from client import SmartContractReentrancyCallgraphAuditorClient

def main():
    client = SmartContractReentrancyCallgraphAuditorClient()
    res = client.audit_contract_callgraph()
    print('Reentrancy Callgraph Auditor: ' + res['audit_id'] + ' (' + res['contract_name'] + '.' + res['function_name'] + ')')
    print('Vulnerable: ' + str(res['reentrancy_vulnerable']) + ' | CEI Compliant: ' + str(res['checks_effects_interactions_pattern_strictly_followed']))
    print('Report URL: ' + res['audit_report_url'])

if __name__ == '__main__':
    main()
