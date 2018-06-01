from django.db import models
from datetime import datetime


class MLModel(models.Model):
    name = models.CharField(max_length=120)
    knowledge_graph = models.URLField()
    created_on = models.DateTimeField(default=datetime.now())
    progress = models.PositiveIntegerField(default=0)
    notes = models.TextField()
    status = models.CharField(max_length=60, default='Not Started')

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "%s> %s" % (str(self.id), self.name)


class Cluster(models.Model):
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    center = models.TextField()  # space separated n-dimensions

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "%s> %s" % (str(self.id), self.name)


class ModelClass(models.Model):
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    class_uri = models.URLField()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "%s> %s" % (str(self.id), self.class_uri)


class PredictionRun(models.Model):
    name = models.CharField(max_length=120)
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now())
    finished_on = models.DateTimeField(default=datetime.now())
    input_file = models.FileField()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "%s> %s" % (str(self.id), self.name)


class ColumnPrediction(models.Model):
    prediction_run = models.ForeignKey(PredictionRun, on_delete=models.CASCADE)
    column_no = models.PositiveIntegerField()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "%s> %s" % (str(self.id), str(self.column_no))


class CCMembership(models.Model):
    column_prediction = models.ForeignKey(ColumnPrediction, on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    membership = models.FloatField()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "%s> %s" % (str(self.id), str(self.membership))
