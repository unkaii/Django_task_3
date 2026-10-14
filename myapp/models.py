from django.db import models


class Grade(models.Model):
    student = models.CharField(max_length=200, verbose_name='ФИО студента')
    subject = models.CharField(max_length=200, verbose_name='Предмет')
    grade = models.IntegerField(verbose_name='Оценка')
    date = models.DateField(verbose_name='Дата')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        ordering = ['-date', 'student']
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'subject', 'grade', 'date'],
                name='unique_grade_record',
            )
        ]

    def __str__(self):
        return f'{self.student} — {self.subject} — {self.grade}'