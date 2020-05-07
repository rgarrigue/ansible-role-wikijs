import os
import pytest
import requests
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("name", ["nodejs", "tar"])
def test_packages(host, name):
    p = host.package(name)
    assert p.is_installed


@pytest.mark.parametrize(
    "path",
    ["/etc/systemd/system/wikijs.service", "/srv/wikijs", "/srv/wikijs/config.yml"],
)
def test_files(host, path):
    f = host.file(path)
    assert f.exists


def test_user(host):
    u = host.user("wikijs")
    assert u.exists


@pytest.mark.parametrize("name", ["wikijs"])
def test_services(host, name):
    s = host.service(name)
    assert s.is_running
    assert s.is_enabled


def test_wikijs(host):
    ip = host.interface("eth0").addresses[0]
    get = requests.get("http://" + ip + ":3000/")
    assert get.status_code == 200
    assert 'wiki-version="2.' in get.text
