from django.db import models
import uuid
from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ""
        return img 
    
    class Meta:
        # negtive means ascending order and we are ranking them according to  the highest vote ranking, than
        # highest vote and then the title
        ordering = ['-vote_ratio', '-vote_total', 'title']
    
    @property
    def reviewers(self):
        # returns the owners id, and the feature 'flat=True' convert this obj into list  
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    # this function is used to update the vote_total and vote_ratio
    @property
    def getVoteCount(self):
        # if there is the relation establish between the two classes we can use the other class obj like here 
        # review_set is not define but due to relation we can use it 
        reviews = self.review_set.all()
        # filtering votes on basis of up factor and returning its count i.e int
        upVotes = reviews.filter(value="up").count()
        totalVotes = reviews.count()
        # calculating the percentage of the upvotes
        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()



class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up Vote'),
        ('down', 'down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
    
    # project owner can't post more than one reviews on his projects that's why binding the owner and project 
    # comnbination of the owner and the project is unique, if already exist can't post another one 
    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name