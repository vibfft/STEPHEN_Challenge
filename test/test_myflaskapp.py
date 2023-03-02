import unittest
import docker

class TestServerConfig(unittest.TestCase):
    def setUp(self):
        # Connect to the Docker API
        self.docker_client = docker.from_env()

        # Start the Docker container
        self.container = self.docker_client.containers.run(
            'myflaskapp',
            detach=True,
            ports={'80/tcp': ('127.0.0.1', 80), '443/tcp': ('127.0.0.1', 443)}
        )

    def tearDown(self):
        # Stop and remove the Docker container
        self.container.stop()
        self.container.remove()

    def test_ports_exposed(self):
        # Check that the container has port 80 exposed
        ports = self.container.attrs['HostConfig']['PortBindings']
        self.assertIn('80/tcp', ports)
        self.assertIn('443/tcp', ports)

        # Check that port 80 is mapped to the correct host port
        port_mapping = ports['80/tcp'][0]
        self.assertEqual(port_mapping['HostIp'], '127.0.0.1')
        self.assertEqual(port_mapping['HostPort'], '80')

        # Check that port 443 is mapped to the correct host port
        port_mapping = ports['443/tcp'][0]
        self.assertEqual(port_mapping['HostIp'], '127.0.0.1')
        self.assertEqual(port_mapping['HostPort'], '443')


if __name__ == '__main__':
    unittest.main()