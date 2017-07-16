#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

# WANTS_JSON

fields = {"route_tables": {"required": True, "type": "list"}}

def main():
    m = AnsibleModule(argument_spec=fields, supports_check_mode=True)

    if "route_tables" not in m.params.keys() or len(m.params["route_tables"]) < 1:
        m.fail_json(msg="No route_tables present in param")

    rtbs = m.params["route_tables"]
    retval = {}
    for rtb in rtbs:
        # default to deleteable
        retval[rtb['id']] = True

        if 'associations' in rtb.keys():
            if True in [i['main'] for i in rtb['associations']]:
                # route table contains an association marked "main", not deleteable
                retval[rtb['id']] = False
                continue

    m.exit_json(failed=False, changed=False, msg="Ding!", deleteable=retval)

if __name__ == '__main__':
    main()
