import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_readonly(Command, File, Sudo):
    f = '/mnt/ro/hello'
    with Sudo('test'):
        c = Command('touch %s', f)
    assert c.rc == 1
    assert not File(f).exists


def test_readwrite(Command, File, Sudo):
    f = '/mnt/rw/hello'
    with Sudo('test'):
        c1 = Command('touch %s', f)
    assert c1.rc == 0
    assert File(f).exists
    with Sudo('test'):
        c2 = Command('rm %s', f)
    assert c2.rc == 0
    assert not File(f).exists
