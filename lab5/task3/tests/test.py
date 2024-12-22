# lab5/task3/tests/test.py

import unittest
import os

from lab5.task3.src.network_packets import (
    task3, PATH, OUTPUT_PATH, simulate_network
)

class TestNetworkPackets(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab5\task3\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab5\task3\txtf\test_output.txt"

        self.original_path = PATH
        self.original_output_path = OUTPUT_PATH
        self._override_global_paths()

    def tearDown(self):
        self._restore_global_paths()
        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        import lab5.task3.src.network_packets as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab5.task3.src.network_packets as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, S, packets):
        """
        S - размер буфера
        packets - список (Ai, Pi)
        """
        n = len(packets)
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(f"{S} {n}\n")
            for (A, P) in packets:
                f.write(f"{A} {P}\n")

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def test_no_packets(self):
        # S=1, n=0 => вывод ничего
        self.write_test_file(1, [])
        task3()
        result = self.read_output_file()
        self.assertEqual(result, [])

    def test_single_packet(self):
        # S=1, n=1 => arrives=0, processing=0 => start=0
        packets = [(0, 0)]
        self.write_test_file(1, packets)
        task3()
        result = self.read_output_file()
        self.assertEqual(result, ["0"])

    def test_buffer_overflow(self):
        # S=1, n=2 => first= arrives=0, p=1 => start=0 => finish=1
        # second= also arrives=0, p=1 => buffer is full => drop => -1
        packets = [(0, 1), (0, 1)]
        self.write_test_file(1, packets)
        task3()
        result = self.read_output_file()
        self.assertEqual(result, ["0", "-1"])

    def test_sequential(self):
        # S=1, n=2 => first=0,1 => start=0 finish=1
        # second=1,1 => when arrives=1 => finish_times[0]=1 => it's done => buffer free => start=1
        packets = [(0,1), (1,1)]
        self.write_test_file(1, packets)
        task3()
        result = self.read_output_file()
        self.assertEqual(result, ["0", "1"])

    def test_simulate_network_function(self):
        # direct tests
        # S=1, packets=[(0,1), (0,1)] => [0, -1]
        res = simulate_network(1, [(0,1), (0,1)])
        self.assertEqual(res, [0, -1])

        # S=1, packets=[(0,1), (1,1)] => [0,1]
        res = simulate_network(1, [(0,1), (1,1)])
        self.assertEqual(res, [0,1])

if __name__ == '__main__':
    unittest.main()
