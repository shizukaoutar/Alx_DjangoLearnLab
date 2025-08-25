from rest_framework.test import APITestCase
from rest_framework import status



class BookAPITest(APITestCase):
    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
    
    def test_create_book(self):
        response = self.client.post('/api/books/', {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2022,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
    
    def test_update_book(self):
        response = self.client.put('/api/books/1/', {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2023,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)  

    def test_delete_book(self):
        response = self.client.delete('/api/books/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
