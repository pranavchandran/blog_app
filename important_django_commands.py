'''
how to use shell in Django
python3 manage.py shell
from django.contrib.auth.models import User
from blog.models import Post
user = User.objects.get(username='root')
post = Post(title='Another post',slug='another post',body='Post body',author=user)
post.save()
Post.objects.create(title='One more post', slug='one-more-post', body='Post body', author=user);

Updating the saved post
p = Post.objects.get(title='Another post')
p.title = 'Pranav'
p.save()

Using Filter method
Post.objects.filter(publish__year=2021)
Post.objects.filter(publish__year=2020,author__username='admin')

Exclude
Post.objects.filter(publish__year=2020).exclude(title__startswith='Why')

Orderby asc and desc
Post.object.order_by('title')
Post.object.order_by('-title')

Delete
post = Post.objects.get(id=1)
post.delete()

Created PublishedManager() filter the status published override
Post.published.filter(title__startswith='Pranav')
'''


