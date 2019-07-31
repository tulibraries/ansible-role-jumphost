import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('instance')


def test_hosts_file(host):
    f = host.file('/tmp/ssh_config')
    assert f.exists
    proxyline = """
    ProxyCommand ssh -o StrictHostKeyChecking=no \
    -W %h:%p -q root@otherhost -p 9229
    """
    assert f.contains(proxyline)
    assert f.contains("Host instance")
    assert f.contains("Host otherhost")
