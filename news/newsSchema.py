import graphene
from graphene_django import DjangoObjectType
from news.models import *

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        
class Query(graphene.ObjectType):
    allCategory = graphene.List(CategoryType)
    allPost = graphene.List(PostType, category_id=graphene.Int())

    def resolve_allCategory(self, info, **kwargs):
        return Category.objects.all()

    def resolve_allPost(self, info, category_id=None, **kwargs):
        if category_id:
            return Post.objects.filter(category_id=category_id)
        return Post.objects.all()

# post mutation
class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)
    class Arguments:
        title=graphene.String()
        content = graphene.String()
        author = graphene.String()
        category = graphene.Int()    
        
    def mutate(self,info, title,content,author,category,**kwargs):
        post = Post(title=title,content=content,author=author,category=category.id)
        post.save()
        return CreatePost(post=post)
# category mutation
class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)
    class Arguments:
        name = graphene.String()
    
    def mutate(self,info,name,**kwargs):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)



class Mutation(graphene.ObjectType):
    createPost = CreatePost.Field()
    createCategory = CreateCategory.Field()


schema = graphene.Schema(query=Query ,mutation=Mutation)

