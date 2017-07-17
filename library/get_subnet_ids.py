#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

# WANTS_JSON

fields = {"subnets": {"required": True, "type": "list"}}

def main():
    m = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    if "subnets" not in m.params.keys() or len(m.params["subnets"]) < 1:
        m.fail_json(msg="No subnets present in param")

    subnets = m.params["subnets"]
    retval = [i['subnet']['id'] for i in subnets]

    m.exit_json(failed=False, changed=False, msg="Ding!", subnets=retval)

if __name__ == '__main__':
    main()
