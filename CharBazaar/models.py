from collectionfield.models import CollectionField
from django.db import models

from Scrapper.models import Character


class AuctionDetails(models.Model):
    character = Character()
    auction_start = models.DateTimeField()
    auction_end = models.DateTimeField()
    winning_bid = models.IntegerField(default=0)
    highlighted_information = models.CharField(max_length=300)


class Skill(models.Model):
    level = models.IntegerField(default=10)
    percentage_to_next_level = models.FloatField(default=0.0)


class General(models.Model):
    hit_points = models.IntegerField()
    mana = models.IntegerField()
    capacity = models.IntegerField(default=100)
    speed = models.IntegerField(default=100)
    blessings = models.IntegerField(default=0)
    mounts = models.IntegerField(default=0)
    outfits = models.IntegerField(default=4)

    skill_axe_fighting = Skill()
    skill_sword_fighting = Skill()
    skill_club_fighting = Skill()
    skill_distance_fighting = Skill()
    skill_fist_fighting = Skill()
    skill_fishing = Skill()
    skill_shielding = Skill()
    skill_magic_level = Skill()

    creation_date = models.DateTimeField()
    experience = models.IntegerField()
    gold = models.IntegerField()
    achievement_points = models.IntegerField()

    regular_world_transfer = models.BooleanField(default=False)
    available_charm_points = models.IntegerField()
    spent_charm_points = models.IntegerField()
    charm_expansion = models.BooleanField()
    daily_reward_streak = models.IntegerField()
    hunting_task_points = models.IntegerField()
    permanent_hunting_tasks_slots = models.BooleanField()
    permanent_prey_slots = models.BooleanField()
    prey_wildcards = models.IntegerField(default=0)

    hirelings = models.IntegerField()
    # hirelings_jobs = models.CharField(max_length=200)
    # hirelings_outfits = models.CharField(max_length=50) # this is a waste of memory in database :P


class Item(models.Model):
    name = models.CharField(max_length=30)
    gif = models.IntegerField()
    amount = models.IntegerField()


class ItemSummary(models.Model):
    pass


class MountsStore(models.Model):
    pass


class Mounts(models.Model):
    pass


class StoreItemSummary(models.Model):
    pass


class OutfitsStore(models.Model):
    pass


class Outfits(models.Model):
    pass


class Familiars(models.Model):
    first = models.CharField(max_length=20, blank=True)
    second = models.CharField(max_length=20, blank=True)


class Blessings(models.Model):
    Adventurers_Blessing = models.SmallIntegerField(default=0)
    blood_of_the_Mountain = models.SmallIntegerField(default=0)
    Embrace_of_tibia = models.SmallIntegerField(default=0)
    Fire_Of_the_suns = models.SmallIntegerField(default=0)
    heart_of_the_mountain = models.SmallIntegerField(default=0)
    spark_of_the_phoenix = models.SmallIntegerField(default=0)
    spiritual_shielding = models.SmallIntegerField(default=0)
    twist_of_fate = models.SmallIntegerField(default=0)
    wisdom_of_solitude = models.SmallIntegerField(default=0)


class Imbuements(models.Model):
    imbuements = CollectionField()


class Charms(models.Model):
    charms = CollectionField()


class CompletedCyclopediaMapAreas(models.Model):
    areas = CollectionField()


class CompletedQuestLines(models.Model):
    quests = CollectionField()


class Titles(models.Model):
    pass


class Achievements(models.Model):
    pass


class BestiaryEntry(models.Model):
    name = models.CharField(max_length=30)
    kills = models.SmallIntegerField(default=0)
    step = models.SmallIntegerField(default=0)


class BestiaryProgress(models.Model):
    u"""Collection of BestiaryEntry instances."""
    entries = CollectionField()


# Create your models here.
class Action(models.Model):
    auction_details = None
    general = None
    item_summary = None
    store_item_summary = None
    mounts_store = None
    mounts = None
    outfits_store = None
    outfits = None
    familiars = None
    blessings = None
    imbuements = None
    charms = None
    completed_cyclopedia_map_areas = None
    completed_quest_lines = None
    titles = None
    achievements = None
    bestiary_progress = None
