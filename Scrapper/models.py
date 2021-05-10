from datetime import datetime

from django.db import models


# Create your models here.
class World(models.Model):
    worlds_names_choices = [
        (0, 'Adra'), (1, 'Antica'), (2, 'Assombra'), (3, 'Astera'), (4, 'Belluma'), (5, 'Belobra'), (6, 'Bona'),
        (7, 'Calmera'), (8, 'Carnera'), (9, 'Celebra'), (10, 'Celesta'), (11, 'Concorda'), (12, 'Cosera'),
        (13, 'Damora'), (14, 'Descubra'), (15, 'Dibra'), (16, 'Duna'), (17, 'Emera'), (18, 'Epoca'), (19, 'Estela'),
        (20, 'Faluna'), (21, 'Ferobra'), (22, 'Firmera'), (23, 'Funera'), (24, 'Furia'), (25, 'Garnera'),
        (26, 'Gentebra'), (27, 'Gladera'), (28, 'Harmonia'), (29, 'Helera'), (30, 'Honbra'), (31, 'Impera'),
        (32, 'Inabra'), (33, 'Javibra'), (34, 'Jonera'), (35, 'Kalibra'), (36, 'Karna'), (37, 'Kenora'),
        (38, 'Libertabra'), (39, 'Lobera'), (40, 'Luminera'), (41, 'Lutabra'), (42, 'Macabra'), (43, 'Menera'),
        (44, 'Mitigera'), (45, 'Monza'), (46, 'Mudabra'), (47, 'Nefera'), (48, 'Noctera'), (49, 'Nossobra'),
        (50, 'Olera'), (51, 'Ombra'), (52, 'Optera'), (53, 'Pacembra'), (54, 'Pacera'), (55, 'Peloria'), (56, 'Premia'),
        (57, 'Pyra'), (58, 'Quelibra'), (59, 'Quintera'), (60, 'Ragna'), (61, 'Refugia'), (62, 'Reinobra'),
        (63, 'Relania'), (64, 'Relembra'), (65, 'Secura'), (66, 'Serdebra'), (67, 'Serenebra'), (68, 'Solidera'),
        (69, 'Talera'), (70, 'Torpera'), (71, 'Tortura'), (72, 'Unica'), (73, 'Utobra'), (74, 'Venebra'), (75, 'Vita'),
        (76, 'Vunira'), (77, 'Wintera'), (78, 'Wizera'), (79, 'Xandebra'), (80, 'Xylona'), (81, 'Yonabra'),
        (82, 'Ysolera'), (83, 'Zenobra'), (84, 'Zuna'), (85, 'Zunera')
    ]

    name = models.PositiveSmallIntegerField(choices=worlds_names_choices)
    players_online = models.PositiveSmallIntegerField(default=0)

    location_choices = [("SA", "South America"), ("EU", "Europe"), ("NA", "North America")]
    location = models.CharField(choices=location_choices, default="EU", max_length=15)
    pvp_settings_choices = [(0, "Open PvP"), (1, "Optional PvP"), (2, "Retro PvP"), (3, "Other")]
    pvp_settings = models.PositiveSmallIntegerField(choices=pvp_settings_choices, default=0)
    transfer_type = models.BooleanField(default=True)
    creation_date = models.DateTimeField(blank=True)
    battle_eye_status = models.BooleanField(default=False)


class AbstractCharacter(models.Model):
    other_characters = models.ManyToManyField("Character")

    class Meta:
        abstract = True


class Character(AbstractCharacter):
    # game data
    name = models.CharField(max_length=25)
    vocation_elite_knight = "EK"
    vocation_knight = "K"
    vocation_elder_druid = "ED"
    vocation_druid = "D"
    vocation_royal_paladin = "RP"
    vocation_paladin = "P"
    vocation_master_sorcerer = "MS"
    vocation_sorcerer = "S"
    vocation_none = "N"

    vocations_choices = [
        (vocation_elite_knight, "Elite Knight"),
        (vocation_knight, "Knight"),
        (vocation_elder_druid, "Elder Druid"),
        (vocation_druid, "Druid"),
        (vocation_royal_paladin, "Royal Paladin"),
        (vocation_paladin, "Paladin"),
        (vocation_master_sorcerer, "Master Sorcerer"),
        (vocation_sorcerer, "Sorcerer"),
        (vocation_none, "None")
    ]

    vocation = models.CharField(max_length=2, choices=vocations_choices, default=vocation_none)
    level = models.IntegerField(default=0)
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default='o')
    guild = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=30, blank=True)
    achievement_points = models.IntegerField(default=0)
    world = models.CharField(max_length=10, choices=World.worlds_names_choices)
    last_login = models.TimeField(default=datetime.min)
    online = models.BooleanField(default=False)
