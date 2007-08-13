from pylonssite.tests import *


class TestPagesController(TestController):
    def test_index(self):
        url = url_for('directory_pages', directory_id='root')
        assert url == '/directories/root/pages'
        response = self.app.get(url)
        # Test response...
