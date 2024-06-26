from rest_framework import serializers
from . import models


class BlogSerializer(serializers.ModelSerializer):
    author=serializers.EmailField()
    class Meta:
        model = models.Blog
        fields = '__all__'

    def to_representation(self, obj):
        serialized_data = super(BlogSerializer, self).to_representation(obj)
        blog_id = serialized_data.get('id')
        blog=models.Blog.objects.get(id=blog_id)
        # comments = models.comment.objects.filter(commented_post=blog_id)
        comments=blog.comments.all()

        nested_comment = []
        for comment in comments:
            cleaned_body = comment.body.replace('\r\n', ' ').replace('\n', ' ').strip()
            single_comment = {"commentor": comment.author.email, "body": cleaned_body}

            nested_comment.append(single_comment)

        serialized_data['comments'] = nested_comment

        return serialized_data
