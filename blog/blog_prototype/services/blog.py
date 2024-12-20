from typing import Dict, List

from django.core.exceptions import ObjectDoesNotExist

from blog_prototype.inputs.blog import (
    CommentCreateInput,
    CommentUpdateInpute,
    PostCreateInput,
    PostUpdateInpute,
)
from blog_prototype.models.blog import Comment, Post


class PostService:

    def create_post(self, data: PostCreateInput) -> Dict:

        post = Post.objects.create(**data.dict())

        return {
            "id": post.id,
            "user_id": post.user.id,
            "title": post.title,
            "description": post.description,
            "create_at": post.create_at.isoformat(),
            "update_at": post.update_at.isoformat(),
        }

    def update_post(self, post_id: int, data: PostUpdateInpute) -> Dict:

        try:
            post = Post.objects.get(id=post_id)

            for field, value in data.dict(exclude_unset=True).items():
                setattr(product, field, value)

            product.save()

            return {
                "id": post.id,
                "user_id": post.user.id,
                "title": post.title,
                "description": post.description,
                "create_at": post.create_at.isoformat(),
                "update_at": post.update_at.isoformat(),
            }

        except ObjectDoesNotExist:
            raise ValueError("Post not found")

    def delete_post(self, post_id: int) -> None:

        try:
            post = Post.objects.get(id=post_id)
            post.delete()

        except ObjectDoesNotExist:
            raise ValueError("Post not found")

    def get_post(self, post_id: int) -> Dict:

        try:
            post = Post.objects.get(id=post_id)

            comment_service = CommentService()
            comments = comment_service.list_comment(post_id)

            return {
                "id": post.id,
                "username": post.user.username,
                "title": post.title,
                "description": post.description,
                "comments": comments,
                "create_at": post.create_at.isoformat(),
                "update_at": post.update_at.isoformat(),
            }

        except ObjectDoesNotExist:
            raise ValueError("Product not found")

    def list_post(self) -> List[Dict]:
        posts = Post.objects.all()

        return [
            {
                "id": post.id,
                "username": post.user.username,
                "title": post.title,
                "description": post.description,
                "create_at_date": post.create_at.date(),
                "create_at_time": post.create_at.time(),
                "update_at": post.update_at.isoformat(),
            }
            for post in posts
        ]


class CommentService:

    def create_comment(self, data: CommentCreateInput) -> Dict:

        try:
            post = Post.objects.get(id=data.post_id)
            comment = Comment.objects.create(post=post, **data.dict(exclude={"post_id"}))

            return {
                "id": comment.id,
                "user_id": comment.user.id,
                "post_id": comment.post.id,
                "description": comment.description,
                "create_at": post.create_at.isoformat(),
                "update_at": post.update_at.isoformat(),
            }

        except ObjectDoesNotExist:
            raise ValueError("Post not found")

    def update_comment(self, comment_id: int, data: CommentUpdateInpute) -> Dict:

        try:
            comment = Comment.objects.get(id=comment_id)

            for field, value in data.dict(exclude_unset=True).items():
                setattr(variant, field, value)

            comment.save()

        except ObjectDoesNotExist:
            raise ValueError("Post not found")

    def delete_comment(self, comment_id: int) -> None:

        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()

        except ObjectDoesNotExist:
            raise ValueError("Comment not found")

    def get_comment(self, comment_id: int) -> Dict:

        try:
            comment = Comment.objects.get(id=comment_id)

            return {
                'id': comment_id,
                'username': comment.user.username,
                'post_id': comment.post.id,
                'description': comment.description,
                "create_at": post.create_at.isoformat(),
                "update_at": post.update_at.isoformat(),
            }

        except ObjectDoesNotExist:
            raise ValueError("Comment not found")


    def list_comment(self, post_id: int):

        try:
            post = Post.objects.get(id=post_id)
            comments = Comment.objects.filter(post=post)

            return [
                {
                    'id': comment.id,
                    'username': comment.user.username,
                    'post_id': comment.post.id,
                    'description': comment.description,
                    "create_at": post.create_at.isoformat(),
                    "update_at": post.update_at.isoformat(),
                }
                for comment in comments
            ]

        except ObjectDoesNotExist:
            raise ValueError("Comment not found")

