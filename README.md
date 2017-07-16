# ec2-vpc

## What?

Creates a new VPC, public subnets, and an internet gateway.

## Why?

Provide a simple self-contained interface.

## How?

```yaml
service_env: 'dev'        # actual VPC name will have this appended ie: name_env
service_state: 'present'  # set to 'absent' to tear things down after

vpc_name: 'test'
vpc_cidr: '10.0.0.0/16'
vpc_region: 'us-east-1'
vpc_public_subnet_cidrs:
  - '10.0.1.0/24'         # whatever you please for subnetting
  - '10.0.2.0/24'         # just have to calculate it yourself
vpc_public_subnet_azs:
  '10.0.1.0/24': 'a'      # these keys much match values in vpc_public_subnet_cidrs
  '10.0.2.0/24': 'b'      # can have extra here, but need to cover all values in ^
```

## Under the Hood

### library/rtb_deleteable.py

This is a simple module meant to parse the facts returned by ec2_vpc_route_table_facts.
It reads in the dict it produces and produces a dict where keys are route table IDs,
and values are a boolean indicating if the route table is safe to delete. It does
this by checking for the flag which marks the "main" route table.

#### Why?

The "main" route table cannot be deleted, except by deleting the VPC, so we need
to skip it. However, digging into a dict like that with pure Ansible is painful/
impossible. Thankfully, adding a hacky little Python script to an Ansible role
is pretty easy.
