from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import secrets
# Create your models here.

class Poll(models.Model):
    owner = models.ForeignKey('Users.User', on_delete=models.CASCADE, default=1)
    poll_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.poll_text
    @property
    def get_vote_count(self):
        return self.vote_set.count()
    
    
    def get_result_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            # alert_class = ['primary', 'secondary', 'success',
            #                'danger', 'dark', 'warning', 'info']

            
            #d['alert_class'] = secrets.choice(alert_class)
            d['text'] = choice.choice_text
            d['num_votes'] = choice.get_vote_count
            if not self.get_vote_count:
                d['percentage'] = 0
            else:
                d['percentage'] = (choice.get_vote_count /
                                   self.get_vote_count)*100

            res.append(d)
        return res    

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    @property
    def get_vote_count(self):
        return self.vote_set.count()
    
    
class Vote(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.poll.poll_text[:15]} - {self.choice.choice_text[:15]} - {self.user.name}'
    