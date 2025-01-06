import unittest
import os
import subprocess




script_path = "./phonebook_skeleton.sh"
pb_path = "./bash_phonebook_entries"

class PhoneBookTestBase(unittest.TestCase):
    def setUp(self):
        self.assertFalse(os.path.exists(pb_path), f"{pb_path} should not exist before setup")

    def tearDown(self):
        if os.path.exists(pb_path):
            os.remove(pb_path)

    def run_script(self, command, *args):
        try:
            result = subprocess.run(
                ["bash", script_path, command, *args],
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                text=True,
                check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            raise


class TestPhoneBookNew(PhoneBookTestBase):
    def test_pb_new(self):
        pname, pnumber = "Linus Torvalds", "111-222-333"
        result = self.run_script("new", pname, pnumber)
        self.assertTrue(os.path.exists(pb_path))
        with open(pb_path, "r") as f:
            content = f.read()
        self.assertIn(f"{pname} {pnumber}", content)


class TestPhoneBookClear(PhoneBookTestBase):
    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            f.write("Linus Torvalds 111-222-333\n")

    def test_pb_clear(self):
        result = self.run_script("clear")
        self.assertFalse(os.path.exists(pb_path))


lines = [
    "Linus Torvalds 111-222-3333\n",
    "Linus Torvalds 888-999-9191\n",
    "Tux 123-456-7890\n",
]


class TestPhoneBookList(PhoneBookTestBase):
    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            for line in lines:
                f.write(line)

    def test_pb_list(self):
        result = self.run_script("list")
        self.assertEqual(result.stdout, "".join(lines))
        self.assertTrue(os.path.exists(pb_path))


class TestPhoneBookLookup(PhoneBookTestBase):
    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            for line in lines:
                f.write(line)

    def test_pb_lookup(self):
        result = self.run_script("lookup", "Linus Torvalds")
        expected_output = "".join(lines[0:2])
        self.assertEqual(result.stdout, expected_output)
        self.assertTrue(os.path.exists(pb_path))


class TestPhoneBookRemove(PhoneBookTestBase):
    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            for line in lines:
                f.write(line)

    def test_pb_remove(self):
        self.run_script("remove", "Linus Torvalds")

        with open(pb_path, "r") as f:
            content = f.read()
        self.assertEqual(content, "".join(lines[2]))


if __name__ == "__main__":
    unittest.main()