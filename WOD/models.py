from django.db import models
from account.models import Profile, User
from account.models import User
# Create your models here.

MOVEMENT_TYPE_WARMUP = [( 'Mobilidade e Ativação Articular',[("Arm circles", "ARM CIRCLES"),
    ("Leg swings", "LEG SWINGS"),
    ("World’s greatest stretch", "WORLD’S GREATEST STRETCH"),
    ("Inchworm to push-up", "INCHWORM TO PUSH-UP"),
    ("Spiderman stretch", "SPIDERMAN STRETCH"),
    ("Ankle mobility", "ANKLE MOBILITY"),
    ("Hip openers", "HIP OPENERS"),
    ("Scorpion stretch", "SCORPION STRETCH"),
    ("Cat-cow", "CAT-COW"),
    ("PVC pass-throughs", "PVC PASS-THROUGHS")
    ]), 

    ('Core e Ativação de Estabilizadores',[("V-up alternado", "V-UP ALTERNADO"),
    ("Hollow hold", "HOLLOW HOLD"),
    ("Hollow rocks", "HOLLOW ROCKS"),
    ("Arch hold", "ARCH HOLD"),
    ("Dead bug", "DEAD BUG"),
    ("Bird-dog", "BIRD-DOG"),
    ("Glute bridge", "GLUTE BRIDGE"),
    ("Side plank", "SIDE PLANK"),
    ("Plank shoulder taps", "PLANK SHOULDER TAPS")
    ]), 

    ('Ginástica Leve (Corpo Livre)',[("Scapular pull-up", "SCAPULAR PULL-UP"),
("Scapular push-up", "SCAPULAR PUSH-UP"),
("Kipping swing", "KIPPING SWING"),
("Jumping pull-up", "JUMPING PULL-UP"),
("Ring rows", "RING ROWS"),
("Wall walk até a metade", "WALL WALK ATÉ A METADE"),
("Air squat", "AIR SQUAT"),
("Push-up", "PUSH-UP"),
("Knee push-up", "KNEE PUSH-UP"),
("PVC overhead squat", "PVC OVERHEAD SQUAT")
]),

('Cardio Leve / Elevação da Frequência Cardíaca',
 
[("Jumping jacks", "JUMPING JACKS"),
("High knees", "HIGH KNEES"),
("Butt kicks", "BUTT KICKS"),
("Single unders", "SINGLE UNDERS"),
("Row 250m leve", "ROW 250M LEVE"),
("Assault bike 1-2 min", "ASSAULT BIKE 1-2 MIN"),
("Jogging no lugar", "JOGGING NO LUGAR")
]),

('Movimentos Técnicos com Carga Leve',
 
[("Empty barbell good mornings", "EMPTY BARBELL GOOD MORNINGS"),
("Barbell deadlifts com barra vazia", "BARBELL DEADLIFTS COM BARRA VAZIA"),
("Barbell front squats", "BARBELL FRONT SQUATS"),
("Barbell overhead squats", "BARBELL OVERHEAD SQUATS"),
("Barbell presses", "BARBELL PRESSES"),
("Snatch balance com PVC", "SNATCH BALANCE COM PVC"),
("Burgener warm-up", "BURGENER WARM-UP")
])

]




MOVEMENT_TYPE_CHOICES = [
    ('BARBELL', [
        ("back squat", "BACK SQUAT"),
        ("bench press", "BENCH PRESS"),
        ("clean", "CLEAN"),
        ("clean & jerk", "CLEAN & JERK"),
        ("clean pull", "CLEAN PULL"),
        ("cluster", "CLUSTER"),
        ("deadlift", "DEADLIFT"),
        ("deadlift fat bar", "DEADLIFT FAT BAR"),
        ("front squat", "FRONT SQUAT"),
        ("hang clean", "HANG CLEAN"),
        ("hang power clean", "HANG POWER CLEAN"),
        ("hang power snatch", "HANG POWER SNATCH"),
        ("hang snatch", "HANG SNATCH"),
        ("muscle clean", "MUSCLE CLEAN"),
        ("muscle snatch", "MUSCLE SNATCH"),
        ("overhead lunge", "OVERHEAD LUNGE"),
        ("overhead squat", "OVERHEAD SQUAT"),
        ("power clean", "POWER CLEAN"),
        ("push jerk", "PUSH JERK"),
        ("push press", "PUSH PRESS"),
        ("shoulder press", "SHOULDER PRESS"),
        ("snatch", "SNATCH"),
        ("snatch deadlift", "SNATCH DEADLIFT"),
        ("snatch pull", "SNATCH PULL"),
        ("split jerk", "SPLIT JERK"),
        ("squat clean", "SQUAT CLEAN"),
        ("squat jerk", "SQUAT JERK"),
        ("squat snatch", "SQUAT SNATCH"),
        ("squat deadlift", "SQUAT DEADLIFT"),
        ("sumo deadlift", "SUMO DEADLIFT"),
        ("sumo deadlift high pull", "SUMO DEADLIFT HIGH PULL"),
        ("thruster", "THRUSTER"),
    ]),

    ('ENDURANCE', [
    ("air bike", "AIR BIKE"),
    ("max burpee", "MAX BURPEE"),
    ("max sit up", "MAX SIT UP"),
    ("max squat", "MAX SQUAT"),
    ("row", "ROW"),
    ("run", "RUN")
    ]),
    
    ('GYMNASTIC',[("abmat sit-up", "ABMAT SIT-UP"),
("box jump", "BOX JUMP"),
("double-under", "DOUBLE-UNDER"),
("handstand push-up", "HANDSTAND PUSH-UP"),
("handstand walk", "HANDSTAND WALK"),
("l-sit", "L-SIT"),
("muscle-up", "MUSCLE-UP"),
("pull-up(strict)", "PULL-UP(STRICT)"),
("pull-up(weighted)", "PULL-UP(WEIGHTED)"),
("pushup", "PUSHUP"),
("ring dip", "RING DIP"),
("rope climb", "ROPE CLIMB"),
("toes to bar", "TOES TO BAR"),
("wall ball", "WALL BALL")])
]


TIME_FORMAT_CHOICES = [("amrap","AMRAP"), 
                     ("emom","EMOM"), 
                     ("tabata","TABATA"),
                     ("rft ","RFT "), ("rnft","RNFT "), ("rx","RX "), ("rm","RM "),  ("rm","RM "), ("rm","RM "), 
                     ]


ALL_MOVEMENT_TYPE = MOVEMENT_TYPE_WARMUP + MOVEMENT_TYPE_CHOICES

class Movement(models.Model):
    name =  models.CharField(max_length=50)
    type =  models.CharField(max_length=50, choices=   ALL_MOVEMENT_TYPE)
    description  = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.name}'

class WOD (models.Model):
    title = models.CharField(max_length=200)
    description_wod  = models.TextField(max_length=10000)
    pinned  = models.BooleanField(default=False)
    coach = models.ForeignKey(Profile, null=False, blank= False, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add= True)
    like = models.ManyToManyField(User,  related_name= 'liked_wod')
    elite  = models.IntegerField(default=0)
    rx = models.IntegerField(default=0)
    amauter  = models.IntegerField(default=0)
    scaled  = models.IntegerField(default=0)
    fit  = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'
