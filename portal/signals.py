from django.db.models.signals import post_save
from .models import Customuser
from django.dispatch import receiver
from .models import Subjectz, Subject_2, Subject_3, Course


session = '2019/2020'
sciences = ['English Language', 'General Mathematics', 'Further Mathematics', 'Physics', 'Biology', 'Chemistry',
            'Animal Husbandry', 'Agricultural Science', 'Health Education', 'Physical Education', 'Fisheries',
            'Civic Education', 'CRK', 'IRK', 'Economics']
arts = ['English Language', 'General Mathematics', 'Civic Education', 'Economics', 'Lit In English', 'Government',
            'CRK', 'IRK', 'History', 'Home Management', 'Igbo', 'Hausa', 'Yoruba', 'Government']

commercials = ['English Language', 'General Mathematics', 'Civic Education', 'Marketing', 'Commerce', 'Financial Accounting',
                'CRK', 'IRK', 'Insurance', 'Office Practice', 'Store Keeping', 'Book keeping', 'Economics' ]


juniors = ['English Language', 'General Mathematics', 'Basic Science and Technology', 'Business Studies',
                'French', 'Igbo', 'Hausa', 'Yoruba', 'Prevocational Studies', 'Health Education']

@receiver(post_save, sender= Customuser)
def create_subject(sender, instance, created, **kwargs):
    if created:
        """#instance = kwargs['instance']
        #updated   = kwargs['update_fields']
        print("================================ a model has just been created ==============================")
        print(instance)
        print('==========================')
        print(updated)"""

        cc = instance.current_class
        if cc == 'SSS 1 SMART' or cc == 'SSS 2 SMART' or cc == 'SSS 3 SMART':
            for subject in sciences:
                subcreator_1 = Subjectz.objects.create(student=instance, title = subject, term = 'First Term', session=session)
                subcreator_2 = Subject_2.objects.create(student=instance, title=subject, term = 'Second Term', session=session)
                subcreator_3 = Subject_3.objects.create(student=instance, title=subject, term = 'Third Term', session=session)
                subcreator_1.save()
                subcreator_2.save()
                subcreator_3.save()
        elif cc == 'SSS 1 HARMONY' or cc == 'SSS 2 HARMONY' or cc == 'SSS 3 HARMONY':
            for subject in arts:
                subcreator_1 = Subjectz.objects.create(student=instance, title=subject, term='First Term', session=session)
                subcreator_2 = Subject_2.objects.create(student=instance, title=subject, term='Second Term', session=session)
                subcreator_3 = Subject_3.objects.create(student=instance, title=subject, term='Third Term', session=session)
                subcreator_1.save()
                subcreator_2.save()
                subcreator_3.save()
        elif cc == 'SSS 1 SPECIAL' or cc == 'SSS 2 SPECIAL' or cc == 'SSS 3 SPECIAL':
            for subject in commercials:
                subcreator_1 = Subjectz.objects.create(student=instance, title=subject, term='First Term', session=session)
                subcreator_2 = Subject_2.objects.create(student=instance, title=subject, term='Second Term', session=session)
                subcreator_3 = Subject_3.objects.create(student=instance, title=subject, term='Third Term', session=session)
                subcreator_1.save()
                subcreator_2.save()
                subcreator_3.save()
        elif cc == 'JSS 1 BLUE' or cc =='JSS 2 BLUE' or cc == 'JSS 3 BLUE' or cc == 'JSS 1 GREEN' or cc == 'JSS 2 GREEN' or cc == 'JSS 3 GREEN' or cc == 'JSS 1 YELLOW' or cc == 'JSS 2 YELLOW' or cc == 'JSS 3 YELLOW' :
            for subject in juniors:
                subcreator_1 = Subjectz.objects.create(student=instance, title=subject, term='First Term', session=session)
                subcreator_2 = Subject_2.objects.create(student=instance, title=subject, term='Second Term', session=session)
                subcreator_3 = Subject_3.objects.create(student=instance, title=subject, term='Third Term', session=session)
                subcreator_1.save()
                subcreator_2.save()
                subcreator_3.save()
        else:
            print("======================== No model was created ============================")
            """subcreator_1 = Subjectz.objects.create(student=instance, title=subject, term='First Term')
            subcreator_2 = Subject_2.objects.create(student=instance, title=subject, term='Second Term')
            subcreator_3 = Subject_3.objects.create(student=instance, title=subject, term='Third Term')
            subcreator_1.save()
            subcreator_2.save()
            subcreator_3.save()"""

#function to handle the changing of classes for all students at the end of every session
def change_class(year):
    all_students = Customuser.objects.all()
    jss1_2 = ['JSS 1 BLUE', 'JSS 1 GREEN', 'JSS 1 YELLOW', 'JSS 2 BLUE', 'JSS 2 GREEN', 'JSS 2 YELLOW']
    jss3 = ['JSS 3 BLUE', 'JSS 3 GREEN', 'JSS 3 YELLOW']
    sss1_2 = ['SSS 1 HARMONY', 'SSS 1 SMART', 'SSS 1 SPECIAL', 'SSS 2 HARMONY', 'SSS 2 SMART', 'SSS 2 SPECIAL']
    sss3 = ['SSS 3 HARMONY', 'SSS 3 SMART', 'SSS 3 SPECIAL']
    for student in all_students:
        print(student)
        #helper function to change the old class name to the new class name based on the session
        def class_name_replace(class_name):
            old_str = class_name[4]
            new_int = int(old_str) + 1
            new_str = str(new_int)
            class_name = class_name.replace(old_str, new_str)
            student.current_class = class_name
            student.save(update_fields=['current_class'])
            #student.update(current_class=class_name)
            print('{} current_class has been updated'.format(student.username))
            return class_name

        #helper function to create subjects for the new session
        def create_subjects_for_new_session(year, subject):
            subcreator_1 = Subjectz.objects.create(student=student, title=subject, term='First Term', session=year)
            subcreator_2 = Subject_2.objects.create(student=student, title=subject, term='Second Term', session=year)
            subcreator_3 = Subject_3.objects.create(student=student, title=subject, term='Third Term', session=year)
            subcreator_1.save()
            subcreator_2.save()
            subcreator_3.save()
            print('{} saved for all terms'.format(subject))
        student_class  = student.current_class
        if student_class in jss1_2:
            print('==================================')
            print(student_class)
            student_class = class_name_replace(student_class)
            print(student_class)
            for sub in juniors:
                create_subjects_for_new_session(year, sub)
            print("===================================")
        elif student_class in jss3:
            print('jss3 student ...special case')
        elif student_class in sss1_2:
            class_suffix = student_class[6:]
            if class_suffix == 'SMART':
                for sub in sciences:
                    create_subjects_for_new_session(year, sub)
            elif class_suffix == 'SPECIAL':
                for sub in commercials:
                    create_subjects_for_new_session(year, sub)
            elif class_suffix == 'HARMONY':
                for sub in arts:
                    create_subjects_for_new_session(year, sub)
            print('==================================')
            print(student_class)
            student_class = class_name_replace(student_class)
            print(student_class)
            print("===================================")
        elif student_class in sss3:
            print('================The student will be moved to the class of Graduates======================')
            student.current_class = 'Graduated'
            student.save(update_fields=['current_class'])

        else:
            print("else case")



