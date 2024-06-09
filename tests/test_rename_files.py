import unittest
from pathlib import Path
import shutil
import os
from imageRenamer.rename_files import rename_files


class TestRenameFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = Path('test_images')
        self.test_dir.mkdir(exist_ok=True)
        # Create some dummy files
        for i in range(12):
            (self.test_dir / f'test_image_{i}.jpg').touch()

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_rename_files(self):
        new_filenames = [
            'office_space_', 'coworking_', 'office_for_rent_', 'furnished_office_',
            'conference_rooms_', 'executive_suites_', 'serviced_office_',
            'meeting_room_', 'shared_office_space_'
        ]
        rename_files(self.test_dir, new_filenames)

        # Check if files are renamed correctly
        files = list(self.test_dir.iterdir())
        self.assertEqual(len(files), 12)
        self.assertTrue(all('new_york' in file.name for file in files))

if __name__ == '__main__':
    unittest.main()
