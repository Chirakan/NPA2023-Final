import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback64070130"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback64070130",
        "description": "Loopback64070130 for Final NPA2023",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.30.130.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
} 

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers,  
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        if(resp.status_code == 204):
            return "Cannot create: Interface loopback 64070130"
        else:
            return "Interface loopback 64070130 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070130 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback 64070130"


def enable():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback64070130",
        "description": "Enable Loopback64070130",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.30.130.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
} 

    resp_get = requests.get(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp_get.status_code >= 200 and resp_get.status_code <= 299):
        print("Interface STATUS OK: {}".format(resp_get.status_code))
        resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )
        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
            return "Interface loopback 64070130 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp_get.status_code))
        return "Cannot enable: Interface loopback 64070130"


def disable():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback64070130",
        "description": "Enable Loopback64070130",
        "type": "iana-if-type:softwareLoopback",
        "enabled": False,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.30.130.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
} 

    resp_get = requests.get(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp_get.status_code >= 200 and resp_get.status_code <= 299):
        print("Interface STATUS OK: {}".format(resp_get.status_code))
        resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )
        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
            return "Interface loopback 64070130 is shutdowned successfully"
    else:
        print('Error. Status Code: {}'.format(resp_get.status_code))
        return "Cannot shutdown: Interface loopback 64070130"


def status():
    api_url_status = api_url

    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = ((resp.status_code >= 200 and resp.status_code <= 299) and "up") or (resp.status_code > 299 and "down")
        oper_status = (response_json["ietf-interfaces:interface"]["enabled"] == True and "up") or (response_json["ietf-interfaces:interface"]["enabled"] == False and "down")
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 64070130 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 64070130 is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 64070130"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
