from django.db import models

class Stat(models.Model):
  testNum = models.CharField(max_length=200)
  numOfAttemptedLogins = models.IntegerField(blank=True, default=0)
  numOfAcceptedLogins = models.IntegerField(blank=True, default=0)
  numOfDeniedLogins = models.IntegerField(blank=True, default=0)
  numOfAcceptedLoginsCorrect = models.IntegerField(blank=True, default=0)
  numOfAcceptedLoginsIncorrect = models.IntegerField(blank=True, default=0)
  numOfDeniedLoginsCorrect = models.IntegerField(blank=True, default=0)
  numOfDeniedLoginsIncorrect = models.IntegerField(blank=True, default=0)
  percentsWhenAccepted = models.JSONField(blank=True, default="[]")
  percentsWhenDenied = models.JSONField(blank=True, default="[]")
  percentsWhenAcceptedCorrect = models.JSONField(blank=True, default="[]")
  percentsWhenAcceptedIncorrect = models.JSONField(blank=True, default="[]")
  percentsWhenDeniedCorrect = models.JSONField(blank=True, default="[]")
  percentsWhenDeniedIncorrect = models.JSONField(blank=True, default="[]")
  dwelldataForKeyE = models.JSONField(blank=True, default="[]")
  dwelldataForKeyA = models.JSONField(blank=True, default="[]")
  dwelldataForKeyR = models.JSONField(blank=True, default="[]")
  dwelldataForKeyI = models.JSONField(blank=True, default="[]")
  dwelldataForKeyO = models.JSONField(blank=True, default="[]")
  flightdataForKeysTH = models.JSONField(blank=True, default="[]")
  flightdataForKeysHE = models.JSONField(blank=True, default="[]")
  flightdataForKeysAN = models.JSONField(blank=True, default="[]")
  flightdataForKeysIN = models.JSONField(blank=True, default="[]")
  flightdataForKeysER = models.JSONField(blank=True, default="[]")
  def __str__(self):
    return self.testNum
  