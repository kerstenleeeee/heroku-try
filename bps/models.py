# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added models

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: models / entities for the database

from django.db import models
import uuid

# building entity
class Building(models.Model):
  buildID = models.CharField(primary_key = True, max_length = 100)
  buildName = models.CharField(max_length = 100)
  buildExist = models.BooleanField(default=False)
  buildFloors = models.IntegerField(default=1)
  #buildLogo = models.URLField()

  def __str__(self):
    return "%s" % (self.buildName)

# floor entity
class Floor(models.Model):
	buildID = models.ForeignKey(Building, on_delete = models.CASCADE)
	floorID = models.CharField(primary_key = True, max_length = 100, unique=True, default=uuid.uuid4)
	floorNo = models.IntegerField()	
	floorImageLink = models.URLField(blank=True, null=True)
	# floorImageLink = models.URLField()

	class Meta:
		unique_together = (('buildID', 'floorID'),)

	def __str__(self):
		return '%s (%d)' % (self.buildID, self.floorNo)

# to from entity
class Routes(models.Model):
	buildID = models.ForeignKey(Building, on_delete = models.CASCADE)
	destination = models.CharField(max_length = 100)
	roomNo = models.IntegerField(primary_key=True, default=1)
	directions = models.TextField("Directions", null=False, blank=False)

	class Meta:
		unique_together = (('buildID', 'roomNo'),)

	def __str__(self):
		return '%s (%d)' % (self.destination, self.roomNo)