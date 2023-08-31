from django.test import TestCase
from .models import blogs
from django.contrib.auth.models import User
from django.shortcuts import reverse


class blogs_test(TestCase):
    @classmethod
    def setUpTestData(cls):   # it can do just one time for all def test
                            # setUpTestData is not an object, it is on the level of class.
        cls.user1 = User.objects.create(username='fatemeh')
        cls.post1 = blogs.objects.create(
            title='test post',
            text='This is a test post!',
            status=blogs.STATUS_CHOICE[0][0],
            author=cls.user1,

        )
        cls.post2 = blogs.objects.create(
            title='test post2',
            text='This is a test post!22',
            status=blogs.STATUS_CHOICE[1][0],
            author=cls.user1,

        )

    # def setUp(self):   # it repeat for every def test
    #     user1 = User.objects.create(username='fatemeh')
    #     self.post1 = blogs.objects.create(
    #         title='test post',
    #         text='This is a test post!',
    #         status=blogs.STATUS_CHOICE[0][0],
    #         author=user1,
    #     )
    #     self.post2 = blogs.objects.create(
    #         title='test post2',
    #         text='This is a test post!22',
    #         status=blogs.STATUS_CHOICE[1][0],
    #         author=user1,
    #     )
    def test_blogs_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_detail_post(self):
        # response = self.client.get(reverse('blog'))
        self.assertEqual(blogs.objects.last().title, self.post2.title)

    def test_url_blog(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_name_blog(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_url_blog_detail(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_name_blog_detail(self):
        response = self.client.get(reverse('detail_view', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog(self):
        response = self.client.get(reverse('blog'))
        self.assertContains(response, self.post1.title)

    def test_post_title_detail_view(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_draft_not_show_post(self):  # Test Driven Development TDD
        response = self.client.get(reverse('blog'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_create_post(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'post_testi',
            'text': 'this is for testi',
            'status': 'POP',
            'author': self.user1.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(blogs.objects.last().title, 'post_testi')
        self.assertEqual(blogs.objects.last().text, 'this is for testi')

    def test_update_post(self):
        response = self.client.post(reverse('update_post', args=[self.post2.id]), {
            'title': 'post_testi1',
            'text': 'this is for testi1',
            'status': 'POP',
            'author': self.user1.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(blogs.objects.last().title, 'post_testi1')
        self.assertEqual(blogs.objects.last().text, 'this is for testi1')

    def test_delete_post(self):
        response = self.client.post(reverse('delete_post', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(blogs.objects.last().title, 'test post')
        self.assertEqual(blogs.objects.last().text, self.post1.text)


