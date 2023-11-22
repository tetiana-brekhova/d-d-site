from django.db import models
from ..authentication.models import CustomUser


class Post(models.Model):

    post_name = models.CharField(blank=True, max_length=128)
    post_body = models.CharField(blank=True)
    post_data = models.DateField(auto_now_add=True)
    post_image = models.ImageField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)


    def __repr__(self):
        return f"Post(id={self.post_name})"

    @staticmethod
    def get_by_id(post_id):
        return Post.objects.get(id=post_id) if Post.objects.filter(id=post_id) else None

    @staticmethod
    def delete_by_id(post_id):
        if Post.get_by_id(post_id) is None:
            return False
        Post.objects.get(id=post_id).delete()
        return True

    @staticmethod
    def create(user, post_name, post_body, post_data, post_image):

        try:
            post = Post(user=user, upost_name=post_name, post_body=post_body, post_data=post_data, post_image=post_image)
            post.save()
            return post
        except ValueError:
            return None
        #
        # post = Post()
        # post.post_name = post_name
        # post.post_body = post_body
        # post.post_data = post_data
        # post.post_image = post_image
        #
        # post.save()


    def update(self, post_name, post_body, post_image):

        if post_name is not None:
            self.name = post_name

        if post_body is not None:
            self.post_body = post_body

        if post_image is not None:
            self.post_image = post_image

        self.save()


    @staticmethod
    def get_all():
        return list(Post.objects.all())


