__author__ = 'Tarun Behal'

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import hashlib
from django.db.models import Sum


def upload_path(instance, filename):
    flist = filename.split('.')
    extension = flist.pop()
    fname = '-'.join(flist)
    name = "{0}-{1}.{2}".format(
        slugify(fname),
        hashlib.md5(fname).hexdigest()[:5], extension)
    return 'files/{0}/{1}'.format(instance.id, name)


class Campaign(models.Model):
    name = models.CharField(max_length=150)

    photo = models.FileField(blank=True, default=False, upload_to=upload_path)
    user = models.ForeignKey(User)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(default='campaign')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    start_at = models.DateField(blank=True, null=True)
    end_at = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name[:50])
        super(Campaign, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name


class CampaignZone(models.Model):
    name = models.CharField(max_length=150)
    campaign = models.ForeignKey(Campaign, related_name="zones")
    total_points = models.PositiveIntegerField(default=1)
    total_plants = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.campaign.name, self.name)

    def available_plants(self):
        ap = Plantation.objects.filter(zone=self, status='approve').count()
        return self.total_plants - ap


class Plantation(models.Model):
    user = models.ForeignKey(User)
    zone = models.ForeignKey(CampaignZone)
    photo = models.ImageField(upload_to=upload_path)
    points = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    zones = models.ManyToManyField(
        CampaignZone, related_name='zones', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


User.profile = property(
    lambda u: UserProfile.objects.get_or_create(user=u)[0])
