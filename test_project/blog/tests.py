import requests
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import post_detail


class TestBlogView(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.post_url = reverse('post-details', kwargs={'post_id':1})
        self.html = """
<head>
    <title>First Post</title>
</head>
<body>
    
    <ul>
        
            <li>First comment</li>
        
            <li>Second comment</li>
        
            <li>Comment via POSTMAN</li>
        
    </ul>
    
</body>
"""

    def test_post_get(self):
        request = self.factory.get(f'{"192.168.0.101:8000"}{self.post_url}')
        response = post_detail(request, 1)
        self.assertEqual(response.status_code, 200)
        self.assertHTMLEqual(str(response.content), str(response.content))

