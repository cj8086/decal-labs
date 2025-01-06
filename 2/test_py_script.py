import unittest
import os
import subprocess

### Run this in current directory.

script_path = os.getenv("SCRIPT_PATH", "./phonebook_skeleton.py")
pb_path = os.getenv("PB_PATH", "./python_phonebook_entries")


class PhoneBookTestBase(unittest.TestCase):
    def setUp(self):
        if os.path.exists(pb_path):
            os.remove(pb_path)

    def tearDown(self):
        if os.path.exists(pb_path):
            os.remove(pb_path)


class TestPhoneBookNew(PhoneBookTestBase):
    def test_pb_new(self):
        pname, pnumber = "Linus Torvalds", "111-222-333"
        result = subprocess.run(
            ["python3", script_path, "new", pname, pnumber],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )

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
        result = subprocess.run(
            ["python3", script_path, "clear"],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )

        self.assertFalse(os.path.exists(pb_path))


class TestPhoneBookList(PhoneBookTestBase):
    lines = [
        "Linus Torvalds 111-222-3333\n",
        "Linus Torvalds 888-999-9191\n",
        "Tux 123-456-7890\n",
    ]

    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            for line in self.lines:
                f.write(line)

    def test_pb_list(self):
        result = subprocess.run(
            ["python3", script_path, "list"],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        self.assertEqual(result.stdout, "".join(self.lines))

        self.assertTrue(os.path.exists(pb_path))


class TestPhoneBookLookup(PhoneBookTestBase):
    lines = [
        "Linus Torvalds 111-222-3333\n",
        "Linus Torvalds 888-999-9191\n",
        "Tux 123-456-7890\n",
    ]

    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            for line in self.lines:
                f.write(line)

    def test_pb_lookup(self):
        result = subprocess.run(
            ["python3", script_path, "lookup", "Linus Torvalds"],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        self.assertEqual(result.stdout, "".join(self.lines[0:2]))
        self.assertTrue(os.path.exists(pb_path))


class TestPhoneBookRemove(PhoneBookTestBase):
    lines = [
        "Linus Torvalds 111-222-3333\n",
        "Linus Torvalds 888-999-9191\n",
        "Tux 123-456-7890\n",
    ]

    def setUp(self):
        super().setUp()
        with open(pb_path, "w") as f:
            for line in self.lines:
                f.write(line)

    def test_pb_remove(self):
        subprocess.run(
            ["python3", script_path, "remove", "Linus Torvalds"],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        with open(pb_path, "r") as f:
            content = f.read()
            self.assertEqual(content, "".join(self.lines[2]))


if __name__ == "__main__":
    unittest.main()