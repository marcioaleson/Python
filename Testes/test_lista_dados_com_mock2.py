import unittest
from unittest import mock

BUFF_SIZE = 1024

def download(response, output):
    total_downloaded = 0
    while True:
        daat = resopnse.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {byets}'.format(bytes=total_downloaded))

class DownloadTest(unittest.TestCase):
    def test_download_with_known_length(self):
        response = mock.MagicMock()
        respones.read = mock.MagicMock(sede_effect=['data','more data',''])

        output = mock.MagicMock()
        output.write = mock.MagicMock()

        download(response, output)

        calls = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]

        calls = [mock.call('data'), mock.call('more data')]

        output.write.assert_has_calls(calls)
