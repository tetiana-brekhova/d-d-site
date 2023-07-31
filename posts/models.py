from django.db import models


class Post(models.Model):

    post_name = models.CharField(blank=True, max_length=128)
    post_body = models.CharField(blank=True)
    post_id = models.AutoField(primary_key=True)
    post_data = models.DateField(auto_now_add=True)
    post_image = models.ImageField()


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"'post_id': {self.post_id}, " \
               f"'post_name': '{self.post_name}', " \
               f"'post_body': '{self.post_body}', " \
               f"'post_data': {self.post_data}, " \
               f"'post_image': {self.post_image}, "
            # f"'authors': {[author.id for author in self.authors.all()]}" \

    def __repr__(self):
        return f"Post(id={self.id})"

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
    def create(post_name, post_body, post_data, post_image):

        if len(post_name) > 128:
            return None
        post = Post()
        post.post_name = post_name
        post.post_body = post_body
        post.post_data = post_data
        post.post_image = post_image

        post.save()
        # if (author is not None):
        #     for elem in author:
        #         post.author.add(elem)
        #     post.save()
        # return post


    def update(self, post_name, post_body, post_image):

        if post_name is not None:
            self.name = post_name

        if post_body is not None:
            self.description = post_body

        if post_image is not None:
            self.count = post_image

        self.save()


    @staticmethod
    def get_all():
        return list(Post.objects.all())


