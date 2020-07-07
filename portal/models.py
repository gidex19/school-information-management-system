from django.db import models
from django.contrib.auth.models import AbstractUser

classes_list = (('JSS 1 BLUE', 'JSS 1 BLUE'), ('JSS 1 GREEN', 'JSS 1 GREEN'), ('JSS 1 YELLOW', 'JSS 1 YELLOW'),
             ('JSS 2 BLUE', 'JSS 2 BLUE'), ('JSS 2 GREEN', 'JSS 2 GREEN'), ('JSS 2 YELLOW', 'JSS 1 YELLOW'),
             ('JSS 3 BLUE', 'JSS 3 BLUE'), ('JSS 3 GREEN', 'JSS 3 GREEN'), ('JSS 3 YELLOW', 'JSS 3 YELLOW'),
             ('SSS 1 HARMONY', 'SSS 1 HARMONY'), ('SSS 1 SMART', 'SSS 1 SMART'), ('SSS 1 SPECIAL', 'SSS 1 SPECIAL'),
             ('SSS 2 HARMONY', 'SSS 2 HARMONY'), ('SSS 2 SMART', 'SSS 2 SMART'), ('SSS 2 SPECIAL', 'SSS 2 SPECIAL'),
             ('SSS 3 HARMONY', 'SSS 3 HARMONY'), ('SSS 3 SMART', 'SSS 3 SMART'), ('SSS 3 SPECIAL', 'SSS 3 SPECIAL'),
             ('Graduated','Graduated'))
class Customuser(AbstractUser):
    middle_name = models.CharField(max_length=20, default=' ', blank=True)
    submitted = models.BooleanField(default=False)
    gender_list = (('Male', 'Male'), ('Female', 'Female'))
    relationship_list = (('father', 'Father'), ('mother', 'Mother'), ('brother', 'Brother'), ('sister', 'Sister'), ('uncle', 'Uncle'))
    states_list = (("Abia", "Abia"), ("Adamawa", "Adamawa"), ("Anambra","Anambra"), ("Akwa Ibom", "Akwa Ibom"), ("Bauchi", "Bauchi"),
    ("Bayelsa","Bayelsa"), ("Benue","Benue"), ("Borno","Borno"), ("Cross River","Cross River"), ("Delta", "Delta"), ("Ebonyi", "Ebonyi"),
    ("Enugu", "Enugu"), ("Edo","Edo"), ("Ekiti", "Ekiti"), ("FCT - Abuja", "FCT - Abuja"), ("Gombe", "Gombe"), ("Imo", "Imo") ,
    ("Jigawa", "Jigawa"), ("Kaduna", "Kaduna"), ("Kano", "Kano"), ("Katsina", "Katsina"), ("Kebbi" , "Kebbi"), ("Kogi", "Kogi"),
    ("Kwara", "Kwara") , ("Lagos", "Lagos"), ("Nasarawa", "Nasarawa"), ("Niger", "Niger"), ("Ogun", "Ogun"), ("Ondo", "Ondo"),
    ("Osun", "Osun"), ("Oyo", "Oyo"), ("Plateau", "Plateau"), ("Rivers", "Rivers"), ("Sokoto", "Sokoto"), ("Taraba", "Taraba"),
    ("Yobe", "Yobe"), ("Zamfara", "Zamfara"))
    res_type_list = (('Day Student','Day Student'), ('Boarding Student','Boarding Student'))
    religion_list = (('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Others', 'Others'))

    current_class = models.CharField(max_length=30, choices = classes_list, blank = True)
    gender = models.CharField(max_length=30, choices=gender_list, blank = True)
    date_of_birth = models.DateField( blank = True, null=True)
    religion = models.CharField(max_length=30, choices=religion_list, blank=True)
    nok1_name = models.CharField(max_length=32, blank = True)
    nok1_phone = models.CharField(max_length=11, blank = True)
    nok1_relationship = models.CharField(max_length=12, choices=relationship_list, blank = True)
    nok2_name = models.CharField(max_length=32, blank = True)
    admission_no = models.CharField(max_length=32, blank = True)
    state_of_origin = models.CharField(max_length=20, choices=states_list, blank = True)
    lga = models.CharField(max_length=22, blank = True)
    resident_type = models.CharField(max_length=20, choices= res_type_list, blank = True)
    house_address = models.TextField(max_length=90, blank=True)
    phonenumber = models.CharField(max_length=20, blank=True)
    prev_school = models.TextField(max_length=140, blank=True)
    passport = models.ImageField(upload_to='passports', blank=True, default="passports/default.jpg")

    def fullname(self):
        return('{} {} {}'.format(self.last_name, self.first_name, self.middle_name))

    def class_count(self):
        class_counts = Customuser.objects.filter(current_class=self.current_class).count()
        return class_counts

    def __str__(self):
        return ('username: {}'.format(self.username))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(' ========================= save method has just been called ============ ')
        """ print(self.username)
        print(self.email)
        print(self.password)
        user = Customuser.objects.filter(username = self.username).first()
        user.set_password(self.password)
        print(self.password)
        print(user.password)
        #user.save() """



term_list = (('First Term','First Term'), ('Second Term', 'Second Term'), ('Third Term', 'Third Term'))
year_list = (('2019/2020','2019/2020'), ('2020/2021','2020/2021'), ('2021/2022','2021/2022'),('2022/2023','2022/2023'),
                 ('2023/2024','2023/2024'),('2024/2025','2024/2025'),('2025/2026','2025/2026'),('2026/2027','2026/2027'),
                 ('2027/2028','2027/2028'),('2028/2029','2028/2029'), ('2029/2030','2029/2030'),('2030/2031','2030/2031'),
                 ('2031/2032','2031/2032'),('2032/2033','2032/2033'),('2033/2034','2033/2034'),('2034/2035','2034/2035'))
class Subjectz(models.Model):


    title = models.CharField(max_length=80, blank=True)
    ca1_score = models.PositiveIntegerField(default=0)
    ca2_score = models.PositiveIntegerField(default=0)
    exam_score = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    grade = models.CharField(max_length=80, blank=True)
    remark = models.CharField(max_length=80, blank=True)
    student = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    term = models.CharField(max_length=80, choices= term_list, blank=True)
    session = models.CharField(max_length=30, choices=year_list, blank=True)
    current_class = models.CharField(max_length=30, choices=classes_list, blank=True)

    def __str__(self):
        return ('first term {} grade for {}'.format(self.title, self.student))

    class Meta:
        ordering = ('-title',)

class Subject_2(models.Model):
    title = models.CharField(max_length=80, blank=True)
    ca1_score = models.PositiveIntegerField(default=0)
    ca2_score = models.PositiveIntegerField(default=0)
    exam_score = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    grade = models.CharField(max_length=80, blank=True)
    remark = models.CharField(max_length=80, blank=True)
    student = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    term = models.CharField(max_length=80, choices= term_list, blank=True)
    session = models.CharField(max_length=30, choices=year_list, blank=True)
    current_class = models.CharField(max_length=30, choices=classes_list, blank=True)

    def __str__(self):
        return ('second term {} grade for {}'.format(self.title, self.student))

    class Meta:
        ordering = ('-title',)

class Subject_3(models.Model):
    title = models.CharField(max_length=80, blank=True)
    ca1_score = models.PositiveIntegerField(default=0)
    ca2_score = models.PositiveIntegerField(default=0)
    exam_score = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    grade = models.CharField(max_length=80, blank=True)
    remark = models.CharField(max_length=80, blank=True)
    student = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    term = models.CharField(max_length=80, choices= term_list, blank=True)
    session = models.CharField(max_length=30, choices=year_list, blank=True)
    current_class = models.CharField(max_length=30, choices=classes_list, blank=True)

    def __str__(self):
        return ('third term {} grade for {}'.format(self.title, self.student))

    class Meta:
        ordering = ('-title',)


class Payment(models.Model):
    student = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    term = models.CharField(max_length=80, choices=term_list)
    session = models.CharField(max_length=30, choices=year_list)
    amount = models.PositiveIntegerField(default=0)
    reference = models.CharField(max_length=100, default='Unpaid')
    paid = models.BooleanField(default= False)


class Course(models.Model):
    title = models.CharField(max_length=80, unique=True)
    teacher = models.CharField(max_length=80)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=80)

    def __str__(self):
        return ('{}'.format(self.title))

